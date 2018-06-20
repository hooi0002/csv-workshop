"""SF Python Project Night: CSV workshop.

The goal of this workshop is to learn how to read data from a .csv file,
manipulate the data in interesting ways, and write data to a .csv file. With
these skills, we can automate boring tasks, like data entry. By using Python to
examine the data, we can go beyond the analytical power of spreadsheet editors, 
freely exploring it for insights.

To read from and write to .csv files, we'll use the csv module. Because our 
sample data involves dates, we'll also be using the datetime module. Both
modules are part of the Python standard library.

The main file we'll be working with is cupcakes.csv. This file contains 
information about monthly cupcake sales. Each line in the file is a record of
sale for an individual cupcake, which may be part of a larger order. 

The fields of cupcakes.csv are as follows: date,order number,flavor

The prices.csv file contains information about the price of cupcakes by flavor.
Using the data in this file, we will create a dictionary to lookup cupcake
pricing.

The fields of prices.csv are as follows: flavor,price 
"""

import csv
import datetime


def get_most_popular_flavor(filename):
    """Determine the most popular cupcake flavor.

    The most popular cupcake flavor is the one that was sold the most.

    Inputs:
    - filename: string, name of the .csv file to be read

    Returns a string.
    """
    
    pass


def prices_to_dict(filename):
    """Makes a dictionary from a .csv file data.

    The input .csv file should have exactly two fields: flavor, price 
    Hint: Try using csv.DictReader.

    Inputs:
    - filename: string, name of the .csv file to be read

    Returns a dictionary.
    """

    pass


def get_gross_income(filename, prices):
    """Determine gross income from cupcake sales.
    
    Inputs:
    - filename: string, name of the .csv file to be read
    - prices: dictionary, where the keys are cupcake flavors (strings) and the
              values are the corresponding cupcake prices (floats)

    Returns a float.
    """
    
    pass


def get_weekly_sales(filename, wk_num):
    """Determine number of sales transactions for a given week in the year.

    Hint: Use the datetime module to parse date strings.

    Inputs:
    - filename: string, name of the .csv file to be read
    - wk_num: integer, number of week in year

    Returns an integer.
    """
    
    pass


def get_most_popular_day_of_week(filename):
    """Determine most popular day of the week to buy cupcakes.

    Inputs:
    - filename: string, name of the .csv file to be read

    Returns a string.  
    """
    
    pass


def tabulate_data(infile, outfile):
    """Tabulate order data and write to file.

    Lines of the input file represent individual cupcakes purchased.
    A single order can span multiple lines of the input file.

    Example:
        date,order,flavor
        05/01/2018,11,chocolate
        05/01/2018,11,chocolate
        05/01/2018,11,green tea

    Lines in the output file represent individual orders with the number of 
    cupcakes purchased tallied by flavor.

    Example:
        date,order,chocolate,green tea,lemon,red velvet,tuxedo,vanilla
        05/01/2018,11,2,1,0,0,0,0

    Inputs:
    - infile: string, name of the .csv file containing raw order data
    - outfile: string, name of the .csv file where tabulated data will be written to

    Returns None.
    """
    
    pass


def get_month_info(filename):
    """Determine the month, year, and week numbers included in the file data.

    Inputs:
    - filename: string, name of the .csv file to be read

    Returns a tuple: month (integer), year (integer), weeks (list)
    """

    pass
