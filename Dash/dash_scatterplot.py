# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 18:52:38 2020

@author: Suren
"""




import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
import numpy as np
import webbrowser

app=dash.Dash()

colors={
        
        'text':'red',
        'plot_bgcolor':'grey',
        'paper_bgcolor':'black',
        'graph_text':'white'
        
        
        }

x_val=np.random.randint(1,61,60)
y_val=np.random.randint(1,61,60)

def main():
    
    app.layout=html.Div([
                     
                dcc.Graph(
                    
                    id='scatter plot',
                    figure={
                        
                        'data':[
                            go.Scatter(
                                x=x_val,
                                y=y_val,
                                mode='markers'
                                
                                
                                
                                )
                            
                            
                            
                            ],
                        'layout':go.layout(
                            
                            title='Scatter plot on Random 60 points',
                            xaxis={'title':'Random X Values'},
                            yaxis={'title':'Random Y Values'}       
                            
                            
                            )
                        
                        }
                    
                    
                    
                    )
                    
                   

                ])
    
   
    
    webbrowser.open_new('http://127.0.0.1:8050/')
    app.run_server()
    


if __name__ == '__main__':
  main()