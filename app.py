import streamlit as st
import pandas as pd
import io
import base64
from PIL import Image

from data_processor import process_data, detect_column_types
from nlp_parser import parse_command
from chart_generator import generate_chart

st.set_page_config(page_title="Data Visualization App", layout="wide")

st.title("Data Visualization Assistant")
st.markdown("""
Upload your data file (CSV or Excel) and use natural language to create beautiful visualizations.
No coding required!
""")

# File upload section
uploaded_file = st.file_uploader("Choose a CSV or Excel file", type=["csv", "xlsx"])

# Example commands sidebar
with st.sidebar:
    st.subheader("Example Commands")
    st.info("""
    Try these commands:
    - "Show sales by region as a pie chart"
    - "Trend of revenue over time"
    - "Compare product categories using bar chart"
    - "Show correlation between price and quantity"
    - "Distribution of values in column X"
    """)
    
    # Export options
    st.subheader("Export Options")
    export_format = st.radio("Export Format", ["PNG", "HTML"], index=0)

# Main content area
if uploaded_file is not None:
    try:
        # Process the uploaded file
        df, error = process_data(uploaded_file)
        
        if error:
            st.error(error)
        else:
            st.success("File loaded successfully!")
            
            # Display basic info about the data
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**Rows:** {df.shape[0]}")
                st.write(f"**Columns:** {df.shape[1]}")
            
            with col2:
                missing_data = df.isnull().sum().sum()
                if missing_data > 0:
                    st.warning(f"⚠️ Found {missing_data} missing values in the dataset")
                else:
                    st.write("✅ No missing values detected")
            
            # Display column information
            st.subheader("Column Information")
            column_types = detect_column_types(df)
            col_info = pd.DataFrame({
                "Type": [column_types[col] for col in df.columns],
                "Sample Values": [', '.join(str(x) for x in df[col].dropna().head(3).tolist()) for col in df.columns]
            }, index=df.columns)
            st.dataframe(col_info)
            
            # Sample of the data
            with st.expander("Preview Data"):
                st.dataframe(df.head())
            
            # Command input
            st.subheader("Create Visualization")
            command = st.text_input("Describe what you want to visualize", 
                                   placeholder="e.g., Show sales by region as a pie chart")
            
            if command:
                # Parse the command and generate appropriate chart
                chart_type, x_col, y_col, title, error = parse_command(command, df, column_types)
                
                if error:
                    st.error(error)
                else:
                    # Generate the chart
                    fig, suggestion = generate_chart(df, chart_type, x_col, y_col, title, column_types)
                    
                    if suggestion:
                        st.info(suggestion)
                    
                    # Display the chart
                    st.plotly_chart(fig, use_container_width=True)
                    
                    # Export options
                    if st.button("Export Chart"):
                        if export_format == "PNG":
                            # Export as PNG
                            buffer = io.BytesIO()
                            fig.write_image(buffer, format="png", width=1200, height=800)
                            buffer.seek(0)
                            
                            btn = st.download_button(
                                label="Download PNG",
                                data=buffer,
                                file_name="chart.png",
                                mime="image/png"
                            )
                        else:
                            # Export as HTML
                            buffer = io.StringIO()
                            fig.write_html(buffer)
                            html_bytes = buffer.getvalue().encode()
                            
                            btn = st.download_button(
                                label="Download HTML",
                                data=html_bytes,
                                file_name="chart.html",
                                mime="text/html"
                            )
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
else:
    # Show welcome message when no file is uploaded
    st.info("👆 Upload a file to get started!")
    
    # Show sample visualizations
    st.subheader("Sample Visualizations")
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://plotly.com/~PlotBot/6431.png", caption="Sample Bar Chart")
    with col2:
        st.image("https://plotly.com/~PlotBot/6435.png", caption="Sample Line Chart")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit and Plotly")