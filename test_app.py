import pytest
from dash.testing.application_runners import import_app

# Load your Dash app
@pytest.fixture
def app_runner():
    return import_app("app")   # assumes your app file is app.py

# Test 1: Header is present
def test_header_is_present(dash_duo, app_runner):
    dash_duo.start_server(app_runner)
    header = dash_duo.find_element("h1")
    assert "Soul Foods Pink Morsel Sales Visualiser" in header.text

# Test 2: Visualisation (line chart) is present
def test_graph_is_present(dash_duo, app_runner):
    dash_duo.start_server(app_runner)
    graph = dash_duo.find_element("#sales-line-chart")
    assert graph is not None

# Test 3: Region picker (radio buttons) is present
def test_region_picker_is_present(dash_duo, app_runner):
    dash_duo.start_server(app_runner)
    radio = dash_duo.find_element("#region-filter")
    assert radio is not None
