CREATE DATABASE CrimeAnalysisDB;
GO
USE CrimeAnalysisDB;
GO
CREATE TABLE Dim_Date (
    DateKey CHAR(8) PRIMARY KEY,      -- Format: YYYYMMDD
    Year INT,
    Month INT,
    Day INT,
    Weekday NVARCHAR(20)
);
CREATE TABLE Dim_Time (
    TimeKey CHAR(4) PRIMARY KEY,      -- Format: HHMM
    Hour INT,
    AM_PM VARCHAR(2)
);
CREATE TABLE Dim_Location (
    LocationKey INT PRIMARY KEY,
    AreaID INT,
    AreaName NVARCHAR(100),
    Latitude FLOAT,
    Longitude FLOAT
);
CREATE TABLE Dim_CrimeType (
    CrimeTypeKey INT PRIMARY KEY,
    CrimeCode INT,
    CrimeDescription NVARCHAR(255)
);
CREATE TABLE Fact_Crime (
    CrimeID BIGINT PRIMARY KEY,       -- From DR_NO
    DateKey CHAR(8) FOREIGN KEY REFERENCES Dim_Date(DateKey),
    TimeKey CHAR(4) FOREIGN KEY REFERENCES Dim_Time(TimeKey),
    LocationKey INT FOREIGN KEY REFERENCES Dim_Location(LocationKey),
    CrimeTypeKey INT FOREIGN KEY REFERENCES Dim_CrimeType(CrimeTypeKey)
);


