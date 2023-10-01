import csv
import pandas as pd
import eightpuzzle
import search

if __name__ == '__main__':
    filename1 = "scenarios.csv"
    header = ["depth", "expanded_nodes", "max_fringe_size"]
    
    # Create lists to store results
    table_1 = [header]
    table_2 = [header]
    table_3 = [header]
    table_4 = [header]

    with open(filename1, mode='r') as file:
        csvReader = csv.reader(file)
        count = 0
        average_1 = [0, 0, 0]
        average_2 = [0, 0, 0]
        average_3 = [0, 0, 0]
        average_4 = [0, 0, 0]

        for lines in csvReader:
            puzzle_list = list(map(lambda n: int(n), lines))
            puzzle = eightpuzzle.EightPuzzleState(list(puzzle_list))
            problem = eightpuzzle.EightPuzzleSearchProblem(puzzle)

            # Perform A* search for different heuristics
            results = search.aStarSearch(problem, search.H1)
            average_1 = [a + b for a, b in zip(average_1, results)]
            table_1.append(results)

            results = search.aStarSearch(problem, search.H2)
            average_2 = [a + b for a, b in zip(average_2, results)]
            table_2.append(results)

            results = search.aStarSearch(problem, search.H3)
            average_3 = [a + b for a, b in zip(average_3, results)]
            table_3.append(results)

            results = search.aStarSearch(problem, search.H4)
            average_4 = [a + b for a, b in zip(average_4, results)]
            table_4.append(results)

            count += 1

    # Calculate average results
    average_1 = [a / count for a in average_1]
    average_2 = [a / count for a in average_2]
    average_3 = [a / count for a in average_3]
    average_4 = [a / count for a in average_4]

    # Create DataFrames
    df1 = pd.DataFrame(table_1)
    df2 = pd.DataFrame(table_2)
    df3 = pd.DataFrame(table_3)
    df4 = pd.DataFrame(table_4)

    # Create a Pandas Excel writer using XlsxWriter as the engine.
    with pd.ExcelWriter('results.xlsx', engine='xlsxwriter') as writer:
        # Write each DataFrame to a different sheet.
        df1.to_excel(writer, sheet_name='H1 RESULTS', index=False, header=None)
        pd.DataFrame([average_1]).to_excel(writer, sheet_name='H1 RESULTS', startrow=12, startcol=0, index=False, header=None)

        df2.to_excel(writer, sheet_name='H2 RESULTS', index=False, header=None)
        pd.DataFrame([average_2]).to_excel(writer, sheet_name='H2 RESULTS', startrow=12, startcol=0, index=False, header=None)

        df3.to_excel(writer, sheet_name='H3 RESULTS', index=False, header=None)
        pd.DataFrame([average_3]).to_excel(writer, sheet_name='H3 RESULTS', startrow=12, startcol=0, index=False, header=None)

        df4.to_excel(writer, sheet_name='H4 RESULTS', index=False, header=None)
        pd.DataFrame([average_4]).to_excel(writer, sheet_name='H4 RESULTS', startrow=12, startcol=0, index=False, header=None)
