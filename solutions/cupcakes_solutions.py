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


def prices_to_dict(filename):
    """Makes a dictionary from a .csv file data.

    The input .csv file should have exactly two fields: flavor, price 
    Hint: Try using csv.DictReader.

    Inputs:
    - filename: string, name of the .csv file to be read

    Returns a dictionary.
    """

    prices = {}
    fieldnames = ['flavor', 'price']
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
    - filename: string, name of the .csv file to be read
    - prices: dictionary, where the keys are cupcake flavors (strings) and the
              values are the corresponding cupcake prices (floats)

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


def get_weekly_sales(filename, wk_num):
    """Determine number of sales transactions for a given week in the year.

    Hint: Use the datetime module to parse date strings.

    Inputs:
    - filename: string, name of the .csv file to be read
    - wk_num: integer, number of week in year

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


def get_most_popular_day_of_week(filename):
    """Determine most popular day of the week to buy cupcakes.

    Inputs:
    - filename: string, name of the .csv file to be read

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
    
    counts = {}
    with open(infile, 'r') as csv_file:
        reader = csv.reader(csv_file)
        flavors = set()
        for row in reader:
            date, order_num, flavor = row
            order_num = int(order_num)
            counts[order_num] = counts.get(order_num, {})
            counts[order_num][flavor] = counts[order_num].get(flavor, 0) + 1
            counts[order_num]['date'] = counts[order_num].get('date', date)
            flavors.add(flavor)
    csv_file.close()
    
    with open(outfile, 'w') as csv_file:
        fieldnames = ['date', 'order'] + sorted(list(flavors))
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        sorted_orders = sorted(list(counts.keys()))
        for order_num in sorted_orders:
            order_data = counts[order_num]
            order_data['order'] = order_num
            for flavor in flavors:
                order_data[flavor] = order_data.get(flavor, 0)
            writer.writerow(order_data)

    csv_file.close()
    print('Data from {} was tabulated and written to {}.'.format(infile, outfile))


def get_month_info(filename):
    """Determine the month, year, and week numbers included in the file data.

    Inputs:
    - filename: string, name of the .csv file to be read

    Returns a tuple: month (integer), year (integer), weeks (list)
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


def print_monthly_sales_report(filename, prices):
    """Prints information about sales for a given month.

    Inputs:
    - filename: string, name of the .csv file to be read
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
    prices = prices_to_dict('prices.csv')
    print_monthly_sales_report('cupcakes.csv', prices)
    tabulate_data('cupcakes.csv', 'cupcakes_tabular.csv')
