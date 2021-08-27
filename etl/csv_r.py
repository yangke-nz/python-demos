import csv
with open('./csv-sample.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))
    for i in data:
        print(i)