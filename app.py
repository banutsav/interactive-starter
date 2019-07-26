import dash
import dash_core_components as dcc
import dash_html_components as html

# Import library of standard functions
import lp
# Import Vizualisation helper functions 
import viz as vz

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
source = lp.getDataSource()
# Get data frame and clean it
df = lp.cleanMarksData(lp.convertCSVToDf(source))

app.layout = html.Div(children=[
    #html.H4(children='Student Report'),
    #html.Div(children='''Analysis of test scores for RC, Math and Writing for 2017-18'''),
    dcc.Graph(id='rc-scatter',figure=vz.scatterRC(df)),
    dcc.Graph(id='writing-scatter',figure=vz.scatterWriting(df)),
    dcc.Graph(id='math-hist',figure=vz.histMath(df))
])

if __name__ == '__main__':
    app.run_server(debug=True)