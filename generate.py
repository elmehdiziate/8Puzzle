import sys
import csv
from itertools import permutations
import eightpuzzle as E
if __name__ == '__main__':
    numbers = [0,1,2,3,4,5,6,7,8]
    filename = "permutations.csv"
    f = open(filename, 'w', newline='')
    writer = csv.writer(f)
    all_permutaions = permutations(numbers)
    
    for row in all_permutaions:
        writer.writerow(list(row))
    # filename = "scenarios.csv"
    # f = open(filename,'w', newline='')
    # writer = csv.writer(f)
    
    # for i in range(20):
    #     puzzle = E.createRandomEightPuzzle(25)
    #     puzzle_list = []
    #     for i in puzzle.cells:
    #         for j in i:
    #             puzzle_list.append(j)
    #     writer.writerow(puzzle_list)            
    
        

    