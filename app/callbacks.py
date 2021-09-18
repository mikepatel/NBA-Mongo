################################################################################
# Imports
from dash.dependencies import Input, Output

# import from other modules in /app/
from app import app
from db import get_data


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
