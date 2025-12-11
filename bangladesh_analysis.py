import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os

def check_output_dir():
    """Ensure the interactive_plots directory exists."""
    if not os.path.exists('interactive_plots'):
        os.makedirs('interactive_plots')

def analyze_bangladesh_data():
    """Generate Bangladesh specific interactive visualizations using Plotly."""
    
    check_output_dir()
    
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
    
    print("Generating Interactive Bangladesh GDP Trend...")
    # 1. GDP Trend (Line + Area)
    fig_gdp = go.Figure()
    fig_gdp.add_trace(go.Scatter(
        x=df_bd['Year'], 
        y=df_bd['GDP (USD Billion)'],
        mode='lines+markers+text',
        name='GDP',
        line=dict(color='#006a4e', width=4),
        fill='tozeroy',
        fillcolor='rgba(0, 106, 78, 0.1)',
        text=[f'${x}B' for x in df_bd['GDP (USD Billion)']],
        textposition="top center"
    ))
    
    fig_gdp.update_layout(
        title='Bangladesh GDP Growth Trajectory (2020-2025)',
        xaxis_title='Year',
        yaxis_title='GDP (USD Billion)',
        template='plotly_white',
        hovermode='x unified'
    )
    fig_gdp.write_html("interactive_plots/bd_gdp_trend.html")

    print("Generating Interactive Inflation vs Reserves Plot...")
    # 2. Inflation vs Reserves (Dual Axis)
    fig_dual = make_subplots(specs=[[{"secondary_y": True}]])
    
    # Inflation (Bar or Line)
    fig_dual.add_trace(
        go.Scatter(
            x=df_bd['Year'], 
            y=df_bd['Inflation Rate (%)'],
            name="Inflation Rate",
            mode='lines+markers',
            marker=dict(symbol='square', size=8),
            line=dict(color='#f44336', width=3)
        ),
        secondary_y=False
    )
    
    # Reserves (Line)
    fig_dual.add_trace(
        go.Scatter(
            x=df_bd['Year'], 
            y=df_bd['Forex Reserves (USD Billion)'],
            name="Forex Reserves",
            mode='lines+markers',
            marker=dict(symbol='circle', size=8),
            line=dict(color='#2196f3', width=3, dash='dash')
        ),
        secondary_y=True
    )
    
    fig_dual.update_layout(
        title='Inflation vs Forex Reserves Dynamics',
        template='plotly_white',
        hovermode='x unified',
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    
    fig_dual.update_yaxes(title_text="Inflation Rate (%)", color='#f44336', secondary_y=False)
    fig_dual.update_yaxes(title_text="Forex Reserves ($B)", color='#2196f3', secondary_y=True)
    fig_dual.update_xaxes(title_text="Year")
    
    fig_dual.write_html("interactive_plots/bd_inflation_reserves.html")
    
    print("Generating Interactive Foreign Reserves Plot...")
    # 3. Dedicated Foreign Reserves Plot (New Request)
    fig_reserves = go.Figure()
    fig_reserves.add_trace(go.Scatter(
        x=df_bd['Year'], 
        y=df_bd['Forex Reserves (USD Billion)'],
        mode='lines+markers+text',
        name='Reserves',
        line=dict(color='#2196f3', width=4),
        fill='tozeroy',
        fillcolor='rgba(33, 150, 243, 0.1)',
        text=[f'${x}B' for x in df_bd['Forex Reserves (USD Billion)']],
        textposition="top center"
    ))
    
    fig_reserves.update_layout(
        title='Foreign Exchange Reserves Trend (2020-2025)',
        xaxis_title='Year',
        yaxis_title='Reserves (USD Billion)',
        template='plotly_white',
        hovermode='x unified'
    )
    fig_reserves.write_html("interactive_plots/bd_forex_reserves.html")

    print("Generating Interactive Debt Plot...")
    # 4. Debt Trend (Bar)
    fig_debt = go.Figure()
    fig_debt.add_trace(go.Bar(
        x=df_bd['Year'], 
        y=df_bd['Debt-to-GDP (%)'],
        name='Debt Ratio',
        marker_color='indianred',
        text=[f'{x}%' for x in df_bd['Debt-to-GDP (%)']],
        textposition='auto'
    ))
    
    fig_debt.update_layout(
        title='Public Debt Evolution',
        xaxis_title='Year',
        yaxis_title='Debt-to-GDP (%)',
        template='plotly_white',
        yaxis_range=[0, 50]
    )
    fig_debt.write_html("interactive_plots/bd_debt_trend.html")

    print("Generating Interactive BDT Devaluation Plot...")
    # 5. BDT Devaluation
    bdt_data = {
        'Year': [
            1972, 1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 
            2012, 2014, 2016, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025
        ],
        'Exchange Rate (BDT/USD)': [
            7.7, 12.0, 15.4, 28.0, 32.8, 40.3, 52.1, 64.3, 69.0, 
            82.0, 77.5, 78.5, 83.9, 84.5, 84.8, 85.5, 95.0, 106.0, 117.0, 125.0
        ]
    }
    df_bdt = pd.DataFrame(bdt_data)
    
    fig_curr = go.Figure()
    fig_curr.add_trace(go.Scatter(
        x=df_bdt['Year'], 
        y=df_bdt['Exchange Rate (BDT/USD)'],
        mode='lines',
        name='Exchange Rate',
        line=dict(color='#e74c3c', width=3),
        fill='tozeroy',
        fillcolor='rgba(231, 76, 60, 0.1)'
    ))
    
    # Add annotation for sharp drop
    fig_curr.add_annotation(
        x=2022, y=95,
        xref="x", yref="y",
        text="Sharp Devaluation",
        showarrow=True,
        arrowhead=1,
        ax=-40, ay=-40
    )
    
    fig_curr.update_layout(
        title='Devaluation of Bangladeshi Taka (1972-2025)',
        xaxis_title='Year',
        yaxis_title='BDT per 1 USD',
        template='plotly_white',
        hovermode='x unified'
    )
    fig_curr.write_html("interactive_plots/bdt_exchange_rate_trend.html")
    
    print("Done generating interactive Bangladesh plots.")

if __name__ == "__main__":
    analyze_bangladesh_data()

