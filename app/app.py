################################################################################
# Imports
import dash
import dash_bootstrap_components as dbc


################################################################################
# ----- SET UP ----- #
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)
server = app.server
