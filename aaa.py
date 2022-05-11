import csv
with open("data-398-2018-08-30.csv", encoding="utf-8") as csv_file:
    reader = csv.DictReader(csv_file)
    total = []
    for row in reader:
        total.append(row)
        print(row["Name"], row["Street"], row["District"])
        print(len(total))
