import sys
import csv
from itertools import permutations
if __name__ == '__main__':
    numbers = [0,1,2,3,4,5,6,7,8]
    filename = "permutations.csv"
    f = open(filename, 'w', newline='')
    writer = csv.writer(f)
    all_permutaions = permutations(numbers)
    
    for row in all_permutaions:
        writer.writerow(list(row))

    