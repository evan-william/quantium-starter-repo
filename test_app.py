from dash.testing.application_runners import import_app

# 1. SETUP: Import app Dash 
def test_header_presence(dash_duo):
    app = import_app("app") # call app.py
    dash_duo.start_server(app)

    # 2. TEST: CHECK HEADER
    # CHECING FOR h1 IN LAYOUT
    header = dash_duo.find_element("h1")
    
    assert header is not None # MAKING SURE HEADER is NOT empty
    assert header.text == "Pink Morsel Visualiser" # check for typo

def test_visualization_presence(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app)

    # 3. TEST: CHECK IF GRAPH IS PRESENT?
    # FINDING BASED ON ID
    graph = dash_duo.find_element("#sales-line-chart")
    
    assert graph is not None # grafik harus ada bro

def test_region_picker_presence(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app)

    # 4. TEST: CEK IF RADIO ITEMS IS PRESENT
    picker = dash_duo.find_element("#region-filter")
    
    assert picker is not None # RADIO FILTER MUST BE PRESENT