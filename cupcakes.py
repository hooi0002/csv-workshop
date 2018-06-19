"""PyBay Project Night CSV workshop.

This code operates on data obtained from a csv file. 
The data represents information about monthly cupcake sales.
"""

import csv
import datetime

def get_month_info(filename):
    """Determine the month, year, and week numbers included in the file data.

    Inputs:
    - filename: str, name of file to be read

    Returns a tuple: month (int), year (int), weeks (list)
    """
    pass


def get_most_popular_flavor(filename):
    """Determine most popular cupcake flavor.

    Inputs:
    - filename: str, name of file to be read

    Returns a string.
    """
    
    pass


def get_weekly_sales(filename, wk_num):
    """Determine number of transactions for a given week in the year.

    Inputs:
    - filename: str, name of file to be read
    - wk_num: int, number of week in year

    Returns an integer.
    """
    
    pass


def prices_to_dict(filename, fieldnames):
    """Makes a dictionary from a CSV file data.

    Inputs:
    - filename: string, name of the csv file to be read
    - fieldnames: list of field names in the file (expects list with two fields)

    Returns a dictionary.
    """
    
    pass


def get_gross_income(filename, prices):
    """Determine gross income from cupcake sales.
    
    Inputs:
    - filename: string, name of the csv file to be read
    - prices: dictionary, keys are strings, values are floats

    Returns a float.
    """
    
    pass


def get_most_popular_day_of_week(filename):
    """Determine most popular day of the week to buy cupcakes.

    Inputs:
        - filename: string, name of the csv file to be read

    Returns a string.  
    """
    
    pass


def transform_data(infile, outfile):
    """Transform sales data and write to file.

    Inputs:
    - infile: string, name of the csv file to be read
    - outfile: string, name of the csv file where data will be written

    Returns None.
    """
    
    pass


def generate_monthly_sales_report(filename, prices):
    """Prints information about sales for a given month.

    Inputs:
    - filename: string, name of the csv file to be read
    - prices: dictionary, keys are strings, values are floats

    Returns None.
    """

    pass
