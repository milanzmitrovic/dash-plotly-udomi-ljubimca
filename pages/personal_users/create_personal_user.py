
from dash import dcc, html, Input, Output, callback, State
from pages.global_ui_components.header.header_file import header


layout = html.Div([

    header,
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),

    dcc.Input('Name', id='personal_user_name'),
    html.Br(),
    dcc.Input('Surname', id='personal_user_surname'),
    html.Br(),
    dcc.Input('Date of birth', id='personal_user_date_of_birth'),
    html.Br(),
    dcc.Input('Place of residence - Current city', id='personal_user_city'),
    html.Br(),
    dcc.Input('Gender', id='personal_user_gender'),
    html.Br(),
    dcc.Input('Image', id='personal_user_image'),
    html.Br(),

    html.Button('Submit Button', id='personal_user_submit_button'),
    html.Br(),

    html.Div(id='personal_user_test_output'),

    dcc.Link('Go to home page', href='/')



])


@callback(
    Output(component_id='personal_user_test_output', component_property='children'),
    [Input(component_id='personal_user_submit_button', component_property='n_clicks'),
     State(component_id='personal_user_name', component_property='value'),
     State(component_id='personal_user_surname', component_property='value'),
     State(component_id='personal_user_date_of_birth', component_property='value'),
     State(component_id='personal_user_city', component_property='value'),
     State(component_id='personal_user_gender', component_property='value'),
     State(component_id='personal_user_image', component_property='value')])
def update_output(n_clicks,
                  name,
                  surname,
                  date_of_birth,
                  city,
                  gender,
                  image
                  ):
    return f"{n_clicks} - {name} - {surname} - {date_of_birth} - {city} - {gender} - {image}"
