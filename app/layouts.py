################################################################################
# Imports
import dash_html_components as html
import dash_bootstrap_components as dbc

# import from other modules in /app/
from components import inputs, player_table


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
                    inputs,
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
