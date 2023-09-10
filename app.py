import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import spacy

# Initialize the Dash app
app = dash.Dash(__name__,title="Task 2")

divmodal_style = {
    'text-align': 'center',
    'height' : '500px',
    'width' : '500px',
    'border' : '5px solid black',
    'display' : 'inline-block',
    'background-color': '#EF9595',
    'margin-top' : '25vh',
    'margin-left' : '25vw',
    'padding-top' : '100px',

}

button_style = {
    'background-color': '#008CBA',  
    'color': 'white',              
    'border': 'none',              
    'padding': '10px 20px',       
    'border-radius': '5px',       
    'cursor': 'pointer',
}

heading_style = {
    'color': 'purple', 
}

# Set up the app layout
app.layout = html.Div([
    html.H1("Text Similarity Calculator", style=heading_style),
    dcc.Input(id='input1', type='text', placeholder='Enter text 1'),
    html.Br(),
    html.Br(),
    dcc.Input(id='input2', type='text', placeholder='Enter text 2'),
    html.Br(),
    html.Br(),
    html.Button('Calculate Similarity', id='submit-button',style=button_style),
    html.Br(),
    html.Br(),
    html.Div(id='output-similarity')
],style=divmodal_style)

# Define a callback function to calculate and display the similarity score
@app.callback(
    Output('output-similarity', 'children'),
    [Input('submit-button', 'n_clicks')],
    [dash.dependencies.State('input1', 'value'),
     dash.dependencies.State('input2', 'value')]
)
def calculate_similarity(n_clicks, text1, text2):
    if text1 and text2:
        # Load spaCy model
        nlp = spacy.load('en_core_web_sm')
        
        # Process the input texts
        doc1 = nlp(text1)
        doc2 = nlp(text2)
        
        # Calculate similarity score (using spaCy's similarity method)
        similarity_score = doc1.similarity(doc2)
        
        return f"Similarity Score: {similarity_score:.2f}"
    else:
        return ""

if __name__ == '__main__':
    app.run_server(debug=True)





