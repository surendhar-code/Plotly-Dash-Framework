


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
           dcc.Markdown('''#### Dash and Markdown

Dash supports [Markdown](http://commonmark.org/help).

Markdown is a simple way to write and format text.
It includes a syntax for things like **bold text** and *italics*,
[links](http://commonmark.org/help), inline `code` snippets, lists,
quotes, and more.
''')
        
        

            ]
        
        
        
        
        )
    
    
    webbrowser.open_new('http://127.0.0.1:8050/')
    app.run_server()
    


if __name__ == '__main__':
  main()
    
    
    
    
    
