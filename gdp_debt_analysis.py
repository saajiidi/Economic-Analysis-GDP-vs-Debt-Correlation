import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import os

def check_output_dir():
    """Ensure the interactive_plots directory exists."""
    if not os.path.exists('interactive_plots'):
        os.makedirs('interactive_plots')

def create_visualizations(df):
    """Create various interactive visualizations from the dataframe."""
    check_output_dir()
    
    # 1. GDP Bar Plot
    fig_gdp = px.bar(
        df.sort_values('GDP (USD) Billion', ascending=False),
        x='Country', 
        y='GDP (USD) Billion',
        title='GDP by Country (USD Billion)',
        text='GDP (USD) Billion',
        color='GDP (USD) Billion',
        color_continuous_scale='Viridis'
    )
    fig_gdp.update_layout(template='plotly_white')
    fig_gdp.write_html("interactive_plots/gdp_by_country.html")

    # 2. Debt-to-GDP Ratio
    df_sorted = df.sort_values('Debt-to-GDP Ratio (%)', ascending=False)
    fig_ratio = px.bar(
        df_sorted,
        x='Country',
        y='Debt-to-GDP Ratio (%)',
        title='Debt-to-GDP Ratio by Country',
        color='Debt-to-GDP Ratio (%)',
        color_continuous_scale='RdYlGn_r', # Red high, Green low
        text='Debt-to-GDP Ratio (%)'
    )
    # Add threshold line
    fig_ratio.add_hline(y=60, line_dash="dash", line_color="red", annotation_text="60% Warning Threshold")
    fig_ratio.update_layout(template='plotly_white')
    fig_ratio.write_html("interactive_plots/debt_to_gdp_ratio.html")

    # 3. Scatter Plot: GDP vs Total Debt
    # 3. Scatter Plot: GDP vs Total Debt
    fig_scatter = px.scatter(
        df,
        x='GDP (USD) Billion',
        y='Total Debt (USD) Billion',
        size='Debt-to-GDP Ratio (%)',
        color='Country',
        hover_name='Country',
        text='Country',
        size_max=40,  # Reduced max size to prevent heavy overlapping
        opacity=0.7,   # Added opacity to see overlapping points
        log_x=True,    # Log scale to spread out clustered economies
        log_y=True,
        title='GDP vs Total Debt (Bubble size = Debt Ratio)'
    )
    fig_scatter.update_traces(textposition='top center')
    fig_scatter.update_layout(template='plotly_white')
    fig_scatter.write_html("interactive_plots/gdp_vs_debt_scatter.html")

    # 4. Correlation Heatmap
    numeric_df = df.select_dtypes(include=[np.number])
    correlation = numeric_df.corr()
    
    fig_corr = px.imshow(
        correlation,
        text_auto=True,
        aspect="auto",
        color_continuous_scale='RdBu_r',
        title='Correlation Heatmap'
    )
    fig_corr.write_html("interactive_plots/correlation_heatmap.html")

    # 5. Debt Categories Pie Chart
    debt_counts = df['Debt Category'].value_counts()
    fig_pie = px.pie(
        names=debt_counts.index,
        values=debt_counts.values,
        title='Distribution of Debt Categories',
        hole=0.3
    )
    fig_pie.write_html("interactive_plots/debt_categories_pie.html")
    
    # 7. Horizontal Bar Plot (Overview)
    df_sorted_asc = df.sort_values('Debt-to-GDP Ratio (%)', ascending=True)
    fig_horiz = px.bar(
        df_sorted_asc,
        y='Country',
        x='Debt-to-GDP Ratio (%)',
        orientation='h',
        title='Debt-to-GDP Ratio Overview',
        text='Debt-to-GDP Ratio (%)',
        color='Debt-to-GDP Ratio (%)',
        color_continuous_scale='RdYlGn_r'
    )
    fig_horiz.add_vline(x=60, line_dash="dash", line_color="orange", annotation_text="Warning")
    fig_horiz.add_vline(x=90, line_dash="dash", line_color="red", annotation_text="Danger")
    fig_horiz.update_layout(template='plotly_white')
    fig_horiz.write_html("interactive_plots/debt_ratio_horizontal.html")

    # Extra: Data Distribution (Box Plots)
    fig_box = make_subplots(rows=1, cols=2, subplot_titles=("GDP Distribution", "Debt Ratio Distribution"))
    
    fig_box.add_trace(go.Box(y=df['GDP (USD) Billion'], name="GDP ($B)"), row=1, col=1)
    fig_box.add_trace(go.Box(y=df['Debt-to-GDP Ratio (%)'], name="Debt Ratio (%)"), row=1, col=2)
    
    fig_box.update_layout(title_text="Data Distributions", template='plotly_white')
    fig_box.write_html("interactive_plots/gdp_debt_boxplot.html")

