#import numpy and pandas
import numpy as np
import pandas as pd

#import bokeh
from bokeh.charts import Bar, output_file, save

#create dataframe to read file/organize data
df = pd.read_csv('parks.csv')

#label the x axis as state, counting the amount of parks in each state
p = Bar(df, 'State') 

#set up file
output_file('Bar.html')

#save graph
save(p)
        


