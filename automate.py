import sys
import csv
import eightpuzzle 
import search
import math
from tabulate import tabulate


if __name__ == '__main__':
    filename1 = "scenarios.csv"
    header = ["depth", "expanded_nodes", "max_fringe_size", "branching factor"]
    table_1 = []
    table_1.append(["H1 RESULTS"])
    table_1.append(header)
    table_2 = []
    table_2.append(["H2 RESULTS"])
    table_2.append(header)
    table_3 = []
    table_3.append(["H3 RESULTS"])
    table_3.append(header)
    table_4 = []
    table_4.append(["H4 RESULTS"])
    table_4.append(header)
    with open(filename1, mode='r')as file:
        csvReader = csv.reader(file)
        count = 0
        average_1 = [0,0,0,0]
        average_2 = [0,0,0,0]
        average_3 = [0,0,0,0]
        average_4 = [0,0,0,0]
        for lines in csvReader:
            puzzle_list = list(map(lambda n: int(n), lines))
            puzzle = eightpuzzle.EightPuzzleState(list(puzzle_list))
            problem = eightpuzzle.EightPuzzleSearchProblem(puzzle)
            results = search.aStarSearch(problem, search.H1)
            average_1[0] += results[0]
            average_1[1] += results[1]
            average_1[2] += results[2]
            average_1[3] += results[3]
            table_1.append(results)
            results = search.aStarSearch(problem, search.H2)
            average_2[0] += results[0]
            average_2[1] += results[1]
            average_2[2] += results[2]
            average_2[3] += results[3]
            table_2.append(results)
            results = search.aStarSearch(problem, search.H3)
            average_3[0] += results[0]
            average_3[1] += results[1]
            average_3[2] += results[2]
            average_3[3] += results[3]
            table_3.append(results)
            results = search.aStarSearch(problem, search.H4)
            average_4[0] += results[0]
            average_4[1] += results[1]
            average_4[2] += results[2]
            average_4[3] += results[3]

            table_4.append(results)
            
            count +=1
            
    # f2.close()
    table_1.append(["average depth","average expanded nodes", "average fringe size"])
    table_1.append([average_1[0]/count, average_1[1]/count, average_1[2]/count, round(average_1[3]/count,3)])
    #print(tabulate(table_1, headers=header,tablefmt="github"))
    table_2.append(["average depth","average expanded nodes", "average fringe size"])
    table_2.append([average_2[0]/count, average_2[1]/count, average_2[2]/count, round(average_2[3]/count,3)])
    #print(tabulate(table_2, headers=header,tablefmt="github"))
    table_3.append(["average depth","average expanded nodes", "average fringe size"])
    table_3.append([average_3[0]/count, average_3[1]/count, average_3[2]/count,round(average_3[3]/count,3)])
    #print(tabulate(table_3, headers=header,tablefmt="github"))
    table_4.append(["average depth","average expanded nodes", "average fringe size"])
    table_4.append([average_4[0]/count, average_4[1]/count, average_4[2]/count, round(average_4[3]/count,3)])
    #print(tabulate(table_4,headers=header,tablefmt="github"))
    
    with open("results.csv", mode='w', newline='') as results_file:
        results_writer = csv.writer(results_file)
        
        results_writer.writerows(table_1)
        
        results_writer.writerows(table_2)
        
        results_writer.writerows(table_3)
        
        results_writer.writerows(table_4)

    




            
            
