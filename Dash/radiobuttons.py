

# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 15:10:49 2020

@author: Suren
"""
import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
import numpy as np
import webbrowser

app=dash.Dash()



def main():
    
    app.layout=html.Div(
        [
           
            html.Label("Radio Items"),
            html.Br(),
            dcc.RadioItems(
                
            options=[{'label':'Chennai','value':'Chennai'},{'label':'Mumbai','value':'Mumbai'},{'label':'Bangalore','value':'Bangalore'}],

            value='Chennai' 
            
                )
               
               
            
            
            ]
        
        
        
        
        )
    
    
    webbrowser.open_new('http://127.0.0.1:8050/')
    app.run_server()
    


if __name__ == '__main__':
  main()
    
    
    
    
    
