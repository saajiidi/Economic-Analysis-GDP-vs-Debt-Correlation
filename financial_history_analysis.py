import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os

def check_output_dir():
    """Ensure the interactive_plots directory exists."""
    if not os.path.exists('interactive_plots'):
        os.makedirs('interactive_plots')

def analyze_financial_history():
    """Generate interactive visualizations for Financial History Dashboard."""
    check_output_dir()
    
    print("Generating M2 Money Supply Plot...")
    
    # 1. US M2 Money Supply (Billions USD)
    # Extrapolated data back to 1914 for context
    m2_years = [1914, 1929, 1939, 1945, 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020, 2025]
    m2_values = [15, 26, 46, 110, 150, 290, 627, 1600, 3284, 4942, 8779, 19392, 22298]
    
    df_m2 = pd.DataFrame({'Year': m2_years, 'M2 (Billions)': m2_values})
    
    fig_m2 = go.Figure()
    fig_m2.add_trace(go.Scatter(
        x=df_m2['Year'], 
        y=df_m2['M2 (Billions)'],
        mode='lines+markers',
        name='M2 Money Supply',
        line=dict(color='#2ecc71', width=4),
        fill='tozeroy',
        fillcolor='rgba(46, 204, 113, 0.2)'
    ))
    
    # Add annotations for key events with better spacing
    fig_m2.add_annotation(x=1914, y=20, text="Fed Created<br>(1913)", showarrow=True, arrowhead=1, ay=-40)
    fig_m2.add_annotation(x=1929, y=26, text="Great Depression", showarrow=True, arrowhead=1, ay=-60)
    fig_m2.add_annotation(x=1944, y=100, text="Bretton Woods<br>(1944)", showarrow=True, arrowhead=1, ay=-80)
    fig_m2.add_annotation(x=1971, y=650, text="Nixon Shock<br>(1971)", showarrow=True, arrowhead=1, ay=-60, ax=40)
    fig_m2.add_annotation(x=2008, y=8000, text="2008 Crisis<br>(QE Begins)", showarrow=True, arrowhead=1, ay=-50, ax=-50)
    fig_m2.add_annotation(x=2021, y=21000, text="Pandemic<br>Stimulus", showarrow=True, arrowhead=1, ay=40, ax=-80)
    
    fig_m2.update_layout(
        title='US Money Supply Explosion (1914-2025)',
        xaxis_title='Year',
        yaxis_title='M2 ($B)',
        template='plotly_dark',
        paper_bgcolor='#1e1e1e',
        plot_bgcolor='#1e1e1e',
        autosize=True,
        margin=dict(l=10, r=10, t=30, b=10),
        hovermode='x unified',
        title_font_size=14,
        font=dict(size=10)
    )
    fig_m2.write_html("interactive_plots/us_m2_supply.html")
    
    print("Generating Oil vs Gold Plot...")
    
    # 2. Crude Oil vs Gold (The Petrodollar Story)
    # Data Sources: Macrotrends, EIA
    years = [1970, 1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2023, 2025]
    oil_prices = [3.86, 7.67, 36.8, 27.5, 24.5, 18.4, 30.3, 56.6, 79.6, 48.7, 39.7, 77.7, 76.0]
    gold_prices = [36, 160, 615, 317, 383, 384, 279, 444, 1224, 1160, 1769, 1940, 3380]
    
    df_compare = pd.DataFrame({
        'Year': years, 
        'Oil (USD/bbl)': oil_prices,
        'Gold (USD/oz)': gold_prices
    })
    
    fig_compare = make_subplots(specs=[[{"secondary_y": True}]])
    
    fig_compare.add_trace(
        go.Scatter(
            x=df_compare['Year'], y=df_compare['Oil (USD/bbl)'],
            name="Crude Oil ($)",
            mode='lines',
            line=dict(color='#bdc3c7', width=3) # Light Grey for Oil in Dark Mode
        ),
        secondary_y=False
    )
    
    fig_compare.add_trace(
        go.Scatter(
            x=df_compare['Year'], y=df_compare['Gold (USD/oz)'],
            name="Gold Price ($)",
            mode='lines',
            line=dict(color='#f1c40f', width=3, dash='dot') # Gold color
        ),
        secondary_y=True
    )
    
    fig_compare.update_layout(
        title='Black Gold vs Real Gold (1970-2025)',
        template='plotly_dark',
        paper_bgcolor='#1e1e1e',
        plot_bgcolor='#1e1e1e',
        autosize=True,
        margin=dict(l=10, r=10, t=30, b=10),
        hovermode='x unified',
        legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5),
        title_font_size=14,
        font=dict(size=10)
    )
    
    fig_compare.update_yaxes(title_text="Oil ($/bbl)", color='#bdc3c7', secondary_y=False)
    fig_compare.update_yaxes(title_text="Gold ($/oz)", color='#f39c12', secondary_y=True)
    
    fig_compare.write_html("interactive_plots/oil_vs_gold.html")
    
    print("Generating Purchasing Power Plot...")
    
    # 3. Purchasing Power of $1 (1913-2025)
    # Inverse of CPI. Base 1913 = $1.00 (Fed Created)
    pp_years = [1913, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020, 2025]
    # Calculated using CPI Inflation Calculator
    purchasing_power = [1.00, 0.50, 0.60, 0.70, 0.42, 0.35, 0.26, 0.12, 0.08, 0.06, 0.04, 0.035, 0.03]
    
    fig_pp = go.Figure()
    fig_pp.add_trace(go.Scatter(
        x=pp_years, 
        y=purchasing_power,
        mode='lines+markers',
        name='Purchasing Power',
        line=dict(color='#e74c3c', width=4),
        fill='tozeroy',
        fillcolor='rgba(231, 76, 60, 0.2)'
    ))
    
    fig_pp.add_annotation(x=1913, y=1.0, text="Fed Reserve<br>(1913)", showarrow=True, arrowhead=1, ay=-40)
    fig_pp.add_annotation(x=1971, y=0.26, text="Gold End<br>(1971)", showarrow=True, arrowhead=1, ay=-40, ax=40)
    
    fig_pp.update_layout(
        title='Purchasing Power of $1 (1913 Base)',
        xaxis_title='Year',
        yaxis_title='Value ($)',
        template='plotly_dark',
        paper_bgcolor='#1e1e1e',
        plot_bgcolor='#1e1e1e',
        autosize=True,
        margin=dict(l=10, r=10, t=30, b=10),
        yaxis_tickformat='$.2f',
        title_font_size=14,
        font=dict(size=10)
    )
    fig_pp.write_html("interactive_plots/purchasing_power.html")
    
    print("Done generating financial history plots.")

if __name__ == "__main__":
    analyze_financial_history()