def create_oic_visualizations(df):
    """Generate OIC specific interactive visualizations."""
    check_output_dir()
    
    # 1. OIC GDP Bar
    fig_oic_gdp = px.bar(
        df.sort_values('GDP (USD) Billion', ascending=True),
        x='GDP (USD) Billion',
        y='Country',
        orientation='h',
        title='Top OIC Economies by GDP (2024 Estimates)',
        text='GDP (USD) Billion',
        color='GDP (USD) Billion',
        color_continuous_scale='Viridis'
    )
    fig_oic_gdp.update_layout(template='plotly_white')
    fig_oic_gdp.write_html("interactive_plots/oic_gdp_bar.html")
    
    # 2. OIC Debt Ratio
    df_sorted = df.sort_values('Debt-to-GDP Ratio (%)', ascending=True)
    
    # Custom colors mapping
    colors = []
    for val in df_sorted['Debt-to-GDP Ratio (%)']:
        if val < 30: colors.append('green')
        elif val < 60: colors.append('orange')
        else: colors.append('red')
        
    fig_oic_debt = go.Figure(go.Bar(
        x=df_sorted['Debt-to-GDP Ratio (%)'],
        y=df_sorted['Country'],
        orientation='h',
        marker_color=colors,
        text=[f"{val}%" for val in df_sorted['Debt-to-GDP Ratio (%)']],
        textposition='auto'
    ))
    
    fig_oic_debt.update_layout(
        title='OIC Members Debt-to-GDP Ratio (2024)',
        xaxis_title='Debt Ratio (%)',
        template='plotly_white'
    )
    fig_oic_debt.write_html("interactive_plots/oic_debt_ratio.html")
    
    # 3. OIC Scatter
    fig_oic_scatter = px.scatter(
        df,
        x='GDP (USD) Billion',
        y='Debt-to-GDP Ratio (%)',
        color='Country',
        size='GDP (USD) Billion',
        text='Country',
        size_max=40,   # Reduced size
        opacity=0.8,
        title='OIC: Size vs Debt Risk'
    )
    fig_oic_scatter.update_traces(textposition='top center')
    fig_oic_scatter.update_layout(template='plotly_white')
    fig_oic_scatter.write_html("interactive_plots/oic_scatter.html")

