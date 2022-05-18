

from dash import html
import dash_bootstrap_components as dbc


header = dbc.Container([

    dbc.Row([
        html.Br(),

    ], style={'height': '10px'}),

    dbc.Row([


        dbc.Col(html.H5("O nama",
                        style={'text-align': 'center'}),
                align="center",
                lg=3,
                xl=2,
                sm=3,
                xs=12
                ),

        dbc.Col(html.H5("Prijavi problem",
                        style={'text-align': 'center'}),
                align="center",
                lg=3,
                xl=2,
                sm=3,
                xs=12
                ),

        dbc.Col(html.H5("Uslovi korišćenja",
                        style={'text-align': 'center'}),
                align="center",
                lg=3,
                xl=2,
                sm=3,
                xs=12
                ),

        dbc.Col(html.H5("Kontakt",
                        style={'text-align': 'center'}),
                align="center",
                lg=3,
                xl=2,
                sm=3,
                xs=12
                )

    ],
        # This command is of great importance!!!
        # Why? - Because it enables sum of bootstrap columns not to be equal to 12 (can be less than 12).
        # But, sum should be even number.
        # Content of columns will be centered, equal margin to both sides will be created.
        justify='center'
    ),

    dbc.Row([
        html.Br(),

    ], style={'height': '5px'}),


],
    style={'backgroundColor': '#D3D3D3'},
    fluid=True,
)


