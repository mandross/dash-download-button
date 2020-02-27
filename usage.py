import download_button
import dash
from dash.dependencies import Input, Output
import dash_html_components as html

EXTERNAL_STYLESHEETS = [
    'https://cdn.jsdelivr.net/npm/foundation-sites@6.5.3/dist/css/foundation.min.css',
    'https://cdnjs.cloudflare.com/ajax/libs/foundicons/3.0.0/foundation-icons.min.css'
]

app = dash.Dash(__name__, external_stylesheets=EXTERNAL_STYLESHEETS)

app.layout = html.Div([
    download_button.DownloadButton(
        ['Download Figure Please'],
        id='button',
        className='button',
        target='output'
    ),
    html.Div(id='output')
])

@app.callback(Output('output', 'children'), [Input('button', 'id')])
def display_output(value):
    return 'You have entered {}'.format(value)

if __name__ == '__main__':
    app.run_server(debug=True)
