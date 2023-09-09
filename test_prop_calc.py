"""
Created on Sat 28 May 2022

@author: Young Ji

This script creates helper data to test the prop_calc function created for the Python Programming for Data Science project.
"""

from prop_calc import prop_calc
import pandas as pd

# create helper data
helper_dict = {'col1': [110, 220, 330, 440, 550, 660, 770], 
            'col2': [100, 200, 300, 400, 500, 600, 700], 
            'col3': [90, 190, 290, 390, 490, 590, 690], 
            'total': [300, 610, 920, 1230, 1540, 1850, 2160]}

# transform dictionary into a dataframe
helper_data = pd.DataFrame.from_dict(helper_dict)

# define a list of the columns for use in prop_calc
helper_columns = ['col1', 'col2', 'col3']

# call the function
results = prop_calc(helper_data, helper_columns, 'total')

# tests 
assert results.shape == (7, 4), "incorrect number of rows and/or columns"
assert list(results['col1']) == [110/300, 220/610, 330/920, 440/1230, 550/1540, 660/1850, 770/2160], "incorrect output for col1"
assert list(results['col2']) == [100/300, 200/610, 300/920, 400/1230, 500/1540, 600/1850, 700/2160], "incorrect output for col2"
assert list(results['col3']) == [90/300, 190/610, 290/920, 390/1230, 490/1540, 590/1850, 690/2160], "incorrect output for col3"
