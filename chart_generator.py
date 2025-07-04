import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

def generate_chart(df, chart_type, x_col, y_col, title, column_types):
    """Generate a chart based on the type and columns."""
    suggestion = None
    
    # Handle missing data for the selected columns
    if x_col and x_col in df.columns:
        if df[x_col].isnull().sum() > 0:
            suggestion = f"⚠️ The '{x_col}' column has {df[x_col].isnull().sum()} missing values."
            
            # For numeric columns, fill with median
            if pd.api.types.is_numeric_dtype(df[x_col]):
                df = df.copy()
                df[x_col] = df[x_col].fillna(df[x_col].median())
                suggestion += " Missing values were filled with the median."
            # For categorical/text columns, omit missing values
            else:
                df = df.copy()
                df = df.dropna(subset=[x_col])
                suggestion += " Rows with missing values were omitted."
    
    if y_col and y_col in df.columns:
        if df[y_col].isnull().sum() > 0:
            if suggestion:
                suggestion += f"\n⚠️ The '{y_col}' column has {df[y_col].isnull().sum()} missing values."
            else:
                suggestion = f"⚠️ The '{y_col}' column has {df[y_col].isnull().sum()} missing values."
            
            # For numeric columns, fill with median
            if pd.api.types.is_numeric_dtype(df[y_col]):
                df = df.copy()
                df[y_col] = df[y_col].fillna(df[y_col].median())
                suggestion += " Missing values were filled with the median."
            # For categorical/text columns, omit missing values
            else:
                df = df.copy()
                df = df.dropna(subset=[y_col])
                suggestion += " Rows with missing values were omitted."
    
    # Generate chart based on type
    if chart_type == 'bar':
        # Check if we need to aggregate the data
        if column_types[x_col] == 'categorical':
            if y_col:
                # If y_col is provided, create a grouped bar chart
                fig = px.bar(
                    df, 
                    x=x_col, 
                    y=y_col,
                    title=title,
                    labels={x_col: x_col.replace('_', ' ').title(), y_col: y_col.replace('_', ' ').title()},
                    color_discrete_sequence=px.colors.qualitative.Plotly
                )
            else:
                # If no y_col, create a count-based bar chart
                value_counts = df[x_col].value_counts().reset_index()
                value_counts.columns = [x_col, 'count']
                
                fig = px.bar(
                    value_counts, 
                    x=x_col, 
                    y='count',
                    title=title,
                    labels={x_col: x_col.replace('_', ' ').title(), 'count': 'Count'},
                    color_discrete_sequence=px.colors.qualitative.Plotly
                )
        else:
            suggestion = f"⚠️ The '{x_col}' column might not be ideal for a bar chart's x-axis. Consider using a categorical column instead."
            # Proceed anyway with the requested chart
            fig = px.bar(
                df, 
                x=x_col, 
                y=y_col,
                title=title,
                labels={x_col: x_col.replace('_', ' ').title(), y_col: y_col.replace('_', ' ').title() if y_col else 'Count'},
                color_discrete_sequence=px.colors.qualitative.Plotly
            )
    
    elif chart_type == 'pie':
        # For pie charts, we need to aggregate the data
        value_counts = df[x_col].value_counts().reset_index()
        value_counts.columns = [x_col, 'count']
        
        fig = px.pie(
            value_counts, 
            names=x_col, 
            values='count',
            title=title,
            labels={x_col: x_col.replace('_', ' ').title(), 'count': 'Count'},
            color_discrete_sequence=px.colors.qualitative.Plotly
        )
        
        # Check if there are too many categories for a pie chart
        if len(value_counts) > 10:
            suggestion = f"⚠️ There are {len(value_counts)} categories in '{x_col}'. Consider using a bar chart for better readability."
    
    elif chart_type == 'line':
        # For line charts, check if x-axis is datetime or numeric
        if column_types[x_col] == 'datetime':
            # Sort by date for line charts
            df_sorted = df.sort_values(by=x_col)
            
            fig = px.line(
                df_sorted, 
                x=x_col, 
                y=y_col,
                title=title,
                labels={x_col: x_col.replace('_', ' ').title(), y_col: y_col.replace('_', ' ').title()},
                markers=True
            )
        elif column_types[x_col] == 'numerical':
            # Sort by numeric x-axis
            df_sorted = df.sort_values(by=x_col)
            
            fig = px.line(
                df_sorted, 
                x=x_col, 
                y=y_col,
                title=title,
                labels={x_col: x_col.replace('_', ' ').title(), y_col: y_col.replace('_', ' ').title()},
                markers=True
            )
        else:
            suggestion = f"⚠️ The '{x_col}' column might not be ideal for a line chart's x-axis. Line charts work best with time-based or numeric x-axes."
            
            # If categorical x-axis, suggest grouping the data
            if column_types[x_col] == 'categorical':
                grouped_data = df.groupby(x_col)[y_col].mean().reset_index()
                
                fig = px.line(
                    grouped_data, 
                    x=x_col, 
                    y=y_col,
                    title=title + " (Averaged)",
                    labels={x_col: x_col.replace('_', ' ').title(), y_col: f"Average {y_col}".replace('_', ' ').title()},
                    markers=True
                )
                
                suggestion += f" Showing average {y_col} for each {x_col} category."
            else:
                # Fallback to a simple line chart
                fig = px.line(
                    df, 
                    x=x_col, 
                    y=y_col,
                    title=title,
                    labels={x_col: x_col.replace('_', ' ').title(), y_col: y_col.replace('_', ' ').title()},
                    markers=True
                )
    
    elif chart_type == 'scatter':
        fig = px.scatter(
            df, 
            x=x_col, 
            y=y_col,
            title=title,
            labels={x_col: x_col.replace('_', ' ').title(), y_col: y_col.replace('_', ' ').title()},
            opacity=0.7
        )
        
        # Add trendline if both columns are numeric
        if column_types[x_col] == 'numerical' and column_types[y_col] == 'numerical':
            # Add trendline
            fig.update_layout(
                shapes=[
                    dict(
                        type='line',
                        yref='paper', y0=0, y1=1,
                        xref='paper', x0=0, x1=1,
                        line=dict(color="red", width=2, dash="dash")
                    )
                ]
            )
            
            # Calculate correlation coefficient
            correlation = df[x_col].corr(df[y_col])
            suggestion = f"The correlation between '{x_col}' and '{y_col}' is {correlation:.2f}"
    
    elif chart_type == 'histogram':
        fig = px.histogram(
            df, 
            x=x_col,
            title=title,
            labels={x_col: x_col.replace('_', ' ').title()},
            opacity=0.7
        )
        
        # Add a curve of the distribution
        fig.update_layout(
            showlegend=True
        )
        
        # Calculate statistics
        mean_val = df[x_col].mean()
        median_val = df[x_col].median()
        
        # Add mean and median lines
        fig.add_vline(x=mean_val, line_dash="dash", line_color="red",
                      annotation_text=f"Mean: {mean_val:.2f}", 
                      annotation_position="top right")
        fig.add_vline(x=median_val, line_dash="dash", line_color="green",
                      annotation_text=f"Median: {median_val:.2f}", 
                      annotation_position="top left")
    
    elif chart_type == 'box':
        fig = px.box(
            df, 
            y=x_col,
            title=title,
            labels={x_col: x_col.replace('_', ' ').title()}
        )
        
        # Add a mean marker
        mean_val = df[x_col].mean()
        fig.add_annotation(
            x=0, y=mean_val,
            text=f"Mean: {mean_val:.2f}",
            showarrow=True,
            arrowhead=2,
            arrowcolor="red",
            ax=50,
            ay=0
        )
    
    elif chart_type == 'heatmap':
        # For heatmap, we need numeric columns
        numeric_columns = [col for col, type_val in column_types.items() if type_val == 'numerical']
        
        if len(numeric_columns) < 2:
            suggestion = "Not enough numeric columns for a correlation heatmap."
            # Default to a different chart type
            fig = px.histogram(
                df, 
                x=x_col,
                title=title,
                labels={x_col: x_col.replace('_', ' ').title()}
            )
        else:
            # Calculate correlation matrix
            corr_matrix = df[numeric_columns].corr()
            
            # Create heatmap
            fig = px.imshow(
                corr_matrix,
                title="Correlation Matrix",
                labels=dict(x="Features", y="Features", color="Correlation"),
                x=corr_matrix.columns,
                y=corr_matrix.columns,
                color_continuous_scale=px.colors.diverging.RdBu_r,
                zmin=-1, zmax=1
            )
    else:
        # Default to a bar chart if chart type is not recognized
        fig = px.bar(
            df, 
            x=x_col, 
            y=y_col if y_col else df[x_col].value_counts().values,
            title=title if title else f"Chart of {x_col}",
            labels={
                x_col: x_col.replace('_', ' ').title(), 
                y_col: y_col.replace('_', ' ').title() if y_col else 'Count'
            }
        )
        suggestion = "Could not determine the chart type from your request, so a bar chart was created."
    
    # Enhance the chart appearance
    fig.update_layout(
        plot_bgcolor='white',
        font=dict(size=12),
        margin=dict(l=40, r=40, t=50, b=40),
        title={
            'text': title,
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=18)
        }
    )
    
    # Add hover information
    fig.update_traces(
        hovertemplate="<b>%{x}</b><br>%{y}<extra></extra>" if chart_type != 'pie' else None
    )
    
    return fig, suggestion