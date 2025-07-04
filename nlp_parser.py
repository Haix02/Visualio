import re
import pandas as pd

def parse_command(command, df, column_types):
    """
    Parse the natural language command to determine what visualization to create.
    
    Returns:
    - chart_type: The type of chart to create
    - x_col: Column to use for x-axis
    - y_col: Column to use for y-axis (None for single variable charts)
    - title: Title for the chart
    - error: Error message if parsing fails
    """
    command = command.lower()
    
    # Default values
    chart_type = None
    x_col = None
    y_col = None
    title = None
    error = None
    
    # Extract explicit chart types mentioned in the command
    chart_keywords = {
        'bar': ['bar', 'column', 'compare'],
        'pie': ['pie', 'donut', 'proportion', 'percentage'],
        'line': ['line', 'trend', 'over time', 'timeseries', 'time series'],
        'scatter': ['scatter', 'correlation', 'relationship'],
        'histogram': ['histogram', 'distribution'],
        'box': ['box', 'boxplot', 'whisker'],
        'heatmap': ['heatmap', 'heat map', 'correlation matrix']
    }
    
    # Check for explicit chart types
    detected_chart_types = []
    for chart, keywords in chart_keywords.items():
        if any(keyword in command for keyword in keywords):
            detected_chart_types.append(chart)
    
    # Find column names in the command
    potential_columns = []
    for col in df.columns:
        if col.lower() in command:
            potential_columns.append(col)
    
    # If no columns found, look for partial matches
    if not potential_columns:
        for col in df.columns:
            col_parts = col.lower().split()
            if any(part in command for part in col_parts if len(part) > 2):
                potential_columns.append(col)
    
    # Handle specific visualization types
    if 'pie' in detected_chart_types:
        # Pie charts typically show distribution of one categorical variable
        categorical_cols = [col for col, type_val in column_types.items() 
                          if type_val == 'categorical' and col in potential_columns]
        
        if not categorical_cols and potential_columns:
            categorical_cols = potential_columns
        
        if categorical_cols:
            chart_type = 'pie'
            x_col = categorical_cols[0]
            title = f"Distribution of {x_col}"
        else:
            # Look for any categorical column
            categorical_cols = [col for col, type_val in column_types.items() 
                              if type_val == 'categorical']
            if categorical_cols:
                chart_type = 'pie'
                x_col = categorical_cols[0]
                title = f"Distribution of {x_col}"
            else:
                error = "Could not find a suitable categorical column for a pie chart."
    
    elif 'bar' in detected_chart_types:
        # Bar charts typically compare values across categories
        categorical_cols = [col for col, type_val in column_types.items() 
                          if type_val == 'categorical' and col in potential_columns]
        numerical_cols = [col for col, type_val in column_types.items() 
                         if type_val == 'numerical' and col in potential_columns]
        
        if categorical_cols and numerical_cols:
            chart_type = 'bar'
            x_col = categorical_cols[0]
            y_col = numerical_cols[0]
            title = f"{y_col} by {x_col}"
        elif categorical_cols:
            chart_type = 'bar'
            x_col = categorical_cols[0]
            # Find a numerical column
            for col, type_val in column_types.items():
                if type_val == 'numerical':
                    y_col = col
                    break
            title = f"Count of {x_col}"
        else:
            # Default to the first categorical and numerical columns
            categorical_cols = [col for col, type_val in column_types.items() 
                              if type_val == 'categorical']
            numerical_cols = [col for col, type_val in column_types.items() 
                             if type_val == 'numerical']
            
            if categorical_cols and numerical_cols:
                chart_type = 'bar'
                x_col = categorical_cols[0]
                y_col = numerical_cols[0]
                title = f"{y_col} by {x_col}"
            else:
                error = "Could not find suitable categorical and numerical columns for a bar chart."
    
    elif 'line' in detected_chart_types:
        # Line charts typically show trends over time
        datetime_cols = [col for col, type_val in column_types.items() 
                       if type_val == 'datetime' and col in potential_columns]
        numerical_cols = [col for col, type_val in column_types.items() 
                         if type_val == 'numerical' and col in potential_columns]
        
        if datetime_cols and numerical_cols:
            chart_type = 'line'
            x_col = datetime_cols[0]
            y_col = numerical_cols[0]
            title = f"{y_col} over Time"
        else:
            # Try to find any datetime and numerical columns
            datetime_cols = [col for col, type_val in column_types.items() 
                           if type_val == 'datetime']
            numerical_cols = [col for col, type_val in column_types.items() 
                             if type_val == 'numerical']
            
            if datetime_cols and numerical_cols:
                chart_type = 'line'
                x_col = datetime_cols[0]
                y_col = numerical_cols[0]
                title = f"{y_col} over Time"
            else:
                error = "Could not find suitable datetime and numerical columns for a line chart."
    
    elif 'scatter' in detected_chart_types:
        # Scatter plots show relationship between two numerical variables
        numerical_cols = [col for col, type_val in column_types.items() 
                         if type_val == 'numerical' and col in potential_columns]
        
        if len(numerical_cols) >= 2:
            chart_type = 'scatter'
            x_col = numerical_cols[0]
            y_col = numerical_cols[1]
            title = f"Relationship between {x_col} and {y_col}"
        else:
            # Try to find any two numerical columns
            numerical_cols = [col for col, type_val in column_types.items() 
                             if type_val == 'numerical']
            
            if len(numerical_cols) >= 2:
                chart_type = 'scatter'
                x_col = numerical_cols[0]
                y_col = numerical_cols[1]
                title = f"Relationship between {x_col} and {y_col}"
            else:
                error = "Could not find two suitable numerical columns for a scatter plot."
    
    elif 'histogram' in detected_chart_types:
        # Histograms show the distribution of a numerical variable
        numerical_cols = [col for col, type_val in column_types.items() 
                         if type_val == 'numerical' and col in potential_columns]
        
        if numerical_cols:
            chart_type = 'histogram'
            x_col = numerical_cols[0]
            title = f"Distribution of {x_col}"
        else:
            # Try to find any numerical column
            numerical_cols = [col for col, type_val in column_types.items() 
                             if type_val == 'numerical']
            
            if numerical_cols:
                chart_type = 'histogram'
                x_col = numerical_cols[0]
                title = f"Distribution of {x_col}"
            else:
                error = "Could not find a suitable numerical column for a histogram."
    
    # If no specific chart type detected, make a best guess based on the columns mentioned
    if not chart_type:
        categorical_cols = [col for col, type_val in column_types.items() 
                          if type_val == 'categorical' and col in potential_columns]
        numerical_cols = [col for col, type_val in column_types.items() 
                         if type_val == 'numerical' and col in potential_columns]
        datetime_cols = [col for col, type_val in column_types.items() 
                       if type_val == 'datetime' and col in potential_columns]
        
        if datetime_cols and numerical_cols:
            chart_type = 'line'
            x_col = datetime_cols[0]
            y_col = numerical_cols[0]
            title = f"{y_col} over Time"
        elif categorical_cols and numerical_cols:
            chart_type = 'bar'
            x_col = categorical_cols[0]
            y_col = numerical_cols[0]
            title = f"{y_col} by {x_col}"
        elif len(numerical_cols) >= 2:
            chart_type = 'scatter'
            x_col = numerical_cols[0]
            y_col = numerical_cols[1]
            title = f"Relationship between {x_col} and {y_col}"
        elif numerical_cols:
            chart_type = 'histogram'
            x_col = numerical_cols[0]
            title = f"Distribution of {x_col}"
        elif categorical_cols:
            chart_type = 'pie'
            x_col = categorical_cols[0]
            title = f"Distribution of {x_col}"
        else:
            # Default fallback - find any suitable columns
            categorical_cols = [col for col, type_val in column_types.items() 
                              if type_val == 'categorical']
            numerical_cols = [col for col, type_val in column_types.items() 
                             if type_val == 'numerical']
            
            if categorical_cols and numerical_cols:
                chart_type = 'bar'
                x_col = categorical_cols[0]
                y_col = numerical_cols[0]
                title = f"{y_col} by {x_col}"
            elif categorical_cols:
                chart_type = 'pie'
                x_col = categorical_cols[0]
                title = f"Distribution of {x_col}"
            elif numerical_cols:
                chart_type = 'histogram'
                x_col = numerical_cols[0]
                title = f"Distribution of {x_col}"
            else:
                error = "Could not determine what to visualize based on your command."
    
    return chart_type, x_col, y_col, title, error