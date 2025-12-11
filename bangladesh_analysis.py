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
        title='Bangladesh GDP (2020-2025)',
        xaxis_title='Year',
        yaxis_title='GDP ($B)',
        template='plotly_white',
        hovermode='x unified',
        autosize=True,
        margin=dict(l=10, r=10, t=30, b=10),
        title_font_size=14,
        font=dict(size=10)
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
            name="Inflation",
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
            name="Reserves",
            mode='lines+markers',
            marker=dict(symbol='circle', size=8),
            line=dict(color='#2196f3', width=3, dash='dash')
        ),
        secondary_y=True
    )
    
    fig_dual.update_layout(
        title='Inflation vs Reserves',
        template='plotly_white',
        hovermode='x unified',
        legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5),
        autosize=True,
        margin=dict(l=10, r=10, t=30, b=10),
        title_font_size=14,
        font=dict(size=10)
    )
    
    fig_dual.update_yaxes(title_text="Inflation (%)", color='#f44336', secondary_y=False)
    fig_dual.update_yaxes(title_text="Reserves ($B)", color='#2196f3', secondary_y=True)
    
    fig_dual.write_html("interactive_plots/bd_inflation_reserves.html")
    
    print("Generating Interactive Foreign Reserves Plot...")
    # 3. Dedicated Foreign Reserves Plot
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
        title='Forex Reserves Trend',
        xaxis_title='Year',
        yaxis_title='Reserves ($B)',
        template='plotly_white',
        hovermode='x unified',
        autosize=True,
        margin=dict(l=10, r=10, t=30, b=10),
        title_font_size=14,
        font=dict(size=10)
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
        yaxis_title='Debt (%)',
        template='plotly_white',
        yaxis_range=[0, 50],
        autosize=True,
        margin=dict(l=10, r=10, t=30, b=10),
        title_font_size=14,
        font=dict(size=10)
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
        name='Exch Rate',
        line=dict(color='#e74c3c', width=3),
        fill='tozeroy',
        fillcolor='rgba(231, 76, 60, 0.1)'
    ))
    
    fig_curr.add_annotation(
        x=2022, y=95,
        xref="x", yref="y",
        text="Sharp Devaluation",
        showarrow=True,
        arrowhead=1,
        ax=-40, ay=-40
    )
    
    fig_curr.update_layout(
        title='BDT Devaluation (1972-2025)',
        xaxis_title='Year',
        yaxis_title='BDT/USD',
        template='plotly_white',
        hovermode='x unified',
        autosize=True,
        margin=dict(l=10, r=10, t=30, b=10),
        title_font_size=14,
        font=dict(size=10)
    )
    fig_curr.write_html("interactive_plots/bdt_exchange_rate_trend.html")

    print("Generating Interactive Gold/Silver vs BDT Plot...")
    # 6. Commodities in BDT
    comm_data = {
        'Year': [
            1972, 1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 
            2012, 2014, 2016, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025
        ],
        'Gold_USD': [
            58, 160, 615, 317, 383, 384, 279, 444, 1224, 
            1669, 1266, 1250, 1268, 1392, 1769, 1798, 1800, 1940, 2380, 3380
        ],
        'Silver_USD': [
            1.8, 4.4, 21.0, 6.1, 4.8, 5.2, 4.9, 7.3, 20.2, 
            31.1, 19.0, 17.1, 15.7, 16.2, 20.5, 25.1, 21.8, 23.4, 28.5, 38.2
        ]
    }
    df_comm = pd.DataFrame(comm_data)
    df_merged = pd.merge(df_comm, df_bdt, on='Year')
    
    df_merged['Gold_BDT_per_oz'] = df_merged['Gold_USD'] * df_merged['Exchange Rate (BDT/USD)']
    df_merged['Silver_BDT_per_oz'] = df_merged['Silver_USD'] * df_merged['Exchange Rate (BDT/USD)']
    
    conversion_factor = 2.666
    df_merged['Gold_BDT_per_Bhori'] = df_merged['Gold_BDT_per_oz'] / conversion_factor
    df_merged['Silver_BDT_per_Bhori'] = df_merged['Silver_BDT_per_oz'] / conversion_factor

    fig_bd_comm = make_subplots(specs=[[{"secondary_y": True}]])
    
    fig_bd_comm.add_trace(
        go.Scatter(
            x=df_merged['Year'], y=df_merged['Gold_BDT_per_Bhori'],
            name="Gold",
            mode='lines',
            line=dict(color='#FFD700', width=3),
            fill='tozeroy',
            fillcolor='rgba(255, 215, 0, 0.1)'
        ),
        secondary_y=False
    )
    
    fig_bd_comm.add_trace(
        go.Scatter(
            x=df_merged['Year'], y=df_merged['Silver_BDT_per_Bhori'],
            name="Silver",
            mode='lines',
            line=dict(color='#BDC3C7', width=3)
        ),
        secondary_y=True
    )
    
    fig_bd_comm.update_layout(
        title='Gold & Silver in BDT',
        template='plotly_white',
        hovermode='x unified',
        legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5),
        autosize=True,
        margin=dict(l=10, r=10, t=30, b=10),
        title_font_size=14,
        font=dict(size=10)
    )
    
    fig_bd_comm.update_yaxes(title_text="Gold (BDT)", color='#b7950b', secondary_y=False)
    fig_bd_comm.update_yaxes(title_text="Silver (BDT)", color='#7f8c8d', secondary_y=True)
    
    fig_bd_comm.write_html("interactive_plots/bd_commodities.html")
    
    print("Generating Interactive Remittances Plot...")
    # 7. Remittances Inflow
    remit_data = {
        'Year': [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
        'Remittances (USD Billion)': [15.3, 14.9, 13.5, 15.5, 18.3, 21.7, 24.8, 21.0, 21.6, 23.9]
    }
    df_remit = pd.DataFrame(remit_data)
    
    fig_remit = go.Figure()
    fig_remit.add_trace(go.Bar(
        x=df_remit['Year'],
        y=df_remit['Remittances (USD Billion)'],
        name='Remittances',
        marker_color='#27ae60',
        text=[f'${x}B' for x in df_remit['Remittances (USD Billion)']],
        textposition='auto'
    ))
    
    fig_remit.update_layout(
        title='Remittance Inflows',
        xaxis_title='Year',
        yaxis_title='USD Billion',
        template='plotly_white',
        autosize=True,
        margin=dict(l=10, r=10, t=30, b=10),
        title_font_size=14,
        font=dict(size=10)
    )
    fig_remit.write_html("interactive_plots/bd_remittances.html")

    print("Generating Interactive Trade Balance Plot...")
    # 8. Trade Balance (Exports vs Imports)
    trade_data = {
        'Year': [2019, 2020, 2021, 2022, 2023, 2024],
        'Exports': [40.5, 33.7, 38.8, 52.0, 55.6, 58.0],
        'Imports': [55.4, 50.7, 60.7, 82.5, 75.1, 72.0]
    }
    df_trade = pd.DataFrame(trade_data)
    
    fig_trade = go.Figure()
    fig_trade.add_trace(go.Bar(
        x=df_trade['Year'], y=df_trade['Exports'],
        name='Exports', marker_color='#2980b9'
    ))
    fig_trade.add_trace(go.Bar(
        x=df_trade['Year'], y=df_trade['Imports'],
        name='Imports', marker_color='#c0392b'
    ))
    
    fig_trade.update_layout(
        title='Trade Balance: Exp vs Imp',
        xaxis_title='Year',
        yaxis_title='USD Billion',
        barmode='group',
        template='plotly_white',
        legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5),
        autosize=True,
        margin=dict(l=10, r=10, t=30, b=10),
        title_font_size=14,
        font=dict(size=10)
    )
    fig_trade.write_html("interactive_plots/bd_trade_balance.html")

    print("Done generating interactive Bangladesh plots.")

if __name__ == "__main__":
    analyze_bangladesh_data()
