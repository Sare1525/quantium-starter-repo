import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Load the formatted sales data
df = pd.read_csv("formatted_sales.csv")
df['date'] = pd.to_datetime(df['date'])

# Create line chart
fig = px.line(
    df,
    x="date",
    y="sales",
    color="region",
    title="Pink Morsel Sales Over Time",
    labels={"date": "Date", "sales": "Sales ($)", "region": "Region"}
)

# Build Dash app
app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1("Soul Foods Pink Morsel Sales Visualiser"),
    dcc.Graph(
        id="sales-line-chart",
        figure=fig
    )
])

if __name__ == "__main__":
    app.run(debug=True)   # ✅ use app.run instead of app.run_server
