import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from google.oauth2 import service_account
from googleapiclient.discovery import build
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Google Sheets API setup
SHEET_ID = '2PACX-1vRqFZrORVk1bo_gRiaub0FPRxIAk2MV85i1z3aXeGiOJZKEXt0zwkkkVywkizoZ4O2mvmQoaGM4qJLa'
SHEET_NAMES = {
    'twc': '880828924',  # Chart - TWC
    'tmc': '1419332815',  # Chart - TMC
    'world_states': '0',  # Top World's States
    'muslim_countries': '149729867'  # Top Muslim Countries
}



def get_google_sheets_service():
    """Authenticate and return the Google Sheets API service."""
    creds = None
    # The file token.json stores the user's access and refresh tokens
    if os.path.exists('token.json'):
        creds = service_account.Credentials.from_service_account_file(
            'token.json', 
            scopes=['https://www.googleapis.com/auth/spreadsheets.readonly']
        )
    
    if not creds:
        raise Exception('Failed to obtain credentials')
    
    return build('sheets', 'v4', credentials=creds)

def get_sheet_data(service, sheet_id, range_name):
    """Get data from a specific sheet and range."""
    try:
        sheet = service.spreadsheets()
        result = sheet.values().get(
            spreadsheetId=SHEET_ID,
            range=f"{sheet_id}!{range_name}"
        ).execute()
        return result.get('values', [])
    except Exception as e:
        print(f"Error getting data: {e}")
        return None

def process_sheet_data(data):
    """Convert sheet data to a pandas DataFrame."""
    if not data:
        return None
    
    # Use first row as header
    headers = data[0]
    rows = data[1:]
    
    # Create DataFrame
    df = pd.DataFrame(rows, columns=headers)
    return df

def analyze_data(df, sheet_name):
    """Perform basic analysis on the data."""
    print(f"\nAnalysis for {sheet_name}:")
    print("-" * 50)
    
    # Basic info
    print("\nData Overview:")
    print(df.head())
    
    # Basic statistics
    print("\nBasic Statistics:")
    print(df.describe())
    
    # Check for missing values
    print("\nMissing Values:")
    print(df.isnull().sum())

def main():
    """Main function to fetch and analyze data from the public Google Sheet."""
    try:
        # Public Google Sheet URL
        sheet_url = "https://docs.google.com/spreadsheets/d/1RqFZrORVk1bo_gRiaub0FPRxIAk2MV85i1z3aXeGiOJZKEXt0zwkkkVywkizoZ4O2mvmQoaGM4qJLa/edit#gid=880828924"
        
        # Read the main sheet
        print("Fetching data from Google Sheet...")
        df = read_public_sheet(sheet_url)
        
        if df is not None and not df.empty:
            print("\nFirst few rows of the data:")
            print(df.head())
            
            # Basic analysis
            analyze_data(df, "GDP_Debt_Analysis")
            
            # Save to CSV for further analysis
            output_file = "gdp_debt_data.csv"
            df.to_csv(output_file, index=False)
            print(f"\nData saved to {output_file}")
        else:
            print("No data was retrieved from the Google Sheet. Please make sure the sheet is published to the web.")
            print("To publish: File > Share > Publish to web > Select format (CSV) > Publish")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        print("\nTroubleshooting tips:")
        print("1. Make sure the Google Sheet is published to the web")
        print("2. Check that the sheet URL is correct")
        print("3. Verify you have an active internet connection")
        print("4. Try using a different method to access the data")

if __name__ == "__main__":
    main()
