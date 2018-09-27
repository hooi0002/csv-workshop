import csv

# open in read-only mode
def read_csv(fname):
    with open(fname, 'r') as csv_file:
        
        # can be opened with reader or DictReader
        reader = csv.reader(csv_file)
        # reader = csv.DictReader(csv_file)
        
        for row in reader:

            # for rows in reader
            print(', '.join(row))
            
            # for rows in DictReader
            # print(row['date of purchase'], row['order number'], row['flavor'])

    csv_file.close()


def write_csv(fname):
    with open(fname, 'w+') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['cupcake'] * 5 + ['muffin'])
    csv_file.close()


if __name__ == '__main__':
    read_csv('cupcakes.csv')
    write_csv('foo.csv')
