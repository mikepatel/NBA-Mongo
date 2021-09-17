"""


"""
################################################################################
# Imports
import dash
import dash_html_components as html

# import from other modules in /app/
from db import get_data


################################################################################
# ----- SET UP ----- #
app = dash.Dash(__name__)
app.title = "NBA Prime"
app.layout = html.Div([
    html.H1("Test")
])


################################################################################
# Main
if __name__ == "__main__":
    app.run_server(debug=True)
