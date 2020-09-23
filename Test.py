import csv
def read_csv_fieldnames (filename, separator, quote):
    with open(filename, newline='') as file:
        spamreader = csv.reader(file, delimiter=separator, quotechar=quote)
        for row in spamreader:
            return row
            break
def read_csv_as_list_dict (filename, separator, quote):
    table = []
    with open(filename, "rt", newline='') as file:
        input_file = csv.DictReader(file, delimiter=separator, quotechar=quote)
        for row in input_file:
            table.append(row)
    return table
def read_csv_as_nested_dict (filename, keyfield, separator, quote):
    table = {}
    with open(filename, "rt", newline='') as file:
        reader = csv.DictReader(file, delimiter=separator, quotechar=quote)
        for row in reader:
            table[row[keyfield]] = row
    return table
