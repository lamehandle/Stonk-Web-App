import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import datetime as datetime

# dataframe for plotting
df = data
#  x-axis should be the Date
x_axis = None
#  y-axis should be price OCLH
y_axis = None
open = None
close = None
low = None
high = None

fig = go.Figure(data=df,
                open=open,
                high=high,
                low=low,
                close=close)



# how do I include volume or does it matter?
# probably not

