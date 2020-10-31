

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
            html.Label("Select your city"),
            html.Br(),
            dcc.Dropdown(id='city_dropdown',
                         
                         options=[{'label':'Chennai','value':'Chennai'},{'label':'Mumbai','value':'Mumbai'},{'label':'Bangalore','value':'Bangalore'}],
                       
                          multi=True,
                         placeholder='Select a city'
                         
                         
                         
                         
                         ),
            
            #slider section
            html.Label("This is a slider"),
            dcc.Slider(
                
                min=1,
                max=10,
                value=5, # defaultly move the slider to the 5 points
                step=0.5,
                marks={i:i for i in range(10)}
                
                
                
                ),
            
            html.Br(),
            html.Br(),
            
            # RangeSlider section
             html.Label("This is a Range Slider"),
             dcc.RangeSlider(
                 min=1,
                 max=10,
                 step=0.5,
                 value=[3,8],
                 marks={i:i for i in range(10)}
                 
                 
                 
                 ),
             
             
            html.Br(),
            html.Br(),
            
            html.Div([
                
                html.Label("This is input box"),
                html.Br(),
                dcc.Input(
                    
                    placeholder="Input your name",
                    type='text',
                    value=''
                    
                    )
                
                
                ])
            
            
            
            ]
        
        
        
        
        )
    
    
    webbrowser.open_new('http://127.0.0.1:8050/')
    app.run_server()
    


if __name__ == '__main__':
  main()
    
    
    
    
    
