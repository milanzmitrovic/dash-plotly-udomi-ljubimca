
from dash import Input, Output, html, dcc, callback


def layout():

    return html.Div([
                html.Br(),
                html.Br(),
                html.Br(),
                html.Br(),
                html.Br(),

                html.H4('Name', id='personal_user_name'),
                html.Br(),
                html.H4('Surname', id='personal_user_surname'),
                html.Br(),
                html.H4('Date of birth', id='personal_user_date_of_birth'),
                html.Br(),
                html.H4('Place of residence - Current city', id='personal_user_city'),
                html.Br(),
                html.H4('Gender', id='personal_user_gender'),
                html.Br(),
                html.H4('Image', id='personal_user_image'),
                html.Br(),

                html.Div([
                    html.Button('Submit Button', id='personal_user_submit_button'),
                ], hidden=True),
                html.Br(),

                html.Div(id='personal_user_test_output'),


            ])


app.layout = layout()


@callback([
    Output(component_id='personal_user_name', component_property='children'),
    Output(component_id='personal_user_surname', component_property='children'),
    Output(component_id='personal_user_date_of_birth', component_property='children'),
    Output(component_id='personal_user_city', component_property='children'),
    Output(component_id='personal_user_gender', component_property='children'),
    Output(component_id='personal_user_image', component_property='children')
    ],
    Input(
        component_id='personal_user_submit_button',
        component_property='n_clicks')
        )
def update_layout(input_):
    print(123)
    return 'Name', 'Surname', 'Date of birth', 'City', 'Gender', 'Image'



