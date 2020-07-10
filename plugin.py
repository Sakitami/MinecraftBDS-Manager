import csv
import numpy as np

def Plugin_Depo_Read(Repo=None):
    with open('Plugin.csv','r') as csvfile:
        reader = csv.reader(csvfile)
        rows= [row for row in reader]
        rows.remove(rows[0])
        return rows

if __name__ == "__main__":
    print(Plugin_Depo_Read())