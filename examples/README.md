# Visualio Examples 📊

This directory contains example datasets and usage scenarios to help you get started with Visualio.

## Sample Datasets

### 1. Sales Data (`sales_data.csv`)
Contains fictional sales data with the following columns:
- **Product**: Product category (Laptops, Tablets, Smartphones)
- **Region**: Geographic region (North America, Europe, Asia, South America)
- **Sales**: Number of units sold
- **Quarter**: Sales quarter (Q1, Q2)
- **Revenue**: Revenue generated
- **Customer_Satisfaction**: Customer satisfaction score (1-5)

#### Example Commands:
- `"Show sales by product as a pie chart"`
- `"Compare revenue across regions using bar chart"`
- `"Revenue trend by quarter"`
- `"Correlation between sales and customer satisfaction"`

### 2. Employee Data (`employee_data.csv`)
Contains fictional employee information with the following columns:
- **Employee_ID**: Unique identifier
- **Name**: Employee name
- **Department**: Department (Engineering, Marketing, Sales, HR, Finance)
- **Age**: Employee age
- **Salary**: Annual salary
- **Performance_Score**: Performance rating (1-5)
- **Years_Experience**: Years of work experience
- **Education_Level**: Education level (Bachelor, Master, PhD)
- **City**: Work location

#### Example Commands:
- `"Show salary distribution by department"`
- `"Age distribution of employees"`
- `"Performance score vs years of experience"`
- `"Average salary by education level"`

## How to Use These Examples

1. **Start Visualio**: Run `streamlit run app.py` in the main directory
2. **Upload Data**: Use the file uploader to select one of the sample CSV files
3. **Try Commands**: Use the example commands provided above
4. **Experiment**: Create your own natural language queries!

## Tips for Creating Commands

- **Be specific**: Mention column names and chart types
- **Use natural language**: Write as if you're talking to a person
- **Try variations**: The same data can be visualized in multiple ways
- **Explore relationships**: Look for correlations and patterns

## Common Command Patterns

| Pattern | Example |
|---------|---------|
| Distribution | `"Distribution of [column] as histogram"` |
| Comparison | `"Compare [column1] by [column2] using bar chart"` |
| Trend | `"[column] trend over [time_column]"` |
| Correlation | `"Relationship between [column1] and [column2]"` |
| Proportion | `"[column] breakdown as pie chart"` |

## Need More Help?

- Check the main README.md for detailed documentation
- Look at the sidebar in the app for example commands
- Experiment with different phrasings for the same request
- Remember that Visualio can handle various file formats (CSV, Excel)