######################################
# FactorSorting.py 
######################################
# Description:
# * Sort factors using target method.

from pandas import DataFrame, read_csv

class FactorSorting:
    
    def __init__(self):
        """
        * Using dataset, sort data readily 
        for use in main model.
        """
        pass


    ####################
    # Private Helpers:
    ####################
    @staticmethod
    def __Validate(data):
        """
        * Validate constructor parameters.
        """
        if not isinstance(data, DataFrame):
            raise Exception('data must be a DataFrame.')