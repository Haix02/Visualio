# Visualio - Data Visualization Assistant 📊

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.29.0-red)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

Visualio is an intelligent data visualization application that allows users to create beautiful, interactive charts from their data using natural language commands. No coding required!

## ✨ Features

- **Natural Language Processing**: Describe what you want to visualize in plain English
- **Multiple Chart Types**: Bar charts, pie charts, line graphs, scatter plots, histograms
- **File Format Support**: CSV and Excel files (.csv, .xlsx, .xls)
- **Interactive Visualizations**: Powered by Plotly for responsive, interactive charts
- **Data Analysis**: Automatic data type detection and missing value handling
- **Export Options**: Save charts as PNG images or interactive HTML files
- **User-Friendly Interface**: Clean, intuitive web interface built with Streamlit

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Haix02/Visualio.git
cd Visualio
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run app.py
```

4. Open your web browser and navigate to `http://localhost:8501`

## 📖 How to Use

1. **Upload Your Data**: Choose a CSV or Excel file using the file uploader
2. **Explore Your Data**: View data summary, column types, and preview
3. **Create Visualizations**: Type natural language commands to generate charts
4. **Export Results**: Download your charts as PNG or HTML files

### Example Commands

- `"Show sales by region as a pie chart"`
- `"Trend of revenue over time"`
- `"Compare product categories using bar chart"`
- `"Show correlation between price and quantity"`
- `"Distribution of values in age column"`

## 🛠️ Technical Architecture

The application consists of four main modules:

- **`app.py`**: Main Streamlit application and user interface
- **`data_processor.py`**: Data loading, cleaning, and type detection
- **`nlp_parser.py`**: Natural language command parsing and interpretation
- **`chart_generator.py`**: Chart creation and styling using Plotly

## 📊 Supported Chart Types

| Chart Type | Use Case | Example Command |
|------------|----------|----------------|
| Bar Chart | Compare categories | "Compare sales by product" |
| Pie Chart | Show proportions | "Distribution of customers by region" |
| Line Chart | Show trends over time | "Revenue trend over months" |
| Scatter Plot | Show correlations | "Relationship between price and sales" |
| Histogram | Show distributions | "Distribution of customer ages" |

## 🔧 Configuration

### Dependencies

The application requires the following Python packages:

- `streamlit==1.29.0` - Web application framework
- `pandas==2.0.3` - Data manipulation and analysis
- `plotly==5.18.0` - Interactive visualization library
- `numpy==1.24.3` - Numerical computing
- `openpyxl==3.1.2` - Excel file support
- `pillow==10.1.0` - Image processing

### Environment Setup

For development, you may want to create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## 🤝 Contributing

We welcome contributions! Please feel free to submit issues and pull requests.

### Development Setup

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎯 Roadmap

- [ ] Support for more file formats (JSON, XML, Parquet)
- [ ] Advanced statistical visualizations
- [ ] Dashboard creation capabilities
- [ ] Real-time data streaming support
- [ ] Custom color themes and styling
- [ ] API integration for data sources

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/) for the web interface
- Powered by [Plotly](https://plotly.com/) for interactive visualizations
- Data processing with [Pandas](https://pandas.pydata.org/)

## 📞 Support

If you encounter any issues or have questions, please:
1. Check the [Issues](https://github.com/Haix02/Visualio/issues) page
2. Create a new issue with detailed information
3. Contact the development team

---

Made with ❤️ by the Visualio team