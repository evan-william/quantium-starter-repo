from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

# 1. INITIALIZE APP
app = Dash(__name__)

# 2. LOAD FORMATTED DATA CSV
df = pd.read_csv("./formatted_data.csv")

# FIX: paksa kolom sales jadi angka & date jadi format tanggal biar gak berantakan
df['sales'] = pd.to_numeric(df['sales'], errors='coerce')
df['date'] = pd.to_datetime(df['date'])

df = df.sort_values(by="date") # make sure data sorted by date

# 3. MAKE LINE CHART USING PLOTLY EXPRES
line_chart = px.line(
    df, 
    x="date", 
    y="sales", 
    title="Pink Morsel Sales Trend (Before & After Price Increase)",
    labels={"sales": "Total Sales (USD)", "date": "Transaction Date"}
)

# ADDED vertical line to mark the price uprise 
line_chart.add_vline(x="2021-01-15", line_dash="dash", line_color="red")

line_chart.add_annotation(
    x="2021-01-15",
    y=1,
    yref="paper",
    text="Price Increase",
    showarrow=False,
    font=dict(color="red"),
    xanchor="left"
)

# 4. Adjusting dashboard layout ? simple
app.layout = html.Div(style={'textAlign': 'center', 'fontFamily': 'Arial'}, children=[
    html.H1(
        children='Pink Morsel Visualiser',
        style={'color': '#2c3e50', 'padding': '20px'}
    ),
    
    html.Div(children='''
        Analisis tren penjualan Pink Morsel untuk memantau dampak kenaikan harga pada 15 Januari 2021.
    ''', style={'marginBottom': '20px'}),

    dcc.Graph(
        id='sales-line-chart',
        figure=line_chart
    )
])

# 5. Run Server
if __name__ == '__main__':
    app.run(debug=True) # ez run i hope