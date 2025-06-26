import pandas as pd
import pyodbc
from datetime import datetime
import re


def parse_date(date_str):
    for fmt in ['%m/%d/%Y', '%m/%d/%y', '%Y-%m-%d', '%d-%b-%y', '%d/%m/%Y']:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            pass

    if isinstance(date_str, str):
        match = re.search(r'(\d{1,2})[/-](\d{1,2})[/-](\d{2,4})', date_str)
        if match:
            month, day, year = match.groups()
            year = int(year) + 2000 if int(year) < 30 else int(year) + 1900 if int(year) < 100 else int(year)
            return datetime(year, int(month), int(day))

        try:
            return datetime(1899, 12, 30) + pd.Timedelta(days=float(date_str))
        except:
            return pd.NaT
    return pd.NaT


def clean_time(time_str):
    try:
        if len(time_str) == 4 and 0 <= int(time_str[:2]) <= 23 and 0 <= int(time_str[2:]) <= 59:
            return time_str
    except:
        pass
    return '0000'


def main():
    df = pd.read_csv("Crime_Data_from_2020_to_Present.csv", low_memory=False)
    print(f"Loaded {len(df)} rows")

    df['DATE OCC'] = df['DATE OCC'].apply(parse_date)
    if 'Date Rptd' in df.columns:
        df['Date Rptd'] = df['Date Rptd'].apply(parse_date)
        df['DATE OCC'] = df['DATE OCC'].fillna(df['Date Rptd'])

    df = df[df['DATE OCC'].notna()].copy()
    df['DateKey'] = df['DATE OCC'].dt.strftime('%Y%m%d')
    df['TimeKey'] = df['TIME OCC'].astype(str).str.zfill(4).apply(clean_time)

    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost\\CRIME2025;"
        "DATABASE=CrimeAnalysisDB;"
        "Trusted_Connection=yes;"
    )
    cursor = conn.cursor()

    for table in ['Fact_Crime', 'Dim_Date', 'Dim_Time', 'Dim_Location', 'Dim_CrimeType']:
        cursor.execute(f"DELETE FROM {table}")
    conn.commit()

    unique_dates = df[['DateKey']].drop_duplicates()
    for _, row in unique_dates.iterrows():
        date_key = row['DateKey']
        cursor.execute("INSERT INTO Dim_Date VALUES (?,?,?,?,?)",
                       date_key, date_key[:4], date_key[4:6], date_key[6:8],
                       datetime.strptime(date_key, '%Y%m%d').strftime('%A'))

    unique_times = df[['TimeKey']].drop_duplicates()
    for _, row in unique_times.iterrows():
        time_key = row['TimeKey']
        cursor.execute("INSERT INTO Dim_Time VALUES (?,?,?)",
                       time_key, int(time_key[:2]), 'AM' if int(time_key[:2]) < 12 else 'PM')

    locations = df.groupby(['AREA', 'AREA NAME']).agg({'LAT': 'mean', 'LON': 'mean'}).reset_index()
    location_map = {}
    for i, (_, row) in enumerate(locations.iterrows(), 1):
        cursor.execute("INSERT INTO Dim_Location VALUES (?,?,?,?,?)",
                       i, row['AREA'], row['AREA NAME'], row['LAT'], row['LON'])
        location_map[row['AREA']] = i

    crimes = df[['Crm Cd', 'Crm Cd Desc']].drop_duplicates()
    crime_map = {}
    for i, (_, row) in enumerate(crimes.iterrows(), 1):
        cursor.execute("INSERT INTO Dim_CrimeType VALUES (?,?,?)",
                       i, row['Crm Cd'], row['Crm Cd Desc'])
        crime_map[row['Crm Cd']] = i

    conn.commit()

    for i in range(0, len(df), 10000):
        batch = df.iloc[i:i + 10000]
        records = []
        for _, row in batch.iterrows():
            records.append((
                int(row['DR_NO']),
                row['DateKey'],
                row['TimeKey'],
                location_map.get(row['AREA'], 1),
                crime_map.get(row['Crm Cd'], 1)
            ))
        cursor.executemany("INSERT INTO Fact_Crime VALUES (?,?,?,?,?)", records)
        conn.commit()
        print(f"Processed {min(i + 10000, len(df))} rows")

    cursor.close()
    conn.close()
    print(f"Completed. Inserted {len(df)} rows")


if __name__ == "__main__":
    main()