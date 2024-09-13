import os
import pandas as pd
from sqlalchemy import create_engine
from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime

# Constants
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
CREDENTIALS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'service_account.json')
SPREADSHEET_ID = 'YOUR_SPREADSHEET_ID'
RANGE_NAME = 'sheet_name!A:N'
DB_CONNECTION_STRING = "mysql+pymysql://username:password@host:port/database_name"

print(f"Path to credentials file: {CREDENTIALS_FILE}")

def get_credentials():
    """
    Obtain Google Sheets API credentials from the service account file.
    """
    try:
        return service_account.Credentials.from_service_account_file(
            CREDENTIALS_FILE, scopes=SCOPES)
    except Exception as e:
        print(f"Error obtaining credentials: {e}")
        raise

def get_spreadsheet_data(service):
    """
    Fetch data from the specified Google Sheet.
    """
    try:
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
        return result.get('values', [])
    except Exception as e:
        print(f"Error fetching spreadsheet data: {e}")
        raise

def process_data(values):
    """
    Process the raw data from the spreadsheet into a pandas DataFrame.
    """
    if not values:
        print("No data found in the spreadsheet.")
        return pd.DataFrame()
    return pd.DataFrame(values[1:], columns=values[0])

def save_to_database(df):
    """
    Save the processed data to the MySQL database.
    """
    try:
        engine = create_engine(DB_CONNECTION_STRING)
        df.to_sql('contract_management', con=engine, if_exists='replace', index=False)
        print(f"Data imported successfully! {datetime.now()}")
    except Exception as e:
        print(f"Error saving to database: {e}")
        raise

def main():
    """
    Main function to orchestrate the data import process.
    """
    try:
        # Obtain credentials and build the service
        creds = get_credentials()
        service = build('sheets', 'v4', credentials=creds)
        
        # Fetch and process data
        values = get_spreadsheet_data(service)
        df = process_data(values)
        
        # Save data if not empty
        if not df.empty:
            save_to_database(df)
        else:
            print("No data to import.")
    except Exception as e:
        print(f"Error in main execution: {e}")

if __name__ == '__main__':
    main()