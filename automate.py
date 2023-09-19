import sys
import csv
import eightpuzzle 
import search
if __name__ == '__main__':
    filename1 = "scenarios.csv"
    filename2 = "results.csv"
    # f2 = open(filename2, 'w', newline='')
    # header = "H3 results"
    with open(filename1, mode='r')as file:

        # reading the CSV file
        csvReader = csv.reader(file)
        count = 0
        # displaying the contents of the CSV file
        # writer = csv.writer(f2)
        # writer.writerow(header)
        average = 0
        for lines in csvReader:
            puzzle_list = list(map(lambda n: int(n), lines))
            puzzle = eightpuzzle.EightPuzzleState(list(puzzle_list))
            problem = eightpuzzle.EightPuzzleSearchProblem(puzzle)
            results = search.aStarSearch(problem, search.H1)
            average += results[2]
            count +=1
        
            # writer.writerow(list(results))
    
    
    # f2.close()
    print(average/count)
    




            
            
