# Build App
app = JupyterDash(__name__)

# Load data and cast survived col as a string
df = sns.load_dataset('mpg')

# Create labebls for PClass input
show = ['displacement', 'horsepower', 'weight', 'acceleration']


app.layout = html.Div([
                       #Title
                       html.H1("Dynamic App Test"),

    
                       # Area to hold Graph
                       dcc.Graph(id="graph"),

    

                       # First Dynamic Input
                       html.Label([
                                   "Compare Miles per Gallon with the following variable",
                                    dcc.Dropdown(
                                        id='var', 
                                        clearable=False,
                                        value= 'weight', 
                                        options=[{'label': "Displacement", 'value': "displacement"},
                                                 {'label': "Horse Power", 'value': "horsepower"},
                                                 {'label': "Weight", 'value': "weight"},
                                                 {'label': "Acceleration", 'value': "acceleration"}]
                                        )
                       ]),
                       
    
    
                       # Line Break
                       html.Br([]),

    
    
    
 #                      # Second Dynamic Input
 #                      html.Label([
 #                                  "Class",
 #                                  dcc.RadioItems(
 #                                      id="class",
 #                                      options=[{'label':x, "value":x} for x in class_label],
 #                                      value='None'                                    )  
 #                                                       ])

                       
])



# Define callback to update graph based on survived

# Note: if you have more than one input or output make sure to have them in a list
@app.callback(
    Output('graph', 'figure'),
    Input("var", "value")
)


def update_figure(var):

    x_axis = var
    px.scatter(
        data_frame = df, # data
        x = x_axis, # x value
        y = "mpg", # y value
        color = "model_year", # Assign Color Marks
        facet_col="origin", # Create a separate row based plot based on this column
        title = "Plotly Scatter",
        )



app.run_server(port = 8001)
