import json
import pandas as pd
import time
import os

def process_data():
    # Wait for file
    print("Waiting for data file...")
    timeout = 60
    start = time.time()
    while not os.path.exists("imf_debt_data.json"):
        if time.time() - start > timeout:
            print("Timeout waiting for imf_debt_data.json")
            return
        time.sleep(1)
    
    print("Loading JSON data...")
    with open("imf_debt_data.json", "r", encoding='utf-8') as f:
        data = json.load(f)
        
    countries_map = {}
    if os.path.exists("imf_countries.json"):
        with open("imf_countries.json", "r", encoding='utf-8') as f:
            c_data = json.load(f)
            # Structure might be complex, let's explore or handle gracefully
            if 'countries' in c_data:
                for k, v in c_data['countries'].items():
                    if 'label' in v:
                        countries_map[k] = v['label']
    
    # Extract Debt Data
    # Path: data['values']['GGXWDG_NGDP'] -> {CountryCode: {Year: Value}}
    
    if 'values' not in data or 'GGXWDG_NGDP' not in data['values']:
        print("Invalid Data Format: GGXWDG_NGDP not found")
        return

    debt_data = data['values']['GGXWDG_NGDP']
    
    processed_list = []
    
    for country_code, year_data in debt_data.items():
        # Get latest available data (prioritizing 2024, then 2023, 2022)
        val = None
        year_used = None
        
        for y in ['2024', '2023', '2022', '2021', '2020']:
            if y in year_data:
                val = year_data[y]
                year_used = y
                break
        
        # Check if value is valid (sometimes it's string "no data" or null)
        try:
            val_float = float(val)
        except (TypeError, ValueError):
            continue
            
        country_name = countries_map.get(country_code, country_code)
        
        # Categorize
        category = "Moderate (30-60%)"
        color_hex = "#388e3c" # Green
        
        if val_float > 200:
            category = "Critical (>200%)"
            color_hex = "#8b0000"
        elif val_float > 90:
            category = "High (>90%)"
            color_hex = "#d32f2f"
        elif val_float > 60:
            category = "High (60-90%)"
            color_hex = "#f57c00"
        elif val_float < 30:
            category = "Low (<30%)"
            color_hex = "#2ecc71" # Light Green
            
        # OIC Flag (approximation/manual list or from metadata if available)
        # We leave OIC specific tagging to the other script if needed, 
        # but for the global map we just need the list.
        
        processed_list.append({
            'Country Code': country_code,
            'Country': country_name,
            'Debt-to-GDP Ratio (%)': round(val_float, 2),
            'Year': year_used,
            'Debt Category': category
        })
        
    df = pd.DataFrame(processed_list)
    print(f"Processed {len(df)} countries.")
    
    df.to_csv("global_debt_data_2024.csv", index=False)
    print("Saved to global_debt_data_2024.csv")

if __name__ == "__main__":
    process_data()
