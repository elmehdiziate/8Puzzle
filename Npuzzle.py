import searchN
import math
class NpuzzleState:
    
    
    def __init__( self, numbers ):
        

        self.cells = []
        self.dimension = int(math.sqrt(len(numbers)))
        numbers = numbers[:] # Make a copy so as not to cause side-effects.
        numbers.reverse()
        for row in range(self.dimension):
            self.cells.append( [] )
            for col in range(self.dimension):
                self.cells[row].append( numbers.pop() )
                if self.cells[row][col] == 0:
                    self.blankLocation = row, col
    
    def isGoal(self):
        
        current = 0
        for row in range(self.dimension):
            for col in range(self.dimension):
                if self.cells[row][col] != current:
                    return False
                current +=1
        return True
    
    def legalMoves(self):
        moves = []
        row, col = self.blankLocation
        if(row != 0):
            moves.append('up')
        if(row != (self.dimension - 1)):
            moves.append('down')
        if(col != 0):
            moves.append('left')
        if(col != (self.dimension-1)):
            moves.append('right')
        return moves
    
    def result(self, move):
        row, col = self.blankLocation
        if(move == 'up'):
            newrow = row - 1
            newcol = col
        elif(move == 'down'):
            newrow = row + 1
            newcol = col
        elif(move == 'right'):
            newrow = row
            newcol = col + 1
        elif(move == 'left'):
            newrow = row
            newcol = col - 1
        else:
            raise "Illegal Move"

        # Create a copy of the current eightPuzzle
        zeros_list = [0 for _ in range(self.dimension**2)]
        newPuzzle = NpuzzleState(zeros_list)
        newPuzzle.cells = [values[:] for values in self.cells]
        # And update it to reflect the move
        newPuzzle.cells[row][col] = self.cells[newrow][newcol] # move the number to the blank space, swap
        newPuzzle.cells[newrow][newcol] = self.cells[row][col] # move the blank space to the number
        newPuzzle.blankLocation = newrow, newcol

        return newPuzzle
    
    
    def __eq__(self, other):
        for row in range(self.dimension):
            if self.cells[row] != other.cells[row]:
                return False
        return True
    
    def __hash__(self):
        return hash(str(self.cells)) # Hashable so it can be used in a set
    
    def __getAsciiString(self):
        """
        Returns a display string for the maze with specified dimension n x n
        """
        lines = []
        n = self.dimension
        horizontalLine = ('-' * (4 * n + 1))  # Adjusted for n
        lines.append(horizontalLine)

        for row in self.cells:
            rowLine = '|'
            for col in row:
                if col == 0:
                    col = ' '
                
                    rowLine = rowLine + f' {col} |'
                elif(int(col) >= 10 and int(col) <100):
                    rowLine = rowLine + f'{col} |'
                elif(int(col)>= 100):
                    rowLine = rowLine + f'{col}|'
                else:
                    rowLine = rowLine + f' {col} |'
            lines.append(rowLine)
            lines.append(horizontalLine)

        return '\n'.join(lines)


    def __str__(self):
        return self.__getAsciiString()

class NPuzzleSearchProblem(searchN.SearchProblem):
    """
      Implementation of a SearchProblem for the  Eight Puzzle domain

      Each state is represented by an instance of an eightPuzzle.
    """
    def __init__(self,puzzle):
        "Creates a new EightPuzzleSearchProblem which stores search information."
        self.puzzle = puzzle

    def getStartState(self):
        return self.puzzle

    def isGoalState(self,state):
        return state.isGoal()

    def getSuccessors(self,state):
        """
          Returns list of (successor, action, stepCost) pairs where
          each succesor is either left, right, up, or down
          from the original state and the cost is 1.0 for each
        """
        succ = []
        for a in state.legalMoves():
            succ.append((state.result(a), a, 1))
        return succ

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        return len(actions)


    
# # ten_list = [i for i in range(11**2)]
# puzzle = NpuzzleState(ten_list)

# print(puzzle)

if __name__ == '__main__':
    # puzzle = createRandomEightPuzzle(25)
    puzzle = NpuzzleState([1,0,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
    print('A random puzzle:')
    print(puzzle)

    problem = NPuzzleSearchProblem(puzzle)
    #path= search.aStarSearch(problem, search.H4)
    path= searchN.astar(problem, searchN.H3)    
    print(path)