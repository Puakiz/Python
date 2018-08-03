import csv

# Get high temperatures from file.
filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs = []
    for row in reader:
        highs.append(row[1])

    print(highs)
