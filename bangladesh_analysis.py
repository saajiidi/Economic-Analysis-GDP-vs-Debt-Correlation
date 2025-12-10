import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_bangladesh_data():
    """Generate Bangladesh specific historical trend visualizations."""
    sns.set_theme(style="whitegrid")
    
    # Explicitly use Agg backend
    plt.switch_backend('Agg')
    
    years = [2020, 2021, 2022, 2023, 2024, 2025]
    
    # Data compiled from research (Macrotrends, World Bank, IMF, FocusEconomics)
    data = {
        'Year': years,
        'GDP (USD Billion)': [374, 416, 460, 437, 450, 475],
        'Inflation Rate (%)': [5.6, 5.6, 7.7, 9.0, 10.3, 8.5],
        'Debt-to-GDP (%)': [34.5, 35.6, 37.9, 39.7, 41.0, 40.3],
        'Forex Reserves (USD Billion)': [43.2, 46.2, 33.7, 21.9, 21.4, 26.7]
    }
    
    df_bd = pd.DataFrame(data)
    
    print("Generating Bangladesh GDP Trend...")
    # 1. GDP Trend Line Plot
    plt.figure(figsize=(8, 5)) # Even smaller
    sns.lineplot(data=df_bd, x='Year', y='GDP (USD Billion)', marker='o', linewidth=3, color='#006a4e') # BD Green
    plt.fill_between(df_bd['Year'], df_bd['GDP (USD Billion)'], alpha=0.1, color='#006a4e')
    
    plt.title('Bangladesh GDP Growth (2020-2025)', fontsize=12)
    plt.xlabel('Year', fontsize=10)
    plt.ylabel('GDP (USD Billion)', fontsize=10)
    
    for i, txt in enumerate(df_bd['GDP (USD Billion)']):
        plt.text(df_bd['Year'][i], txt+5, f'${txt}B', ha='center', fontsize=8)
        
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('bd_gdp_trend.png', dpi=100)
    plt.close('all')
    
    print("Generating Bangladesh Inflation/Reserves Plot...")
    # 2. Inflation vs Reserves (Dual Axis)
    fig, ax1 = plt.subplots(figsize=(8, 5))
    
    color = '#f44336' # Red for Inflation
    ax1.set_xlabel('Year', fontsize=10)
    ax1.set_ylabel('Inflation Rate (%)', color=color, fontsize=10)
    ax1.plot(df_bd['Year'], df_bd['Inflation Rate (%)'], color=color, marker='s', linewidth=2, label='Inflation')
    ax1.tick_params(axis='y', labelcolor=color)
    
    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
    color = '#2196f3' # Blue for Reserves
    ax2.set_ylabel('Forex Reserves (USD Billion)', color=color, fontsize=10)
    ax2.plot(df_bd['Year'], df_bd['Forex Reserves (USD Billion)'], color=color, marker='o', linewidth=2, linestyle='--', label='Reserves')
    ax2.tick_params(axis='y', labelcolor=color)
    
    plt.title('Inflation vs Reserves', fontsize=12)
    fig.tight_layout()
    plt.savefig('bd_inflation_reserves.png', dpi=100)
    plt.close('all')
    
    print("Generating Bangladesh Debt Plot...")
    # 3. Debt Trend
    plt.figure(figsize=(8, 5))
    sns.barplot(data=df_bd, x='Year', y='Debt-to-GDP (%)', palette='Reds')
    
    plt.title('Public Debt Evolution', fontsize=12)
    plt.ylim(0, 50) 
    
    for i, v in enumerate(df_bd['Debt-to-GDP (%)']):
        plt.text(i, v + 0.5, f'{v}%', ha='center', fontsize=8)
        
    plt.tight_layout()
    plt.savefig('bd_debt_trend.png', dpi=100)
    plt.close('all')
    print("Done.")

if __name__ == "__main__":
    analyze_bangladesh_data()
