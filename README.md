# csv-workshop
Workshop exercises to learn the csv python standard library
(created for SF Python Project Night)

## Goals
The goal of this workshop is to learn how to read data from a .csv file,
manipulate the data in interesting ways, and write data to a .csv file. With
these skills, we can automate boring tasks, like data entry. By using Python to
examine the data, we can go beyond the analytical power of spreadsheet editors, 
freely exploring it for insights.

## Tools
To read from and write to .csv files, we'll use the csv module. Because our 
sample data involves dates, we'll also be using the datetime module. Both
modules are part of the Python standard library.

## Sample Data
The main file we'll be working with is cupcakes.csv. This file contains 
information about monthly cupcake sales. Each line in the file is a record of
sale for an individual cupcake, which may be part of a larger order. 

The fields of cupcakes.csv are as follows: date,order number,flavor

The prices.csv file contains information about the price of cupcakes by flavor.
Using the data in this file, we will create a dictionary to lookup cupcake
pricing.

The fields of prices.csv are as follows: flavor,price
