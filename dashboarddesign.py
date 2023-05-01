import csv
with open("adressen.csv") as csvdatei:
    csv_reader_object = csv.reader(csvdatei)
    for row in csv_reader_object:
        print(row)