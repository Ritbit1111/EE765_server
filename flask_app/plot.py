import numpy as np
import pandas as pd
import time
import os

from bokeh.models import Slider
from bokeh.models.widgets import Button, TextInput
from bokeh.layouts import row, column, gridplot
from bokeh.plotting import Figure, ColumnDataSource
from bokeh.embed import components 

def get_normal(mu = 0, sigma = 1, k = 1000):
    #np.random.seed(2)
    s = np.random.normal(mu, sigma, k)
    hist, edges = np.histogram(s, density=True, bins=1000)
    left_edges = edges[:-1]
    right_edges = edges[1:]
    return dict(hist = hist, left_edges = left_edges, right_edges = right_edges)

class Plot():
    def plt(self):
        source_normal = ColumnDataSource(data = get_normal(0,1,10000))
        plot_normal = Figure(plot_width = 450, plot_height = 450, x_range = (-6,6), title = 'Normal')
        plot_normal.quad(top='hist', bottom=0, left='left_edges', right='right_edges', source= source_normal, fill_color="navy")        
        def update_plot_normal(attrname, old , new):
            source_normal.data = get_normal(mu_slider.value, sigma_slider.value, 10000)
            
        mu_slider = Slider(start = -5, end = 5, value = 0, step = 0.2, title = 'Mean')
        mu_slider.on_change('value', update_plot_normal)
            
        sigma_slider = Slider(start = 0.1, end = 5, value = 1, step = 0.2, title = 'Std_Dev')
        sigma_slider.on_change('value', update_plot_normal)
        layout = row(plot_normal, column(mu_slider, sigma_slider))
