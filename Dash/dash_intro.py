# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 18:33:54 2020

@author: Suren
"""


import dash
import dash_html_components as html
import dash_core_components as dcc
import webbrowser

app=dash.Dash()


def main():
    
    app.layout=html.Div([
                     
                html.H1("Hello Dash!!!"),
                html.Div("Dash : A Data product development framework from plotly")

                     

                ])
    webbrowser.open_new('http://127.0.0.1:8050/')
    app.run_server()
    


if __name__ == '__main__':
  main()