# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 13:53:22 2020

@author: Suren
"""


# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 19:14:00 2020

@author: Suren
"""


# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 18:52:38 2020

@author: Suren
"""




import dash
import dash_html_components as html
import dash_core_components as dcc
import webbrowser

app=dash.Dash()

colors={
        
        'text':'red',
        'plot_bgcolor':'grey',
        'paper_bgcolor':'black',
        'graph_text':'white'
        
        
        }

def main():
    
    app.layout=html.Div([
                     
                html.H1(children="Hello Dash!!!",
                        
                        style={
                            
                            'textAlign' : 'center',
                            'color' : colors['text']
                            }
                        
                        ),
                html.Div(children="Dash : A Data product development framework from plotly",
                         
                          style={
                            
                            'textAlign' : 'center',
                            'color' : colors['text']
                            }
                         ),
                
                dcc.Graph(id='samplechart' , figure={'data':[
                
                {'x':[4,6,8],'y':[12,16,18],'type':'bar','name':'First Chart'},
                 {'x':[4,6,8],'y':[20,30,40],'type':'bar','name':'Second Chart'}],
           'layout':{
                'title':'Simple Bar Chart',
                 'paper_bgcolor':colors['paper_bgcolor'],
                 "plot_bgcolor":colors['plot_bgcolor'],
                'font':{
                    'color':colors['graph_text']}
                }
            
            
            }
        
        
        
        
        
        )
                     

                ])
    
   
    
    webbrowser.open_new('http://127.0.0.1:8050/')
    app.run_server()
    


if __name__ == '__main__':
  main()