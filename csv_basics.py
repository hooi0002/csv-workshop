"""CSV Utilities for PyBay Project Night CSV workshop.

This code demonstrates how the csv python standard library can be used to obtain
data from csv files.
"""

import csv


def print_csv_data(filename):
    """Prints data from a .csv file.

    Inputs:
    - filename: string, name of the .csv file to be read

    Returns None.
    """

    with open(filename, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            print(', '.join(row))
    csv_file.close()


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
    print_csv_data('prices.csv')
    write_to_csv('test.csv', [['a', 1], ['b', 2], ['c', 3], ['d', 4]])