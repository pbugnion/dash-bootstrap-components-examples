
from dash import Dash

import dbc_custom_components as dbccc
import dash_bootstrap_components as dbc
import dash_html_components as html


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


app.layout = dbc.Container(
    [
        html.H1("Demo app"),
        dbc.Row(
            [
                dbc.Col(dbccc.MyBadge(color="secondary"), width=2),
                dbc.Col(html.Pre("<- That is a custom badge component"))
            ]
        )
    ]
)


if __name__ == "__main__":
    app.run_server(8899, debug=True)
