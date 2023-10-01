import sys
import csv
import eightpuzzle 
import search
import math
from tabulate import tabulate


if __name__ == '__main__':
    filename1 = "scenarios.csv"
    header = ["depth", "expanded_nodes", "max_fringe_size"]
    table_1 = []
    table_1.append(["bfs RESULTS"])
    table_1.append(header)
    table_2 = []
    table_2.append(["UCS RESULTS"])
    table_2.append(header)
    table_3 = []
    table_3.append(["Deepening dfs RESULTS"])
    table_3.append(header)
    table_4 = []
    table_4.append(["dfs RESULTS"])
    table_4.append(header)


    with open(filename1, mode='r')as file:
        csvReader = csv.reader(file)
        count = 0
        average_1 = [0,0,0]
        average_2 = [0,0,0]
        average_3 = [0,0,0]
        average_4 = [0,0,0]
        for lines in csvReader:
            puzzle_list = list(map(lambda n: int(n), lines))
            puzzle = eightpuzzle.EightPuzzleState(list(puzzle_list))
            problem = eightpuzzle.EightPuzzleSearchProblem(puzzle)
            print("BFS",count)
            results = search.bfs(problem)
            average_1[0] += results[0]
            average_1[1] += results[1]
            average_1[2] += results[2]
            table_1.append(results)
            print("UCS",count)
            results = search.ucs(problem)
            average_2[0] += results[0]
            average_2[1] += results[1]
            average_2[2] += results[2]
            table_2.append(results)
            print("iterative deepening DFS",count)
            results = search.iterativeDeepeningDFS(problem)
            average_3[0] += results[0]
            average_3[1] += results[1]
            average_3[2] += results[2]
            table_3.append(results)
            print("DFS",count)
            results = search.dfs(problem)
            average_4[0] += results[0]
            average_4[1] += results[1]
            average_4[2] += results[2]
            table_4.append(results)
            count +=1
            
    table_1.append(["average depth","average expanded nodes", "average fringe size"])
    table_1.append([average_1[0]/count, average_1[1]/count, average_1[2]/count])
    table_2.append(["average depth","average expanded nodes", "average fringe size"])
    table_2.append([average_2[0]/count, average_2[1]/count, average_2[2]/count])
    table_3.append(["average depth","average expanded nodes", "average fringe size"])
    table_3.append([average_3[0]/count, average_3[1]/count, average_3[2]/count])
    table_4.append(["average depth","average expanded nodes", "average fringe size"])
    table_4.append([average_4[0]/count, average_4[1]/count, average_4[2]/count])
    with open("results2.csv", mode='w', newline='') as results_file:
        results_writer = csv.writer(results_file)
        
        results_writer.writerows(table_1)
        
        results_writer.writerows(table_2)
        
        results_writer.writerows(table_3)
        
        results_writer.writerows(table_4)
        

    




            
            
