"""/*=====Start Change Task 2=====*/"""
import sys
import csv
from itertools import permutations
import eightpuzzle as E
def getInvCount(arr): #count the number of inversions in the puzzle
    inv_count = 0
    empty_value = 0
    for i in range(0, 9):
        for j in range(i + 1, 9):
            if arr[j] != empty_value and arr[i] != empty_value and arr[i] > arr[j]:
                inv_count += 1
    return inv_count
 
     

def isSolvable(puzzle) :#check if the puzzle is solvable
    inv_count = getInvCount([j for sub in puzzle for j in sub])
    return (inv_count % 2 == 0)
if __name__ == '__main__':
    filename = "scenarios.csv"
    f = open(filename,'w', newline='')
    writer = csv.writer(f)
    count = 0
    while count != 500:
        puzzle = E.createRandomEightPuzzle(25) #create a random puzzle
        if(isSolvable(puzzle.cells)):
            puzzle_list = []
            for i in puzzle.cells:
                for j in i:
                    puzzle_list.append(j)
            writer.writerow(puzzle_list) 
            count+=1
    f.close()
"""/*=====End Change Task 2=====*/"""
       
    
        

    