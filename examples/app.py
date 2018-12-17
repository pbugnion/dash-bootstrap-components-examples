
from dash import Dash

import dbc_custom_components as dbccc
import dash_bootstrap_components as dbc


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


app.layout = dbc.Container(
    [
        dbccc.MyBadge(color="secondary")
    ]
)


if __name__ == "__main__":
    app.run_server(8899, debug=True)