def analyze_global_inflation():
    """Analyze and visualize Global/US Dollar Inflation interactively."""
    check_output_dir()
    
    years = list(range(1970, 2025))
    inflation_rates = [
        # 1970-1979
        5.8, 4.3, 3.3, 6.2, 11.1, 9.1, 5.8, 6.5, 7.6, 11.3,
        # 1980-1989
        13.5, 10.3, 6.1, 3.2, 4.3, 3.6, 1.9, 3.6, 4.1, 4.8,
        # 1990-1999
        5.4, 4.2, 3.0, 3.0, 2.6, 2.8, 3.0, 2.3, 1.6, 2.2,
        # 2000-2009
        3.4, 2.8, 1.6, 2.3, 2.7, 3.4, 3.2, 2.8, 3.8, -0.4,
        # 2010-2019
        1.6, 3.2, 2.1, 1.5, 1.6, 0.1, 1.3, 2.1, 2.4, 1.8,
        # 2020-2024
        1.2, 4.7, 8.0, 4.1, 2.9
    ]
    
    data = {'Year': years, 'Inflation Rate (%)': inflation_rates}
    df = pd.DataFrame(data)
    
    # Calculate Purchasing Power
    purchasing_power = []
    val = 100.0
    for rate in df['Inflation Rate (%)']:
        val = val / (1 + rate/100)
        purchasing_power.append(val)
    df['Purchasing Power ($)'] = purchasing_power
    
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    fig.add_trace(
        go.Bar(name="Inflation %", x=df['Year'], y=df['Inflation Rate (%)'], marker_color='#e74c3c', opacity=0.4),
        secondary_y=False,
    )
    
    fig.add_trace(
        go.Scatter(name="Purchasing Power ($)", x=df['Year'], y=df['Purchasing Power ($)'], marker_color='#2c3e50', line=dict(width=3)),
        secondary_y=True,
    )
    
    fig.update_layout(
        title_text="US Dollar Value Erosion (1970-2024)",
        template='plotly_white',
        hovermode='x unified'
    )
    
    fig.update_yaxes(title_text="Inflation Rate (%)", secondary_y=False)
    fig.update_yaxes(title_text="Purchasing Power of $100 ", secondary_y=True)
    
    fig.write_html("interactive_plots/global_inflation_trends.html")

def create_dataframe():
    """Create the dataframe for analysis."""
    data = {
        'Country': [
            'United States', 'China', 'OIC (57 members)', 'Japan', 'Germany', 
            'India', 'United Kingdom', 'France', 'Italy', 'Brazil', 'Canada'
        ],
        'GDP (USD) Billion': [
            28780, 19400, 9200, 4200, 4590, 
            4125, 3590, 3130, 2330, 2260, 2280
        ],
        'Total Debt (USD) Billion': [
            35000, 14000, 3500, 11500, 2900, 
            3300, 3400, 3400, 3200, 1700, 2400
        ],
        'Debt-to-GDP Ratio (%)': [
            123.0, 72.0, 38.0, 260.0, 63.0, 
            80.0, 95.0, 110.0, 137.0, 75.0, 105.0
        ],
        'Debt Category': [
            'High (>90%)', 'High (60-90%)', 'Moderate (30-60%)', 'Critical (>200%)', 'High (60-90%)', 
            'High (60-90%)', 'High (>90%)', 'High (>90%)', 'High (>90%)', 'High (60-90%)', 'High (>90%)'
        ]
    }
    return pd.DataFrame(data)

def create_oic_dataframe():
    """Create a dataframe specifically for OIC member countries analysis."""
    data = {
        'Country': [
            'Indonesia', 'Saudi Arabia', 'Turkey', 'Iran', 'UAE', 
            'Malaysia', 'Egypt', 'Bangladesh', 'Pakistan', 'Nigeria', 
            'Kazakhstan', 'Qatar'
        ],
        'GDP (USD) Billion': [
            1396, 1240, 1320, 437, 537, 
            422, 389, 450, 373, 188, 
            288, 218
        ],
        'Debt-to-GDP Ratio (%)': [
            38.8, 26.2, 24.7, 36.8, 31.3, 
            70.4, 90.1, 21.8, 72.5, 46.6, 
            23.4, 43.0
        ]
    }
    df = pd.DataFrame(data)
    df['Total Debt (USD) Billion'] = df['GDP (USD) Billion'] * (df['Debt-to-GDP Ratio (%)'] / 100)
    return df

def main():
    """Main function to analyze the GDP and debt data."""
    try:
        print("Analyzing Global GDP and Debt Data...")
        df = create_dataframe()
        create_visualizations(df)
        print("Global interactive visualizations created.")

        print("Analyzing OIC Specific Data...")
        oic_df = create_oic_dataframe()
        create_oic_visualizations(oic_df)
        print("OIC interactive visualizations created.")

        print("Analyzing Global Inflation Data...")
        analyze_global_inflation()
        print("Global inflation visualization created.")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
