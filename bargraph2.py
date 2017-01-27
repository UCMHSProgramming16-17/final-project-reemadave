#import nump and pandas
import numpy as np
import pandas as pd

#import bokeh
from bokeh.charts import Bar, output_file, save

#create dataframe
df = pd.read_csv('parks.csv')

#label
p = Bar(df, 
    'State', 
    'Acres', 
    agg = 'mean',
    color = "blue",
    title = "Average Amount of Acres of National Park in Each State",
    legend = 'top_right')

#set up file
output_file('Bar2.html')

#save graph
save(p)