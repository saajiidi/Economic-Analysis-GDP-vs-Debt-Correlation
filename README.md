# GDP vs Debt Analysis (2025)

This project fetches and analyzes GDP and debt data from a Google Sheets document containing multiple datasets.

## Setup

1. **Install Python** (3.7 or higher) if you haven't already.

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Google Cloud Project and Enable Google Sheets API**:
   - Go to the [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project
   - Enable the Google Sheets API
   - Create credentials (OAuth 2.0 Client ID) and download the JSON file
   - Rename the downloaded file to `token.json` and place it in the project root

4. **Share the Google Sheet**:
   - Open the [Google Sheet](https://docs.google.com/spreadsheets/d/2PACX-1vRqFZrORVk1bo_gRiaub0FPRxIAk2MV85i1z3aXeGiOJZKEXt0zwkkkVywkizoZ4O2mvmQoaGM4qJLa/)
   - Click on "Share" and grant "Viewer" access to the service account email from your Google Cloud Project

## Running the Analysis

```bash
python gdp_debt_analysis.py
```

The script will:
1. Connect to the Google Sheet
2. Fetch data from all available sheets
3. Perform basic analysis
4. Save each sheet's data as a CSV file

## Project Structure

- `gdp_debt_analysis.py`: Main script for fetching and analyzing data
- `requirements.txt`: Python dependencies
- `*.csv`: Output files containing the fetched data
- `token.json`: Google Cloud credentials (not included in version control)

## Data Sources

The data is sourced from the following Google Sheets document:
[GDP vs Debt - 2025](https://docs.google.com/spreadsheets/d/2PACX-1vRqFZrORVk1bo_gRiaub0FPRxIAk2MV85i1z3aXeGiOJZKEXt0zwkkkVywkizoZ4O2mvmQoaGM4qJLa/)
