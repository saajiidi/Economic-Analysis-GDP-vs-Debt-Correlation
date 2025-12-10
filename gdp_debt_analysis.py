import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def create_visualizations(df):
    """Create various visualizations from the dataframe."""
    # Set the style
    # plt.style.use('seaborn')
    sns.set_theme()
    
    # 1. GDP Bar Plot
    plt.figure(figsize=(14, 7))
    df_sorted = df.sort_values('GDP (USD) Billion', ascending=False)
    ax = sns.barplot(x='Country', y='GDP (USD) Billion', data=df_sorted, palette='viridis')
    plt.title('GDP by Country (USD Billion)', fontsize=16)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('gdp_by_country.png', dpi=300, bbox_inches='tight')
    plt.close()

    # 2. Debt-to-GDP Ratio (Sorted)
    plt.figure(figsize=(14, 7))
    df_sorted = df.sort_values('Debt-to-GDP Ratio (%)', ascending=False)
    ax = sns.barplot(x='Country', y='Debt-to-GDP Ratio (%)', data=df_sorted, palette='coolwarm')
    plt.axhline(y=60, color='red', linestyle='--', label='60% Warning Threshold')
    plt.title('Debt-to-GDP Ratio by Country (%)', fontsize=16)
    plt.xticks(rotation=45, ha='right')
    plt.legend()
    plt.tight_layout()
    plt.savefig('debt_to_gdp_ratio.png', dpi=300, bbox_inches='tight')
    plt.close()

    # 3. Scatter Plot: GDP vs Total Debt
    plt.figure(figsize=(10, 8))
    ax = sns.scatterplot(
        x='GDP (USD) Billion', 
        y='Total Debt (USD) Billion',
        size='Debt-to-GDP Ratio (%)',
        sizes=(100, 1000),
        alpha=0.7,
        data=df
    )
    plt.title('GDP vs Total Debt (Bubble size = Debt-to-GDP Ratio)', fontsize=16)
    plt.xlabel('GDP (USD Billion)')
    plt.ylabel('Total Debt (USD Billion)')
    
    # Add country labels
    for i, txt in enumerate(df['Country']):
        ax.annotate(txt, 
                   (df['GDP (USD) Billion'].iloc[i], 
                    df['Total Debt (USD) Billion'].iloc[i]),
                   fontsize=8)
    
    plt.tight_layout()
    plt.savefig('gdp_vs_debt_scatter.png', dpi=300, bbox_inches='tight')
    plt.close()

    # 4. Correlation Heatmap
    plt.figure(figsize=(10, 8))
    numeric_df = df.select_dtypes(include=[np.number])
    correlation = numeric_df.corr()
    sns.heatmap(correlation, 
                annot=True, 
                cmap='coolwarm', 
                center=0,
                fmt=".2f",
                linewidths=0.5)
    plt.title('Correlation Heatmap', fontsize=16)
    plt.tight_layout()
    plt.savefig('correlation_heatmap.png', dpi=300, bbox_inches='tight')
    plt.close()

    # 5. Debt Categories Pie Chart
    plt.figure(figsize=(10, 8))
    debt_counts = df['Debt Category'].value_counts()
    plt.pie(debt_counts, 
            labels=debt_counts.index, 
            autopct='%1.1f%%',
            startangle=90,
            colors=sns.color_palette('pastel')[0:len(debt_counts)],
            explode=[0.05] * len(debt_counts))
    plt.title('Distribution of Debt Categories', fontsize=16)
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig('debt_categories_pie.png', dpi=300, bbox_inches='tight')
    plt.close()

    # 6. Box Plot of GDP and Debt
    plt.figure(figsize=(12, 6))
    gdp_debt = pd.melt(df, 
                      id_vars=['Country'], 
                      value_vars=['GDP (USD) Billion', 'Total Debt (USD) Billion'],
                      var_name='Metric',
                      value_name='Value')
    sns.boxplot(x='Metric', y='Value', data=gdp_debt, palette='Set2')
    plt.title('Distribution of GDP and Total Debt', fontsize=16)
    plt.tight_layout()
    plt.savefig('gdp_debt_boxplot.png', dpi=300, bbox_inches='tight')
    plt.close()

    # 7. Horizontal Bar Plot of Debt-to-GDP Ratio
    plt.figure(figsize=(12, 8))
    df_sorted = df.sort_values('Debt-to-GDP Ratio (%)', ascending=True)
    colors = ['green' if x < 60 else 'orange' if x < 90 else 'red' for x in df_sorted['Debt-to-GDP Ratio (%)']]
    plt.barh(df_sorted['Country'], 
             df_sorted['Debt-to-GDP Ratio (%)'], 
             color=colors,
             alpha=0.7)
    plt.axvline(x=60, color='red', linestyle='--', alpha=0.5)
    plt.axvline(x=90, color='red', linestyle='--', alpha=0.5)
    plt.text(62, len(df_sorted) - 0.5, '60% Warning Level', color='red')
    plt.text(92, len(df_sorted) - 0.5, '90% Danger Level', color='red')
    plt.title('Debt-to-GDP Ratio by Country', fontsize=16)
    plt.xlabel('Debt-to-GDP Ratio (%)')
    plt.tight_layout()
    plt.savefig('debt_ratio_horizontal.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_debt_analysis_plots(df):
    """Create additional debt analysis plots."""
    # Set style
    # plt.style.use('seaborn')
    sns.set_theme()
    
    # 1. Enhanced Debt-to-GDP Ratio Plot
    plt.figure(figsize=(14, 8))
    df_sorted = df.sort_values('Debt-to-GDP Ratio (%)', ascending=True)
    colors = ['#2ecc71' if x < 60 else '#f39c12' if x < 90 else '#e74c3c' 
             for x in df_sorted['Debt-to-GDP Ratio (%)']]
    
    bars = plt.barh(df_sorted['Country'], 
                   df_sorted['Debt-to-GDP Ratio (%)'],
                   color=colors, alpha=0.8)
    
    # Add value labels
    for bar in bars:
        width = bar.get_width()
        plt.text(width + 1, bar.get_y() + bar.get_height()/2,
                f'{width:.1f}%',
                va='center', ha='left', fontsize=9)
    
    plt.axvline(x=60, color='red', linestyle='--', alpha=0.5)
    plt.axvline(x=90, color='red', linestyle='--', alpha=0.5)
    plt.text(62, len(df_sorted) - 0.5, '60% Warning Level', color='red', fontsize=10)
    plt.text(92, len(df_sorted) - 0.5, '90% Danger Level', color='red', fontsize=10)
    
    plt.title('Debt-to-GDP Ratio by Country', fontsize=16, pad=20)
    plt.xlabel('Debt-to-GDP Ratio (%)', fontsize=12)
    plt.tight_layout()
    plt.savefig('debt_ratio_enhanced.png', dpi=300, bbox_inches='tight')
    plt.close()

    # 2. Enhanced Debt Categories Pie Chart
    plt.figure(figsize=(10, 10))
    debt_cats = df['Debt Category'].value_counts().sort_index()
    colors = ['#2ecc71', '#3498db', '#f39c12', '#e74c3c']
    explode = [0.05] * len(debt_cats)
    
    plt.pie(debt_cats, 
            labels=debt_cats.index,
            autopct='%1.1f%%',
            startangle=90,
            colors=colors,
            explode=explode,
            textprops={'fontsize': 12})
    
    plt.title('Distribution of Debt Categories', fontsize=16, pad=20)
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig('debt_categories_enhanced.png', dpi=300, bbox_inches='tight')
    plt.close()

    # 3. Debt-to-GDP Overview (Boxplot + Violin)
    plt.figure(figsize=(14, 6))
    
    plt.subplot(1, 2, 1)
    sns.boxplot(y='Debt-to-GDP Ratio (%)', data=df, color='#3498db')
    plt.title('Debt-to-GDP Distribution', fontsize=14)
    
    plt.subplot(1, 2, 2)
    sns.violinplot(y='Debt-to-GDP Ratio (%)', data=df, color='#e74c3c')
    plt.title('Debt-to-GDP Density', fontsize=14)
    
    plt.tight_layout()
    plt.savefig('debt_distribution_analysis.png', dpi=300, bbox_inches='tight')
    plt.close()

    # 4. Correlation Matrix with Annotations
    plt.figure(figsize=(10, 8))
    numeric_df = df.select_dtypes(include=[np.number])
    correlation = numeric_df.corr()
    
    mask = np.triu(np.ones_like(correlation, dtype=bool))
    cmap = sns.diverging_palette(230, 20, as_cmap=True)
    
    sns.heatmap(correlation, 
                mask=mask, 
                cmap=cmap, 
                vmax=1, 
                vmin=-1,
                center=0,
                square=True,
                linewidths=.5,
                annot=True,
                fmt=".2f",
                cbar_kws={"shrink": .8})
    
    plt.title('Correlation Matrix', fontsize=16, pad=20)
    plt.tight_layout()
    plt.savefig('correlation_matrix_enhanced.png', dpi=300, bbox_inches='tight')
    plt.close()

    # 5. Data Distribution (Histograms)
    plt.figure(figsize=(15, 10))
    
    plt.subplot(2, 2, 1)
    sns.histplot(df['GDP (USD) Billion'], kde=True, color='#3498db')
    plt.title('GDP Distribution', fontsize=14)
    
    plt.subplot(2, 2, 2)
    sns.histplot(df['Total Debt (USD) Billion'], kde=True, color='#e74c3c')
    plt.title('Total Debt Distribution', fontsize=14)
    
    plt.subplot(2, 2, 3)
    sns.histplot(df['Debt-to-GDP Ratio (%)'], kde=True, color='#2ecc71')
    plt.title('Debt-to-GDP Ratio Distribution', fontsize=14)
    
    plt.tight_layout()
    plt.savefig('data_distributions.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_dataframe():
    """Create the dataframe for analysis."""
    try:
        # Try to read from CSV first
        df = pd.read_csv('emerging_markets_debt_analysis.csv')
        print("Data loaded from 'emerging_markets_debt_analysis.csv'")
        return df
    except FileNotFoundError:
        print("CSV file not found. Creating dataframe from hardcoded data.")
        # Fallback to hardcoded data if CSV is missing
        data = {
            'Country': ['Indonesia', 'Turkey', 'Egypt', 'Malaysia', 'Saudi Arabia', 'Pakistan', 'Iran', 'UAE', 'Kazakhstan', 'Qatar', 'Nigeria', 'Bangladesh', 'Iraq', 'Morocco', 'Algeria'],
            'GDP (USD) Billion': [1390, 1150, 477, 447, 1060, 376, 367, 503, 225, 220, 514, 460, 297, 147, 163],
            'Total Debt (USD) Billion': [-600, -500, -400, -300, -250, -250, -200, -150, -150, -150, -100, -100, -100, -80, -50],
            'Debt-to-GDP Ratio (%)': [43.2, 43.5, 83.9, 67.1, 23.6, 66.5, 54.5, 29.8, 66.7, 68.2, 19.5, 21.7, 33.7, 54.4, 30.7],
            'Debt Category': ['Moderate (30-60%)', 'Moderate (30-60%)', 'High (60-90%)', 'High (60-90%)', 'Low (<30%)', 'High (60-90%)', 'Moderate (30-60%)', 'Low (<30%)', 'High (60-90%)', 'High (60-90%)', 'Low (<30%)', 'Low (<30%)', 'Moderate (30-60%)', 'Moderate (30-60%)', 'Moderate (30-60%)']
        }
        df = pd.DataFrame(data)
        return df

def analyze_data(df, title):
    """Perform basic analysis on the data."""
    print(f"\nAnalysis for {title}:")
    print("-" * 50)
    
    # Basic info
    print("\nData Overview:")
    print(df.info())
    
    # Basic statistics
    print("\nBasic Statistics:")
    print(df.describe())
    
    # Check for missing values
    print("\nMissing Values:")
    print(df.isnull().sum())




def main():
    """Main function to analyze the GDP and debt data."""
    try:
        print("Analyzing GDP and Debt Data for Selected Countries...")
        df = create_dataframe()
        
        if df is not None and not df.empty:
            create_debt_analysis_plots(df)

            print("\nFirst few rows of the data:")
            print(df.head())
            
            # Basic analysis
            analyze_data(df, "Emerging Markets GDP and Debt Analysis")
            
            # Create visualizations
            create_visualizations(df)
            
            print("\nVisualizations have been created and saved as PNG files:")
            print("- gdp_by_country.png")
            print("- debt_to_gdp_ratio.png")
            print("- gdp_vs_debt_scatter.png")
            print("- correlation_heatmap.png")
            print("- debt_categories_pie.png")
            print("- gdp_debt_boxplot.png")
            print("- debt_ratio_horizontal.png")
            
            # Save to CSV for further analysis
            output_file = "emerging_markets_debt_analysis.csv"
            df.to_csv(output_file, index=False)
            print(f"\nData saved to {output_file}")
                
        else:
            print("No data was available for analysis.")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        import traceback
        traceback.print_exc()



if __name__ == "__main__":
    main()