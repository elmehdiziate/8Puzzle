"""/*=====Start Change Task 4=====*/"""
import csv
import random

def getInvCount(arr): #count the number of inversions in the puzzle
    inv_count = 0
    empty_value = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] != empty_value and arr[i] != empty_value and arr[i] > arr[j]:
                inv_count += 1
    return inv_count

def isSolvable(puzzle):  # check if the puzzle is solvable
    inv_count = getInvCount([j for sub in puzzle for j in sub])
    return (inv_count % 2 == 0)

def createRandomPuzzle(n): #create a random puzzle
    puzzle = [[j for j in range(i*n+1, (i+1)*n+1)] for i in range(n)]
    puzzle[-1][-1] = 0
    random.shuffle([j for sub in puzzle for j in sub])
    return puzzle

if __name__ == '__main__':
    filename = "scenariosN.csv"
    f = open(filename,'w', newline='')
    writer = csv.writer(f)
    count = 0
    while count != 12:  # Generate 12 puzzles
        n = random.randint(4, 8)  # Generate a random n between 4 and 8 (inclusive)
        puzzle = createRandomPuzzle(n)
        if isSolvable(puzzle):
            puzzle_list = [j for sub in puzzle for j in sub]
            writer.writerow(puzzle_list) 
            count += 1   

f.close()
