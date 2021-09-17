"""


"""
################################################################################
# Imports
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_table
import dash_bootstrap_components as dbc

# import from other modules in /app/
from db import get_data


################################################################################
# ----- SET UP ----- #
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)


################################################################################
# ----- Component: ----- #
players = [
    "LeBron James",
    "Kevin Durant",
    "Stephen Curry",
    "Giannis Antetokounmpo"
]
player_options = [{"label": p, "value": p} for p in players]

player_dropdown = dcc.Dropdown(
    id="player-dropdown",
    options=player_options,
    value=players[0]
)


player_table = dash_table.DataTable(
    id="player-table",
    style_as_list_view=True,
    style_header={'backgroundColor': 'rgb(30, 30, 30)'},
    style_cell={
        'backgroundColor': 'rgb(50, 50, 50)',
        'color': 'white'
    }
)


################################################################################
# ----- Callback: ----- #
@app.callback(
    [
        Output(component_id="player-table", component_property="data"),
        Output(component_id="player-table", component_property="columns")
    ],
    Input(component_id="player-dropdown", component_property="value")
)
def update(value):
    df = get_data(value)
    data = df.to_dict("records")
    columns = [{"name": c, "id": c} for c in df.columns]

    return data, columns


################################################################################
# ----- Layout: index ----- #
index_layout = dbc.Container(
    [
        html.H1("Player Career Stats"),
        html.Hr(),
        # input
        dbc.Row(
            [
                dbc.Col(
                    player_dropdown,
                    width=4
                )
            ]
        ),
        # output
        dbc.Row(
            [
                dbc.Col(
                    player_table
                )
            ]
        )
    ]
)


################################################################################
app.title = "NBA Prime"
app.layout = index_layout


################################################################################
# Main
if __name__ == "__main__":
    app.run_server(debug=True)
