
from dash import Dash, html, dcc, Input, Output
from pages.personal_users import create_personal_user
from pages.personal_users import read_personal_user

app = Dash(__name__, suppress_callback_exceptions=True)
server = app.server


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Button(),
    html.Div(id='page-content'),
    dcc.Link('Go to Page 1', href='/personal_user/create'),
    html.Br(),
    dcc.Link('Go to Page 2', href='/personal_user/read')
])


@app.callback(
    Output(component_id='page-content', component_property='children'),
    Input(component_id='url', component_property='pathname')
    )
def display_page(pathname):

    if pathname == '/personal_user/create':
        return create_personal_user.layout
    elif pathname == '/delete_personal_user_account':
        return ''
    elif pathname == '/user_validation_number':
        return ''
    elif pathname == '/personal_user/read':
        return read_personal_user.layout()
    elif pathname == '/update_personal_user':
        return ''


if __name__ == '__main__':
    # app.run_server(debug=True)
    app.run_server(host="0.0.0.0", port=8050, debug=True)




