"""
Created on Sat 28 May 2022

@author: Young Ji
"""

def prop_calc(data, col_list, total_column):
    import pandas as pd
    """
    A function updates a list of columns in a dataframe with their proportions out of a specified column representing their totals
    
    Parameters
    ----------
    data: pandas.core.frame.DataFrame
        The dataframe of interest
        
    col_list: list
        The list of columns for which you want calculate their proportions and overwrite 
        
    total_column: str
        The name of the column which represents the total values from which to calculate the proportion values
        
    Returns
    -------
    pandas.core.frame.DataFrame
        An updated dataframe where each column in col_list reflects their original values as proportions of the totals in total_column
        
    Raises
    ------
    TypeError
        If the input argument data is not of type pandas.core.frame.DataFrame
    TypeError
        If the input argument col_list is not of type list
    AssertError
        If the input argument total_column is not in the dataframe
    
    Examples
    --------
    >>>prop_calc(data, list_of_cols, 'total')
    """

    # checks if a dataframe is the type of object being passed into the data argument
    if not isinstance(data, pd.DataFrame): 
        raise TypeError("The data argument is not of type DataFrame")
        
    # checks if a list is the type of object being passed into the col_list argument
    if not isinstance(col_list, list): 
        raise TypeError("The col_list argument is not of type list")
    
    # tests that the the total column is in the dataframe
    assert total_column in data.columns, "total_column does not exist in the dataframe"
    
    # iterate over each column in col_list
    for column in col_list:
        
        # update each column with proportions of the total 
        data[column] = data[column] / data[total_column]
        
    # return the updated dataframe 
    return data