from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

# 1. INITIALIZE APP
app = Dash(__name__)

# 2. LOAD & CLEAN DATA
df = pd.read_csv("./formatted_data.csv")
df['sales'] = pd.to_numeric(df['sales'], errors='coerce')
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values(by="date")

# 3. STYLING DICTIONARY (Biar rapi kodenya)
COLORS = {
    'background': '#f9f9f9',
    'text': '#2c3e50',
    'accent': '#e74c3c'
}

# 4. DASHBOARD LAYOUT ? make it pretty!
app.layout = html.Div(style={'backgroundColor': COLORS['background'], 'padding': '40px', 'fontFamily': 'Segoe UI, Arial'}, children=[
    
    # Header Section
    html.H1(
        children='Pink Morsel Visualiser',
        style={'textAlign': 'center', 'color': COLORS['text'], 'fontWeight': 'bold', 'marginBottom': '10px'}
    ),
    
    html.P(
        children='Interactive sales trend analysis for Soul Foods',
        style={'textAlign': 'center', 'color': '#7f8c8d', 'marginBottom': '40px'}
    ),

    # Filter Box Section
    html.Div(style={'backgroundColor': 'white', 'padding': '20px', 'borderRadius': '10px', 'boxShadow': '0 4px 6px rgba(0,0,0,0.1)', 'maxWidth': '800px', 'margin': '0 auto 30px auto'}, children=[
        html.Label("Select Region to Filter Sales Data:", style={'fontWeight': 'bold', 'display': 'block', 'marginBottom': '15px', 'textAlign': 'center'}),
        
        dcc.RadioItems(
            id='region-filter',
            options=[
                {'label': ' North ', 'value': 'north'},
                {'label': ' East ', 'value': 'east'},
                {'label': ' South ', 'value': 'south'},
                {'label': ' West ', 'value': 'west'},
                {'label': ' All ', 'value': 'all'}
            ],
            value='all', # default selection
            inline=True,
            style={'textAlign': 'center'},
            labelStyle={'marginRight': '20px', 'cursor': 'pointer'}
        )
    ]),

    # Graph Section
    html.Div(style={'backgroundColor': 'white', 'padding': '20px', 'borderRadius': '10px', 'boxShadow': '0 4px 6px rgba(0,0,0,0.1)', 'maxWidth': '1000px', 'margin': '0 auto'}, children=[
        dcc.Graph(id='sales-line-chart')
    ])
])

# 5. CALLBACK: Filter data based on radio selection
@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-filter', 'value')
)
def update_graph(selected_region):
    # Logic filtering
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]
    
    # Create the chart
    fig = px.line(
        filtered_df, 
        x="date", 
        y="sales", 
        template="plotly_white", # biar estetik & clean
        color_discrete_sequence=[COLORS['accent']],
        labels={"sales": "Total Sales (USD)", "date": "Date"}
    )
    
    # Tambah garis vertikal harga naik
    fig.add_vline(x="2021-01-15", line_dash="dash", line_color="#34495e")
    
    # Merapikan margin chart
    fig.update_layout(
        margin={'l': 40, 'b': 40, 't': 40, 'r': 40},
        hovermode='closest'
    )
    
    return fig

# 6. Run Server
if __name__ == '__main__':
    app.run(debug=True) # ez run i hope