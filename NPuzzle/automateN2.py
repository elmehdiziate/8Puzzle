"""/*=====Start Change Task 4=====*/"""
import sys
import csv
import Npuzzle 
import searchN
import math
from tabulate import tabulate


if __name__ == '__main__':
    filename1 = "scenariosN.csv"
    header = ["depth", "expanded_nodes", "max_fringe_size"]
    table_1 = []
    table_1.append(["bfs RESULTS"])
    table_1.append(header)
    table_2 = []
    table_2.append(["UCS RESULTS"])
    table_2.append(header)
    table_4 = []
    table_4.append(["DFS RESULTS"])
    table_4.append(header)


    with open(filename1, mode='r')as file:#read the file
        csvReader = csv.reader(file)
        count = 0
        dfs_count = 0
        average_1 = [0,0,0]
        average_2 = [0,0,0]
        average_4 = [0,0,0]
        for lines in csvReader:
            puzzle_list = list(map(lambda n: int(n), lines))#convert the string to int
            puzzle = Npuzzle.NpuzzleState(list(puzzle_list))#create a puzzle
            problem = Npuzzle.NPuzzleSearchProblem(puzzle)#create a problem
            print("BFS",count)
            results = searchN.bfs(problem)#search the problem with bfs
            average_1[0] += results[0]
            average_1[1] += results[1]
            average_1[2] += results[2]
            table_1.append(results)
            print("UCS",count)
            results = searchN.ucs(problem)#search the problem with ucs
            average_2[0] += results[0]
            average_2[1] += results[1]
            average_2[2] += results[2]
            table_2.append(results)
            print("DFS",count)
            results = searchN.dfs(problem)#search the problem with dfs
            if(results != None):#if the puzzle is solvable with dfs then add the results to the table 
                average_4[0] += results[0]
                average_4[1] += results[1]
                average_4[2] += results[2]
                table_4.append(results)
                dfs_count += 1
            else:
                table_4.append([0,0,0])
            count +=1
            
    table_1.append(["average depth","average expanded nodes", "average fringe size"])
    table_1.append([average_1[0]/count, average_1[1]/count, average_1[2]/count])#add the average results to the table
    table_2.append(["average depth","average expanded nodes", "average fringe size"])
    table_2.append([average_2[0]/count, average_2[1]/count, average_2[2]/count])
    table_4.append(["average depth","average expanded nodes", "average fringe size"])
    table_4.append([average_4[0]/dfs_count, average_4[1]/dfs_count, average_4[2]/dfs_count])
    with open("results2N.csv", mode='w', newline='') as results_file:#write the results to a file
        results_writer = csv.writer(results_file)
        
        results_writer.writerows(table_1)
        
        results_writer.writerows(table_2)
        
        
        results_writer.writerows(table_4)

"""/*=====End Change Task 4=====*/"""

    




            
            
