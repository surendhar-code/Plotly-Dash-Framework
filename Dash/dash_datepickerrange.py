


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
from datetime import datetime as dt
import webbrowser

app=dash.Dash()



def main():
    
    app.layout=html.Div(
        [
           html.Label("Date Pickers Single"),
           html.Br(),
           dcc.DatePickerSingle(
    id='date-picker-single',
    date=dt(2020, 5, 10)
    ),
    html.Br(),
    html.Br(),
    html.Label("Date Pickers Range"),
    html.Br(),
    dcc.DatePickerRange(
        
        id='dt-pick-range',
        start_date=dt(2015,4,12),
        end_date_placeholder_text='Select the end date'
        
        
        )

            ]
        
        
        
        
        )
    
    
    webbrowser.open_new('http://127.0.0.1:8050/')
    app.run_server()
    


if __name__ == '__main__':
  main()
    
    
    
    
    
