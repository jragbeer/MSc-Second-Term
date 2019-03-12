import pandas as pd
import numpy as np
import datetime
import time
import sqlite3
import os
import glob
from bokeh.plotting import figure, show
from bokeh.models import BasicTickFormatter, HoverTool, LassoSelectTool, BoxSelectTool, BoxZoomTool, ResetTool, Span, FactorRange,OpenURL, CustomJS, DatetimeTickFormatter, LabelSet
from bokeh.models import NumeralTickFormatter, WheelZoomTool, PanTool, SaveTool, TapTool, PolySelectTool,ColumnDataSource, LinearAxis, Range1d, FuncTickFormatter, Band, Toggle, SingleIntervalTicker
from bokeh.models.widgets import Select, RadioGroup, DataTable, StringFormatter, TableColumn, NumberFormatter, Button, inputs, CheckboxButtonGroup, Div
from bokeh.layouts import widgetbox, row, column
from bokeh.events import ButtonClick, SelectionGeometry
from bokeh.io import curdoc
from bokeh.colors import Color
from bokeh.core.properties import Seq, Date
from os.path import dirname, join
from bokeh.models.widgets import TextInput

def circlecallback(event):
    try:
        thing = int(text_input.value)
    except:
        try:
            thing = float(text_input.value)
        except:
            div2.text = 'Not a number'
    squa.visible = False
    if isinstance(thing, int) or isinstance(thing, float):
        source.data = ColumnDataSource(data = dict(x = [0], y = [0], radius = [thing], top = [0], bottom = [0] , left = [0], right = [0])).data
        circ.visible = True
        div2.text = ''
    else:
        pass
def squarecallback(event):
    try:
        thing = int(text_input.value)
    except:
        try:
            thing = float(text_input.value)
        except:
            div2.text = 'Not a number'
    circ.visible = False
    if isinstance(thing, int) or isinstance(thing, float):
        source.data = ColumnDataSource(data=dict(x=[0], y=[0], radius=[0], top=[thing/2], bottom=[-thing/2], left=[-thing/2], right=[thing/2])).data
        squa.visible = True
        div2.text = ''
    else:
        pass


def clearcallback(event):
    source.data = ColumnDataSource(data = dict(x=[], y=[], radius=[], top=[], bottom=[], left=[], right=[])).data


doc = curdoc()
#clears the html page and gives the tab a name
doc.clear()
doc.title = 'Homework 4 Question 2'

source = ColumnDataSource(data= dict(x=[], y=[], radius=[], top=[], bottom=[], left=[], right=[]))

p = figure(plot_width=800, plot_height=800,x_range=(-20, 20), y_range=(-20, 20),
           tools=[BoxSelectTool(), BoxZoomTool(), ResetTool(), WheelZoomTool(), SaveTool(), PanTool()],
           x_axis_label='Units', y_axis_label="Units", toolbar_location="right")

circ = p.circle(x = 'x', y = 'y',radius = 'radius',color="firebrick", alpha=0.8, source = source, radius_dimension = 'max')
squa = p.quad(top = 'top', bottom = 'bottom', left = 'left', right = 'right', color="navy", alpha=0.8, source = source)


p.xaxis.ticker = [x for x in range(-20, 20)]
p.yaxis.ticker = [x for x in range(-20, 20)]
circ.visible = False
squa.visible = False

text_input = TextInput(value="", title="INPUT (only numbers):")

circlebutton = Button(label="Circle", button_type="primary")
circlebutton.on_event(ButtonClick, circlecallback)

squarebutton = Button(label="Square", button_type="primary")
squarebutton.on_event(ButtonClick, squarecallback)

clearbutton = Button(label="Clear", button_type="warning")
clearbutton.on_event(ButtonClick, clearcallback)

div2 = Div(text = '',width=300, height=100)

aa = row([text_input, circlebutton,squarebutton,clearbutton])
bb = column([p, aa, div2])
doc.add_root(bb)
show(bb)

