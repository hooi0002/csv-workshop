"""CSV Generator for PyBay Project Night CSV workshop.

This code generates a .csv file with sample monthly cupcake sales data.

The output file has the fields:
 date,order number,item
"""

import csv
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
            num_items = int(math.floor(max(1, random.gauss(5, 5))))
            for k in range(1, num_items + 1):
                item = random.choice(choices)
                line = [date.strftime('%m/%d/%Y'), order_no, item]
                data.append(line)
            order_no += 1
    return data

def write_to_csv(filename, data):
    """Writes data to a .csv file.

    Inputs:
    - filename: string, name of the .csv file where data will be written to.
    - data: iterable, each item will be written to a line in the file.

    Returns None.
    """

    with open(filename, 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(data)
    csv_file.close()

if __name__ == '__main__':
    sales_data = make_monthly_data(31, 5, 2018, flavors)
    write_to_csv('cupcakes1.csv', sales_data)
