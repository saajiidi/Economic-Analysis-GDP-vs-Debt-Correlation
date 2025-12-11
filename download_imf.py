import requests
import json
import os

def download_data():
    try:
        print("Downloading IMF Debt Data...")
        url = "https://www.imf.org/external/datamapper/api/v1/GGXWDG_NGDP"
        # Use a user agent to avoid 403/405 if possible, though API should be open
        headers = {'User-Agent': 'Mozilla/5.0'}
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        with open("imf_debt_data.json", "w", encoding='utf-8') as f:
            f.write(r.text)
        print("Debt data saved.")

        print("Downloading IMF Country Metadata...")
        url_countries = "https://www.imf.org/external/datamapper/api/v1/countries"
        r = requests.get(url_countries, headers=headers)
        r.raise_for_status()
        with open("imf_countries.json", "w", encoding='utf-8') as f:
            f.write(r.text)
        print("Country data saved.")
        
    except Exception as e:
        print(f"Error downloading: {e}")

if __name__ == "__main__":
    download_data()
