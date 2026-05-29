import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Load the formatted sales data
df = pd.read_csv("formatted_sales.csv")
df['date'] = pd.to_datetime(df['date'])

# Build Dash app
app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1("Soul Foods Pink Morsel Sales Visualiser",
            style={"textAlign": "center", "color": "#B22222", "fontFamily": "Arial"}),

    # Radio buttons for region filter
    html.Div([
        html.Label("Select Region:", style={"fontWeight": "bold", "marginRight": "10px"}),
        dcc.RadioItems(
            id="region-filter",
            options=[
                {"label": "All", "value": "all"},
                {"label": "North", "value": "north"},
                {"label": "South", "value": "south"},
                {"label": "East", "value": "east"},
                {"label": "West", "value": "west"}
            ],
            value="all",
            inline=True,
            style={"marginBottom": "20px"}
        )
    ], style={"textAlign": "center"}),

    # Line chart
    dcc.Graph(id="sales-line-chart")
], style={"backgroundColor": "#f9f9f9", "padding": "20px"})

# Callback for filtering by region
@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region]

    fig = px.line(
        filtered_df,
        x="date",
        y="sales",
        color="region",
        title="Pink Morsel Sales Over Time",
        labels={"date": "Date", "sales": "Sales ($)", "region": "Region"}
    )
    fig.update_layout(
        plot_bgcolor="#ffffff",
        paper_bgcolor="#f9f9f9",
        font=dict(family="Arial", size=12, color="#333333"),
        title=dict(x=0.5, font=dict(size=20, color="#B22222"))
    )
    return fig

if __name__ == "__main__":
    app.run(debug=True)
