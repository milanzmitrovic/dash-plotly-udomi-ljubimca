
from dash import Dash, html, dcc, Input, Output
from pages.personal_users import create_personal_user


app = Dash(__name__, suppress_callback_exceptions=True)
server = app.server


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Button(),
    html.Div(id='page-content'),
    dcc.Link('Go to Page 1', href='/create_personal_user')
])


@app.callback(
    Output(component_id='page-content', component_property='children'),
    Input(component_id='url', component_property='pathname')
    )
def display_page(pathname):

    if pathname == '/create_personal_user':
        return create_personal_user.layout
    elif pathname == '/delete_personal_user_account':
        return ''
    elif pathname == '/user_validation_number':
        return ''
    elif pathname == '/read_personal_user':
        return ''
    elif pathname == '/update_personal_user':
        return ''


if __name__ == '__main__':
    app.run_server(debug=True)




