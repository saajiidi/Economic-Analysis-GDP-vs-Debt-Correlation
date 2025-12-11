import pandas as pd

# Approx 2023/2024 Estimates (IMF/World Bank Sources)
data = {
    'AFG': 9.0, 'ALB': 60.0, 'DZA': 48.0, 'AGO': 70.0, 'ARG': 85.0, 'ARM': 49.0, 'AUS': 49.0, 'AUT': 78.0, 'AZE': 21.0, 
    'BHS': 85.0, 'BHR': 120.0, 'BGD': 40.0, 'BRB': 115.0, 'BLR': 40.0, 'BEL': 105.0, 'BLZ': 66.0, 'BEN': 53.0, 'BTN': 110.0, 'BOL': 80.0, 'BIH': 28.0, 'BWA': 20.0, 'BRA': 88.0, 'BRN': 2.5, 'BGR': 23.0, 'BFA': 55.0, 'BDI': 60.0, 'CPV': 115.0, 'KHM': 26.0, 'CMR': 42.0, 'CAN': 106.0, 'CAF': 50.0, 'TCD': 40.0, 'CHL': 38.0, 'CHN': 83.0, 'COL': 55.0, 'COM': 30.0, 'COD': 23.0, 'COG': 95.0, 'CRI': 60.0, 'CIV': 58.0, 'HRV': 62.0, 'CUB': 110.0, 'CYP': 75.0, 'CZE': 44.0, 
    'DNK': 30.0, 'DJI': 40.0, 'DMA': 100.0, 'DOM': 59.0, 'ECU': 55.0, 'EGY': 92.0, 'SLV': 80.0, 'GNQ': 35.0, 'ERI': 175.0, 'EST': 20.0, 'ETH': 35.0, 
    'FJI': 85.0, 'FIN': 75.0, 'FRA': 111.0, 
    'GAB': 65.0, 'GMB': 77.0, 'GEO': 40.0, 'DEU': 63.0, 'GHA': 85.0, 'GRC': 159.0, 'GRD': 70.0, 'GTM': 28.0, 'GIN': 40.0, 'GNB': 78.0, 'GUY': 28.0, 
    'HTI': 25.0, 'HND': 47.0, 'HKG': 6.0, 'HUN': 75.0, 
    'ISL': 65.0, 'IND': 82.0, 'IDN': 39.0, 'IRN': 35.0, 'IRQ': 45.0, 'IRL': 43.0, 'ISR': 62.0, 'ITA': 137.0, 
    'JAM': 75.0, 'JPN': 255.0, 'JOR': 90.0, 
    'KAZ': 24.0, 'KEN': 70.0, 'KIR': 15.0, 'KWT': 3.5, 'KGZ': 50.0, 
    'LAO': 120.0, 'LVA': 42.0, 'LBN': 280.0, 'LSO': 60.0, 'LBR': 55.0, 'LBY': 60.0, 'LTU': 37.0, 'LUX': 28.0, 
    'MDG': 45.0, 'MWI': 75.0, 'MYS': 65.0, 'MDV': 115.0, 'MLI': 50.0, 'MLT': 55.0, 'MHL': 20.0, 'MRT': 50.0, 'MUS': 80.0, 'MEX': 52.0, 'FSM': 15.0, 'MDA': 35.0, 'MNG': 60.0, 'MNE': 70.0, 'MAR': 70.0, 'MOZ': 100.0, 'MMR': 60.0, 
    'NAM': 68.0, 'NRU': 25.0, 'NPL': 45.0, 'NLD': 48.0, 'NZL': 45.0, 'NIC': 45.0, 'NER': 50.0, 'NGA': 40.0, 'MKD': 52.0, 'NOR': 40.0, 
    'OMN': 40.0, 
    'PAK': 75.0, 'PLW': 30.0, 'PAN': 55.0, 'PNG': 50.0, 'PRY': 40.0, 'PER': 33.0, 'PHL': 60.0, 'POL': 52.0, 'PRT': 100.0, 
    'QAT': 42.0, 
    'ROU': 50.0, 'RUS': 20.0, 'RWA': 65.0, 
    'WSM': 45.0, 'SMR': 80.0, 'STP': 55.0, 'SAU': 27.0, 'SEN': 75.0, 'SRB': 52.0, 'SYC': 60.0, 'SLE': 90.0, 'SGP': 168.0, 'SVK': 58.0, 'SVN': 70.0, 'SLB': 15.0, 'SOM': 10.0, 'ZAF': 74.0, 'SSD': 40.0, 'ESP': 107.0, 'LKA': 105.0, 'KNA': 55.0, 'LCA': 75.0, 'VCT': 80.0, 'SDN': 250.0, 'SUR': 90.0, 'SWE': 33.0, 'CHE': 38.0, 'SYR': 80.0, 
    'TWN': 25.0, 'TJK': 35.0, 'TZA': 45.0, 'THA': 62.0, 'TLS': 15.0, 'TGO': 60.0, 'TON': 45.0, 'TTO': 55.0, 'TUN': 80.0, 'TUR': 32.0, 'TKM': 8.0, 'TUV': 10.0, 
    'UGA': 50.0, 'UKR': 85.0, 'ARE': 30.0, 'GBR': 104.0, 'USA': 123.0, 'URY': 65.0, 'UZB': 35.0, 
    'VUT': 45.0, 'VEN': 150.0, 'VNM': 37.0, 
    'YEM': 70.0, 
    'ZMB': 110.0, 'ZWE': 95.0
}

