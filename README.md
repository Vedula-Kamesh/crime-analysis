# Crime Analysis Dashboard

![Dashboard_Screenshot](Screenshot/Dashboard%20Screenshot.png)

An interactive Power BI dashboard analyzing crime patterns in Los Angeles (2020–present), powered by Python ETL and SQL Server.

## 📁 Project Structure
crime-analysis-dashboard/<br>
├── data_processing/ # Data pipeline scripts                                                                                                                                                                 
│ ├── crime_etl.py # Python ETL script (data cleaning)<br>                                                                                                                                                           │ └── crime_schema.sql # SQL Server schema definition<br>                                                                                                                                                            ├── powerbi/ # Dashboard files<br>                                                                                                                                                                                   │ └── crime_dashboard.pbix # Main Power BI report<br>                                                                                                                                                                ├── docs/ # Documentation<br>                                                                                                                                                                                        │  ── screenshots/ # Dashboard previews<br>                                                                                                                                                                          ├── .gitignore # Excluded files<br>                                                                                                                                                                                  └── LICENSE # MIT License<br>

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

bash<br>
cd data_processing<br>
pip install -r requirements.txt  # Install Python dependencies<br>
python crime_etl.py<br>

#Power BI:

Open powerbi/crime_dashboard.pbix

Set data source credentials in:

text
Home → Transform data → Data source settings<br>
🔍 Key Features
Feature	Description	Example Use Case<br>
Crime Hotspots	Leaflet map with precise coordinates	Identify high-crime neighborhoods<br>
Time Trends	Quarterly/hourly crime patterns	Optimize police patrol schedules<br>
Crime Rankings	Top 10 crime types by frequency	Allocate resources to top risks<br>
📊 Data Flow<br>
Diagram<br>
Code<br>





🚀 Usage
Apply Filters:

Use the Year slider to focus on specific periods

Click crime types in the legend to isolate patterns

Export Data:<br>

powerquery<br>
// Power BI: File → Export → CSV/PDF<br>
🤝 Contributing
Fork the repository

Create a feature branch:<br>

bash<br>
git checkout -b feature/heatmap-enhancements<br>
Submit a Pull Request with:<br>

Tested changes<br>

Updated documentation<br>

📜 License
MIT License - See LICENSE for details.

📬 Contact
Vedula Kamesh Babu - vkv333kamesh@gmail.com

Project Link: github.com/Vedula-Kamesh/crime-analysis-dashboard
