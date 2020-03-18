#import plotly.figure_factory as ff
import pandas as pd
import os
import plotly.graph_objects as go
#import numpy as np

os.chdir("C:\\Users\\mlein\\Documents\\Python\\Untitled Folder")

df = pd.read_csv('.\\Ozone_ISA_CVD_effects.csv')

fig = go.Figure(data=go.Heatmap(
                x=df['STUDY_TYPE'],
                y=df['ENDPOINT_CATEGORY'],
                z=df['Increasing (Red) Decreasing (Blue)']))

fig.show()