import pandas as pd
import numpy as np
from datetime import datetime
import re

def process_data(file):
    """Process the uploaded file and return a pandas DataFrame."""
    try:
        # Check file extension
        file_name = file.name.lower()
        if file_name.endswith('.csv'):
            df = pd.read_csv(file)
        elif file_name.endswith(('.xls', '.xlsx')):
            df = pd.read_excel(file)
        else:
            return None, "Unsupported file format. Please upload a CSV or Excel file."
        
        # Handle missing values - notify but don't modify original data yet
        return df, None
    except Exception as e:
        return None, f"Error processing file: {str(e)}"

def is_datetime(column):
    """Check if a column could be a datetime."""
    if column.dtype == 'datetime64[ns]':
        return True
    
    # Try converting string columns to datetime
    if column.dtype == object:
        try:
            # Check if at least 80% of non-null values can be parsed as dates
            non_null_count = column.count()
            if non_null_count == 0:
                return False
            
            # Try a few common date formats
            date_count = 0
            for val in column.dropna().head(100):  # Check just first 100 values for performance
                try:
                    pd.to_datetime(val)
                    date_count += 1
                except:
                    continue
            
            sample_size = min(100, non_null_count)
            return date_count / sample_size > 0.8
        except:
            return False
    
    return False

def is_categorical(column):
    """Check if a column should be treated as categorical."""
    if column.dtype == 'object':
        # If many unique values relative to length, probably not categorical
        unique_ratio = column.nunique() / column.count() if column.count() > 0 else 0
        if unique_ratio < 0.2 or column.nunique() < 10:
            return True
    
    # Check for low-cardinality numeric columns
    elif pd.api.types.is_numeric_dtype(column):
        if column.nunique() < 10:
            return True
    
    return False

def detect_column_types(df):
    """Detect the types of columns in the DataFrame."""
    column_types = {}
    
    for col in df.columns:
        if is_datetime(df[col]):
            column_types[col] = 'datetime'
        elif is_categorical(df[col]):
            column_types[col] = 'categorical'
        elif pd.api.types.is_numeric_dtype(df[col]):
            column_types[col] = 'numerical'
        else:
            column_types[col] = 'text'
            
    return column_types

def handle_missing_data(df, strategy='warn'):
    """Handle missing data in the DataFrame."""
    missing_cols = df.columns[df.isnull().any()].tolist()
    
    if strategy == 'warn':
        # Just return information about missing data
        missing_info = {col: df[col].isnull().sum() for col in missing_cols}
        return df, missing_info
    
    elif strategy == 'auto':
        # Make a copy to avoid modifying the original
        df_clean = df.copy()
        
        for col in missing_cols:
            if pd.api.types.is_numeric_dtype(df[col]):
                # For numeric columns, fill with median
                df_clean[col] = df_clean[col].fillna(df_clean[col].median())
            else:
                # For non-numeric columns, fill with mode if it exists
                if not df_clean[col].dropna().empty:
                    df_clean[col] = df_clean[col].fillna(df_clean[col].mode()[0])
                
        return df_clean, missing_cols
    
    return df, []