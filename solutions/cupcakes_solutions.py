"""Solutions to PyBay Project Night CSV workshop.

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

    with open(filename, 'r') as csv_file:
        reader = csv.reader(csv_file)
        datestamp, order_num, flavor = next(reader)
        date = datetime.datetime.strptime(datestamp, '%m/%d/%Y')
        month = date.strftime('%B')
        year = date.strftime('%Y')
        week = date.strftime('%V')
        weeks = set([int(week)])
        for row in reader:
            datestamp, order_num, flavor = row
            date = datetime.datetime.strptime(datestamp, '%m/%d/%Y')
            week = date.strftime('%V')
            weeks.add(int(week))
    csv_file.close()
    weeks = sorted(list(weeks))
    return (month, year, weeks)


def get_most_popular_flavor(filename):
    """Determine most popular cupcake flavor.

    Inputs:
    - filename: str, name of file to be read

    Returns a string.
    """
    
    counts = {}
    with open(filename, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            date, order_num, flavor = row
            counts[flavor] = counts.get(flavor, 0) + 1
    csv_file.close()
    
    most_sold = 0
    most_popular_flavor = None
    
    for flavor, num_sold in counts.items():
        if num_sold > most_sold:
            most_sold = num_sold
            most_popular_flavor = flavor
    
    return most_popular_flavor


def get_weekly_sales(filename, wk_num):
    """Determine number of transactions for a given week in the year.

    Inputs:
    - filename: str, name of file to be read
    - wk_num: int, number of week in year

    Returns an integer.
    """
    
    with open(filename, 'r') as csv_file:
        reader = csv.reader(csv_file)
        num_sales = 0
        for row in reader:
            datestamp, order_num, flavor = row
            date = datetime.datetime.strptime(datestamp, '%m/%d/%Y')
            week_in_year = int(date.strftime('%V'))
            if week_in_year == wk_num:
                num_sales += 1
    csv_file.close()

    return num_sales


def prices_to_dict(filename, fieldnames):
    """Makes a dictionary from a CSV file data.

    Inputs:
    - filename: string, name of the csv file to be read
    - fieldnames: list of field names in the file (expects list with two fields)

    Returns a dictionary.
    """
    
    prices = {}
    with open(filename, 'r') as csv_file:
        reader = csv.DictReader(csv_file, fieldnames=fieldnames)
        for row in reader:
            key = row[fieldnames[0]] # flavor
            value = row[fieldnames[1]] # price
            prices[key] = value
    csv_file.close()
    return prices


def get_gross_income(filename, prices):
    """Determine gross income from cupcake sales.
    
    Inputs:
    - filename: string, name of the csv file to be read
    - prices: dictionary, keys are strings, values are floats

    Returns a float.
    """
    
    gross_income = 0
    with open(filename, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            date, order_num, flavor = row
            gross_income += float(prices[flavor])
    csv_file.close()

    return gross_income


def get_most_popular_day_of_week(filename):
    """Determine most popular day of the week to buy cupcakes.

    Inputs:
        - filename: string, name of the csv file to be read

    Returns a string.  
    """
    
    counts = {}
    with open(filename, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            datestamp, order_num, flavor = row
            date = datetime.datetime.strptime(datestamp, '%m/%d/%Y')
            day_of_week = date.strftime('%A')
            counts[day_of_week] = counts.get(day_of_week, 0) + 1
    csv_file.close()

    most_sold = 0
    most_popular_day_of_week = None
    
    for day_of_week, num_sold in counts.items():
        if num_sold > most_sold:
            most_sold = num_sold
            most_popular_day_of_week = day_of_week
    
    return most_popular_day_of_week


def transform_data(infile, outfile):
    """Transform sales data and write to file.

    Inputs:
    - infile: string, name of the csv file to be read
    - outfile: string, name of the csv file where data will be written

    Returns None.
    """
    
    counts = {}
    with open(infile, 'r') as csv_file:
        reader = csv.reader(csv_file)
        flavors = set()
        for row in reader:
            date, order_num, flavor = row
            counts[order_num] = counts.get(order_num, {})
            counts[order_num][flavor] = counts[order_num].get(flavor, 0) + 1
            flavors.add(flavor)
    csv_file.close()
    
    with open(outfile, 'w') as csv_file:
        fieldnames = ['order'] + sorted(list(flavors))
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for order, tally in counts.items():
            tally['order'] = order
            for flavor in flavors:
                tally[flavor] = tally.get(flavor, 0)
            writer.writerow(tally)

    csv_file.close()
    print('Data from {} was transformed and written to {}.'.format(infile, outfile))


def generate_monthly_sales_report(filename, prices):
    """Prints information about sales for a given month.

    Inputs:
    - filename: string, name of the csv file to be read
    - prices: dictionary, keys are strings, values are floats

    Returns None.
    """

    month, year, weeks = get_month_info(filename)
    gross_income = get_gross_income(filename, prices)
    most_popular_flavor = get_most_popular_flavor(filename)
    most_popular_day_of_week = get_most_popular_day_of_week(filename)
    
    print('-- {} {} cupcake sales report --'.format(month, year))
    print('* Gross income: ${:,.2f}'.format(gross_income))
    print('* Most popular flavor sold: {}'.format(most_popular_flavor))
    print('* Most popular day of the week to buy cupcakes: {}'
          .format(most_popular_day_of_week))
    print('* Weekly sales breakdown:')
    for week in weeks:
        weekly_sales = get_weekly_sales(filename, week)
        print('  - Week {}: {} cupcakes sold'.format(week, weekly_sales))


if __name__ == '__main__':
    prices = prices_to_dict('prices.csv',['flavor', 'price'])
    generate_monthly_sales_report('cupcakes.csv', prices)
    transform_data('cupcakes.csv', 'cupcakes_matrix.csv')