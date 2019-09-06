import csv
import random
import time
import math

t = 0
periodic_func = 0

fieldnames = ["t", "periodic_func"]

with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while True:

    with open('data.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        info = {
            "t": t,
            "periodic_func": periodic_func
        }

        csv_writer.writerow(info)
        print(t, periodic_func)

        a = 5 * math.sin(2 * (math.pi) * t)
        periodic_func = 3 * (math.pi) * (math.exp(-a))
        t += 1

    time.sleep(0.1)
