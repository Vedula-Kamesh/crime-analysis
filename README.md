# Crime Analysis Dashboard

![DashboardScreenshot](Dashboard Screenshot.png)

An interactive Power BI dashboard analyzing crime patterns in Los Angeles (2020–present), powered by Python ETL and SQL Server.

## 📁 Project Structure
crime-analysis-dashboard/
├── data_processing/ # Data pipeline scripts
│ ├── crime_etl.py # Python ETL script (data cleaning)
│ └── crime_schema.sql # SQL Server schema definition
├── powerbi/ # Dashboard files
│ └── crime_dashboard.pbix # Main Power BI report
├── docs/ # Documentation
│  ── screenshots/ # Dashboard previews
├── .gitignore # Excluded files
└── LICENSE # MIT License

text

## 🛠️ Setup Guide

### Prerequisites
- **Power BI Desktop** (v2.120+)
- **Python 3.10+** (with `pandas`, `pyodbc`)
- **SQL Server** (2019+) or Azure SQL DB

### Installation
1. **Database Setup**:
   ```bash
   sqlcmd -S your_server -U username -P password -i data_processing/crime_schema.sql
ETL Pipeline:

bash
cd data_processing
pip install -r requirements.txt  # Install Python dependencies
python crime_etl.py
Power BI:

Open powerbi/crime_dashboard.pbix

Set data source credentials in:

text
Home → Transform data → Data source settings
🔍 Key Features
Feature	Description	Example Use Case
Crime Hotspots	Leaflet map with precise coordinates	Identify high-crime neighborhoods
Time Trends	Quarterly/hourly crime patterns	Optimize police patrol schedules
Crime Rankings	Top 10 crime types by frequency	Allocate resources to top risks
📊 Data Flow
Diagram
Code





🚀 Usage
Apply Filters:

Use the Year slider to focus on specific periods

Click crime types in the legend to isolate patterns

Export Data:

powerquery
// Power BI: File → Export → CSV/PDF
🤝 Contributing
Fork the repository

Create a feature branch:

bash
git checkout -b feature/heatmap-enhancements
Submit a Pull Request with:

Tested changes

Updated documentation

📜 License
MIT License - See LICENSE for details.

📬 Contact
Vedula Kamesh Babu - vkv333kamesh@gmail.com

Project Link: github.com/Vedula-Kamesh/crime-analysis-dashboard