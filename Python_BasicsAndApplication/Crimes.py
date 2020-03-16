import csv
import re

counter = {}
count = 0
with open(r'C:\Users\Aleksandr\PycharmProjects\stepik1\Crimes.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if re.search(r'\d*/\d*/(\d{4})',row["Date"]).group(1) == '2015':
            if counter.__contains__(row["Primary Type"]):
                counter[row["Primary Type"]] += 1
            else:
                counter[row["Primary Type"]] = 0
    crimes_names = ""
    for k,v in counter.items():
        if v > count:
            count = v
            crimes_names = k
print(crimes_names)