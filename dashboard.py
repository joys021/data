import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import numpy as np

# Uses an External Stylesheet
# Use a css file from your GitHub Pages site 
external_stylesheets = ['https://usfmumaanalyticsteam.github.io/learn.css']

# Creates the app to instantiate the content for the Dashboard and use the external_stylesheets
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Use a csv dataset from a repository in your GitHub account. Use the Raw URL to expose the data to the Python dataframe
df = pd.read_csv('https://joys021.github.io/data/airplane-clean.csv')
pv1 = pd.pivot_table(df, index=['Operator'],values=["Fatalities"],  aggfunc=sum, fill_value=0)
trace1 = go.Bar(x=pv1.index, y=pv1[('Fatalities')])

pv2 = pd.pivot_table(df, index=['Operator'],values=["Aboard"],  aggfunc=sum, fill_value=0)
trace2 = go.Bar(x=pv2.index, y=pv2[('Aboard')])

labels = df['operator-type'].value_counts().index
values = df['operator-type'].value_counts().values
trace3 = go.Figure(data=[go.Pie(labels=labels, values=values)])

df['year'] = pd.DatetimeIndex(df['Date']).year


pv4 = pd.pivot_table(df, index=['year'],columns=['operator-type'],values=["Fatalities"],  aggfunc=sum, fill_value=0)
print(pv4)



fig = go.Figure()
# Create and style traces
fig.add_trace(go.Scatter(x=pv4.index, y=pv4[('Fatalities','MILITARY')], name='Military',
                         line=dict(color='firebrick', width=4)))
fig.add_trace(go.Scatter(x=pv4.index, y=pv4[('Fatalities','PASSENGER')], name = 'Passenger',
                         line=dict(color='royalblue', width=4)))

fig.update_layout(title='Fatalities by operator type over the years',
                   xaxis_title='Year',
                   yaxis_title='Count of Fatalities')

#df2 = pd.read_csv('https://raw.githubusercontent.com/USFMumaAnalyticsTeam/data/master/usa-agricultural-exports-2011.csv')




