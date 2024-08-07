# Data-processing
Retail Orders Data Processing

## Introduction
This project demonstrates the use of Python for data processing and database interactions. 

## Features
- Download retail orders dataset from Kaggle.
- Extract the dataset from a zip file.
- Clean and process the data (handle missing values, derive new columns, etc.).
- Convert date columns to appropriate formats.
- Upload the processed data to a SQL Server database.

## Data Processing Steps
- **Download Dataset**: Use the Kaggle API to download the dataset.
- **Extract Dataset**: Unzip the downloaded file.
- **Load Data**: Read the CSV file into a Pandas DataFrame.
- **Handle Missing Values**: Replace 'Not Available' and 'unknown' with NaN.
- **Derive New Columns**: Create new columns such as `profit` by performing calculations.
- **Convert Date Columns**: Convert date columns to datetime objects.
- **Drop Unnecessary Columns**: Remove columns that are not needed.

## Database Upload
The processed data is uploaded to a SQL Server database using SQLAlchemy. Ensure you have SQL Server installed and configured on your machine.

## Dependencies
- pandas
- sqlalchemy
- kaggle
- zipfile 