# Mapping codes to names
country_names = {
    'AFG': 'Afghanistan', 'ALB': 'Albania', 'DZA': 'Algeria', 'AGO': 'Angola', 'ARG': 'Argentina', 'ARM': 'Armenia', 'AUS': 'Australia', 'AUT': 'Austria', 'AZE': 'Azerbaijan',
    'BHS': 'Bahamas', 'BHR': 'Bahrain', 'BGD': 'Bangladesh', 'BRB': 'Barbados', 'BLR': 'Belarus', 'BEL': 'Belgium', 'BLZ': 'Belize', 'BEN': 'Benin', 'BTN': 'Bhutan', 'BOL': 'Bolivia', 'BIH': 'Bosnia and Herzegovina', 'BWA': 'Botswana', 'BRA': 'Brazil', 'BRN': 'Brunei', 'BGR': 'Bulgaria', 'BFA': 'Burkina Faso', 'BDI': 'Burundi', 'CPV': 'Cabo Verde', 'KHM': 'Cambodia', 'CMR': 'Cameroon', 'CAN': 'Canada', 'CAF': 'Central African Republic', 'TCD': 'Chad', 'CHL': 'Chile', 'CHN': 'China', 'COL': 'Colombia', 'COM': 'Comoros', 'COD': 'Congo, Dem. Rep.', 'COG': 'Congo, Rep.', 'CRI': 'Costa Rica', 'CIV': 'Cote d\'Ivoire', 'HRV': 'Croatia', 'CUB': 'Cuba', 'CYP': 'Cyprus', 'CZE': 'Czech Republic',
    'DNK': 'Denmark', 'DJI': 'Djibouti', 'DMA': 'Dominica', 'DOM': 'Dominican Republic', 'ECU': 'Ecuador', 'EGY': 'Egypt', 'SLV': 'El Salvador', 'GNQ': 'Equatorial Guinea', 'ERI': 'Eritrea', 'EST': 'Estonia', 'ETH': 'Ethiopia',
    'FJI': 'Fiji', 'FIN': 'Finland', 'FRA': 'France',
    'GAB': 'Gabon', 'GMB': 'Gambia, The', 'GEO': 'Georgia', 'DEU': 'Germany', 'GHA': 'Ghana', 'GRC': 'Greece', 'GRD': 'Grenada', 'GTM': 'Guatemala', 'GIN': 'Guinea', 'GNB': 'Guinea-Bissau', 'GUY': 'Guyana',
    'HTI': 'Haiti', 'HND': 'Honduras', 'HKG': 'Hong Kong SAR', 'HUN': 'Hungary',
    'ISL': 'Iceland', 'IND': 'India', 'IDN': 'Indonesia', 'IRN': 'Iran', 'IRQ': 'Iraq', 'IRL': 'Ireland', 'ISR': 'Israel', 'ITA': 'Italy',
    'JAM': 'Jamaica', 'JPN': 'Japan', 'JOR': 'Jordan',
    'KAZ': 'Kazakhstan', 'KEN': 'Kenya', 'KIR': 'Kiribati', 'KWT': 'Kuwait', 'KGZ': 'Kyrgyz Republic',
    'LAO': 'Lao PDR', 'LVA': 'Latvia', 'LBN': 'Lebanon', 'LSO': 'Lesotho', 'LBR': 'Liberia', 'LBY': 'Libya', 'LTU': 'Lithuania', 'LUX': 'Luxembourg',
    'MDG': 'Madagascar', 'MWI': 'Malawi', 'MYS': 'Malaysia', 'MDV': 'Maldives', 'MLI': 'Mali', 'MLT': 'Malta', 'MHL': 'Marshall Islands', 'MRT': 'Mauritania', 'MUS': 'Mauritius', 'MEX': 'Mexico', 'FSM': 'Micronesia', 'MDA': 'Moldova', 'MNG': 'Mongolia', 'MNE': 'Montenegro', 'MAR': 'Morocco', 'MOZ': 'Mozambique', 'MMR': 'Myanmar',
    'NAM': 'Namibia', 'NRU': 'Nauru', 'NPL': 'Nepal', 'NLD': 'Netherlands', 'NZL': 'New Zealand', 'NIC': 'Nicaragua', 'NER': 'Niger', 'NGA': 'Nigeria', 'MKD': 'North Macedonia', 'NOR': 'Norway',
    'OMN': 'Oman',
    'PAK': 'Pakistan', 'PLW': 'Palau', 'PAN': 'Panama', 'PNG': 'Papua New Guinea', 'PRY': 'Paraguay', 'PER': 'Peru', 'PHL': 'Philippines', 'POL': 'Poland', 'PRT': 'Portugal',
    'QAT': 'Qatar',
    'ROU': 'Romania', 'RUS': 'Russia', 'RWA': 'Rwanda',
    'WSM': 'Samoa', 'SMR': 'San Marino', 'STP': 'Sao Tome and Principe', 'SAU': 'Saudi Arabia', 'SEN': 'Senegal', 'SRB': 'Serbia', 'SYC': 'Seychelles', 'SLE': 'Sierra Leone', 'SGP': 'Singapore', 'SVK': 'Slovak Republic', 'SVN': 'Slovenia', 'SLB': 'Solomon Islands', 'SOM': 'Somalia', 'ZAF': 'South Africa', 'SSD': 'South Sudan', 'ESP': 'Spain', 'LKA': 'Sri Lanka', 'KNA': 'St. Kitts and Nevis', 'LCA': 'St. Lucia', 'VCT': 'St. Vincent and the Grenadines', 'SDN': 'Sudan', 'SUR': 'Suriname', 'SWE': 'Sweden', 'CHE': 'Switzerland', 'SYR': 'Syria',
    'TWN': 'Taiwan', 'TJK': 'Tajikistan', 'TZA': 'Tanzania', 'THA': 'Thailand', 'TLS': 'Timor-Leste', 'TGO': 'Togo', 'TON': 'Tonga', 'TTO': 'Trinidad and Tobago', 'TUN': 'Tunisia', 'TUR': 'Turkey', 'TKM': 'Turkmenistan', 'TUV': 'Tuvalu',
    'UGA': 'Uganda', 'UKR': 'Ukraine', 'ARE': 'United Arab Emirates', 'GBR': 'United Kingdom', 'USA': 'United States', 'URY': 'Uruguay', 'UZB': 'Uzbekistan',
    'VUT': 'Vanuatu', 'VEN': 'Venezuela', 'VNM': 'Vietnam',
    'YEM': 'Yemen',
    'ZMB': 'Zambia', 'ZWE': 'Zimbabwe'
}

processed_list = []
for code, val in data.items():
    category = "Moderate (30-60%)"
    if val > 200:
        category = "Critical (>200%)"
    elif val > 90:
        category = "High (>90%)"
    elif val > 60:
        category = "High (60-90%)"
    elif val < 30:
        category = "Low (<30%)"
        
    name = country_names.get(code, code)
    processed_list.append({
        'Country Code': code,
        'Country': name,
        'Debt-to-GDP Ratio (%)': val,
        'Debt Category': category
    })

df = pd.DataFrame(processed_list)
df.to_csv("global_debt_data_2024.csv", index=False)
print("Manually generated global_debt_data_2024.csv")