# Add content to the app layout
# Begin all content DIV
app.layout=html.Div([
    # Add your HTML tags to the content - notice a comma is added between HTML elements
    html.H1('Data Visualization for Story Telling'),
    html.Div([
        html.P('Airplane crash in 2015..'),
    ]),
    # Begin of DIV surrounding both Tables
    html.Div([
    # Begin of First Table
    html.Table(style={'width':'100%'},
               # Begin of Table children
               children=[
                   #######################################################################
                   # Begin of First Tr
                 html.Tr(
                     #Begin Tr children
                     children=[
                         # Begin Th
                         
                         html.Th(style={'width':'150%'},
                             # Begin Th children
                             children=[
                                 html.H3('Count of crashes by operator')
                             # End of Th children   
                             ]
                         
                         # End of Th - Notice a comma is placed here to separate the next Th
                         ),
                         # Begin of Th
                        
                         
                         # End of Th
                         
                         
                     # End of Tr children    
                     ]
                 # End of First Tr - Notice a comma is placed here to separate the next Tr
                 ),
                 #########################################################################
                 # Begin of Second Tr
                 html.Tr(
                     #Begin Tr children
                     children=[
                         # Begin Td
                         html.Td(
                             # Begin Td children
                             children=[
                                    # Display bar graph
                                    dcc.Graph(
                                    id='example-graph',
                                    figure={
                                        'data': [trace1],
                                        'layout': go.Layout(title='Fatalities by operator', barmode='stack')
                                    }
                                # End of Chart 1
                                )
                              # End of Td children   
                             ]
                         
                         # End of Td - Notice a comma is placed here to separate the next Th
                         ),
                         # Being of Td
                         
                     # End of Tr children    
                     ]
                 # End of Tr
                 )     
                #########################################################################                   
               #End of Table Children    
               ]
              # End of First Table - Notice a comma is placed here to separate the next Table
              ),
    
    #########################################################################################   
    # Begin of Second Table
    html.Table(style={'width':'100%'},
               children=[
                 #######################################################################
                 # Begin First Tr
                 html.Tr(
                     #Begin Tr children
                     children=[
                         # Begin Th
                         html.Th(style={'width':'150%'},
                             # Begin Th children
                             children=[
                                 html.H3('Count of People abroad by operator')
                             # End of Th children   
                             ]
                         
                         # End of Th - Notice a comma is placed here to separate the next Th
                         ),
                        
                        
                     # End of Tr children    
                     ]
                 # End of First Tr
                 ),
                   
                    ######################################################################
                    # Begin of Second Tr
                     html.Tr(
                         #Begin Tr children
                         children=[
                             # Begin Td
                             html.Td(
                                 # Begin Td children
                                 children=[
                                        # Display a simple line graph
                                        dcc.Graph(
                                        id='g1', 
                                        figure={
                                        'data': [trace2],
                                        'layout': go.Layout(title='Number of People Aboard by operator', barmode='stack')
                                    }

                                        )
                             # End of Td children   
                             ]
                         
                         # End of Td - Notice a comma is placed here to separate the next Th
                         ),
                         # Begin of Td
                         
                         
                         # Begin of Td
                         html.Td(
                             # Begin of Td children
                             children=[
                                    # Execute custom generate_table function and display data
                                    # Use data from dataframe df2
                                    #generate_table(df2)
                             # End of Td children    
                             ]
                         # End of Td
                         )
                     # End of Tr children    
                     ]
                 # End of Second Tr
                 )     
               
               #######################################################################
               #End of Table Children    
               ]
              #########################################################################################
              # End of Second Table - Notice a comma is placed here to separate the next Content
              ),

              #########################################################################################   
    # Begin of Third Table
             html.Table(style={'width':'100%'},
               children=[
                 #######################################################################
                 # Begin First Tr
                 html.Tr(
                     #Begin Tr children
                     children=[
                         # Begin Th
                         html.Th(style={'width':'150%'},
                             # Begin Th children
                             children=[
                                 html.H3('Fatalities by Operator Types')
                             # End of Th children   
                             ]
                         
                         # End of Th - Notice a comma is placed here to separate the next Th
                         ),
                        
                        
                     # End of Tr children    
                     ]
                 # End of First Tr
                 ),
                   
                    ######################################################################
                    # Begin of Second Tr
                     html.Tr(
                         #Begin Tr children
                         children=[
                             # Begin Td
                             html.Td(
                                 # Begin Td children
                                 children=[
                                        # Display a simple line graph
                                        dcc.Graph(
                                        id='g3', 
                                        figure=trace3

                                        )
                             # End of Td children   
                             ]
                         
                         # End of Td - Notice a comma is placed here to separate the next Th
                         ),
                         # Begin of Td
                         
                         
                         # Begin of Td
                         html.Td(
                             # Begin of Td children
                             children=[
                                    # Execute custom generate_table function and display data
                                    # Use data from dataframe df2
                                    #generate_table(df2)
                             # End of Td children    
                             ]
                         # End of Td
                         )
                     # End of Tr children    
                     ]
                 # End of Second Tr
                 )     
               
               #######################################################################
               #End of Table Children    
               ]
              #########################################################################################
              # End of Third Table - Notice a comma is placed here to separate the next Content
              ),
               #########################################################################################   
    # Begin of Fourth Table
             html.Table(style={'width':'100%'},
               children=[
                 #######################################################################
                 # Begin First Tr
                 html.Tr(
                     #Begin Tr children
                     children=[
                         # Begin Th
                         html.Th(style={'width':'150%'},
                             # Begin Th children
                             children=[
                                 html.H3('Fatalities by operator type')
                             # End of Th children   
                             ]
                         
                         # End of Th - Notice a comma is placed here to separate the next Th
                         ),
                        
                        
                     # End of Tr children    
                     ]
                 # End of First Tr
                 ),
                   
                    ######################################################################
                    # Begin of Second Tr
                     html.Tr(
                         #Begin Tr children
                         children=[
                             # Begin Td
                             html.Td(
                                 # Begin Td children
                                 children=[
                                        # Display a simple line graph
                                        dcc.Graph(
                                        id='g4', 
                                        figure= fig

                                        )
                             # End of Td children   
                             ]
                         
                         # End of Td - Notice a comma is placed here to separate the next Th
                         ),
                         # Begin of Td
                         
                         
                         # Begin of Td
                         html.Td(
                             # Begin of Td children
                             children=[
                                    # Execute custom generate_table function and display data
                                    # Use data from dataframe df2
                                    #generate_table(df2)
                             # End of Td children    
                             ]
                         # End of Td
                         )
                     # End of Tr children    
                     ]
                 # End of Second Tr
                 )     
               
               #######################################################################
               #End of Table Children    
               ]
              #########################################################################################
              # End of Fourth Table - Notice a comma is placed here to separate the next Content
              ),
    
    # End of DIV surrounding both Tables
    ]),
               
# End of all content DIV
])

# Run the app on the web server
if __name__ == '__main__':
    # Set debug to False. Some configurations are not setup for Debug
    app.run_server(debug=False)

