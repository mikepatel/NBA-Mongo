################################################################################
# Imports
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_table


################################################################################
# ----- Component: player-dropdown ----- #
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


################################################################################
# ----- Component: player-table ----- #
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
# ----- Component: inputs ----- #
inputs = dbc.FormGroup([
    player_dropdown
])


################################################################################
