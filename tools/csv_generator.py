"""CSV Generator for PyBay Project Night CSV workshop.

This code generates a csv file with sample monthly cupcake sales data.
Each line in the resulting file has the data: date, order number, item
"""

import csv
import csv_utils
import datetime
import math
import random


flavors = ['chocolate', 'green tea', 'lemon', 'red velvet', 'tuxedo', 'vanilla']

def make_monthly_data(days, month, year, choices):
    """
    Makes CSV file with monthly sales data.

    Inputs:
    - days: int, number of days in the month
    - month: int, specified as an integer 1-12
    - year: int, specified with four digits
    - choices: list, options for items purchased in a given order 

    Returns a nested list. 
    - Inner list: [date (str), order number (int), item (str)]
    """
    data = []
    order_no = 1
    for i in range(1, days + 1):
        date = datetime.date(year, month, i)
        num_sales = random.randint(1, 30)
        for j in range(1, num_sales + 1):
            num_items = math.floor(max(1, random.gauss(5, 5)))
            for k in range(1, num_items + 1):
                item = random.choice(choices)
                line = [date.strftime('%m/%d/%Y'), order_no, item]
                data.append(line)
            order_no += 1
    return data

if __name__ == '__main__':
    sales_data = make_monthly_data(31, 5, 2018, flavors)
    csv_utils.write_to_csv('cupcakes.csv', sales_data)