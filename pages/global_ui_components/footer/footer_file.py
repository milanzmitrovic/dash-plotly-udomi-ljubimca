
from dash import html
import dash_bootstrap_components as dbc

# footer = html.Div([], style={'backgroundColor': 'blue'})


footer = dbc.Container([

    dbc.Row([
        html.Br(),
        html.Br(),
        # html.Br()

    ]),

    dbc.Row([

        dbc.Col(html.H5("O nama",
                        style={'text-align': 'center'}),
                align="center",
                lg=3,
                xl=1,
                sm=3,
                xs=12
                ),

        dbc.Col(html.H5("Prijavi problem",
                        style={'text-align': 'center'}),
                align="center",
                lg=3,
                xl=1,
                sm=3,
                xs=12
                ),

        dbc.Col(html.H5("Uslovi korišćenja",
                        style={'text-align': 'center'}),
                align="center",
                lg=3,
                xl=1,
                sm=3,
                xs=12
                ),

        dbc.Col(html.H5("Kontakt",
                        style={'text-align': 'center'}),
                align="center",
                lg=3,
                xl=1,
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

    html.Br(),

    dbc.Row(html.H6("@ 2022 Udomi Ljubimce | All Rights Reserved",
                    style={'text-align': 'center'}),
            align='center'
            ),
    html.Br()

],
    style={'backgroundColor': '#D3D3D3'},
    fluid=True,
)




