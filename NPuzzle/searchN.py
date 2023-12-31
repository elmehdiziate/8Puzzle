"""/*=====Start Change Task 4=====*/"""

import math
import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined() #raise exception if code not implemented

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined() 

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()

def Branching_factor(depth, num_expandedNodes):

    if (depth == 0):
        return 'ERROR'
    b = round(math.pow(num_expandedNodes,(1/depth)),3)

    return b

def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """Search the deepest nodes in the search tree first."""

    #states to be explored (LIFO). holds nodes in form (state, action)
    frontier = util.Stack()
    #previously explored states (for path checking), holds states
    exploredNodes = []
    expanded_nodes = 0
    maxDepth = 0
    max_Fringe_size = 0
    #define start node
    startState = problem.getStartState()
    startNode = (startState, []) 
    
    frontier.push(startNode)
    
    while not frontier.isEmpty():
        #begin exploring last (most-recently-pushed) node on frontier
        currentState, actions = frontier.pop()
        
        if currentState not in exploredNodes:
            #mark current node as explored
            exploredNodes.append(currentState)
            expanded_nodes +=1

            if problem.isGoalState(currentState):

                return maxDepth, expanded_nodes, max_Fringe_size
            else:
                #get list of possible successor nodes in 
                #form (successor, action, stepCost)
                successors = problem.getSuccessors(currentState)
                
                #push each successor to frontier
                for succState, succAction, succCost in successors:
                    newAction = actions + [succAction]
                    newNode = (succState, newAction)
                    frontier.push(newNode)
                    max_Fringe_size = max(max_Fringe_size, len(frontier.list))

    return maxDepth, expanded_nodes, max_Fringe_size  

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""

    #to be explored (FIFO)
    frontier = util.Queue()
    
    #previously expanded states (for cycle checking), holds states
    exploredNodes = []
    depth = 0
    expanded_nodes = 0
    max_fringe_size = 0
    
    startState = problem.getStartState()
    startNode = (startState, [], 0) #(state, action, cost)
    
    frontier.push(startNode)
    
    while not frontier.isEmpty():
        #begin exploring first (earliest-pushed) node on frontier
        currentState, actions, currentCost = frontier.pop()
        depth = max(depth, len(actions))
        
        if currentState not in exploredNodes:
            #put popped node state into explored list
            exploredNodes.append(currentState)
            expanded_nodes += 1
            if problem.isGoalState(currentState):
                return depth, expanded_nodes, max_fringe_size
            else:
                #list of (successor, action, stepCost)
                successors = problem.getSuccessors(currentState)
                
                for succState, succAction, succCost in successors:
                    newAction = actions + [succAction]
                    newCost = currentCost + succCost
                    newNode = (succState, newAction, newCost)

                    frontier.push(newNode)
                    expanded_nodes = len(exploredNodes)
                    max_fringe_size = max(max_fringe_size, len(frontier.list))


    return depth, expanded_nodes, max_fringe_size

        
def uniformCostSearch(problem):
    """Search the node of least total cost first."""

    #to be explored (FIFO): holds (item, cost)
    frontier = util.PriorityQueue()
    depth = 0
    #previously expanded states (for cycle checking), holds state:cost
    exploredNodes = {}
    
    startState = problem.getStartState()
    startNode = (startState, [], 0) #(state, action, cost)
    max_fringe_size = 0
    frontier.push(startNode, 0)
    
    while not frontier.isEmpty():
        #begin exploring first (lowest-cost) node on frontier
        currentState, actions, currentCost = frontier.pop()
        depth = max(depth, len(actions))
        if (currentState not in exploredNodes) or (currentCost < exploredNodes[currentState]):
            #put popped node's state into explored list
            exploredNodes[currentState] = currentCost

            if problem.isGoalState(currentState):
                return depth, len(exploredNodes), max_fringe_size
            else:
                #list of (successor, action, stepCost)
                successors = problem.getSuccessors(currentState)
                
                for succState, succAction, succCost in successors:
                    newAction = actions + [succAction]
                    newCost = currentCost + succCost
                    newNode = (succState, newAction, newCost)
                    max_fringe_size = max(max_fringe_size, len(frontier.heap))
                    frontier.update(newNode, newCost)

    return depth, len(exploredNodes), max_fringe_size

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

    

def H4(state, goal_state,dimension):#  heuristic 4
    outofrows = 0
    outofcols = 0
    x = 0
    for row in state.cells:
        y = 0
        for n in row:
            if n != 0:
                x1 = int(n/dimension)
                y1 = goal_state[x1].index(n)#find the index of the number in the goal state
                if x1 != x:
                    outofrows +=1
                if y1 != y:
                    outofcols +=1
            y +=1
        x +=1
    return outofcols + outofrows

def H3(state, goal_state, dimesion):#heuristic 3
  x=0
  distance = 0
  for row in state.cells:
      y=0
      for n in row:
          if n != 0:
            x1 = int(n/dimesion)#find the row of the number in the goal state
            y1 = goal_state[x1].index(n)
            distance += util.manhattanDistance((x,y), (x1,y1))
          y = y+1
      x = x+1
  return distance

def H2(state, goal_state, dimension):#heuristic 2
    x=0
    distance = 0
    for row in state.cells:
        y=0
        for n in row:
            if n != 0:
                x1 = int(n/dimension)
                y1 = goal_state[x1].index(n)#find the index of the number in the goal state
                distance += math.sqrt((x -x1)**2 + (y - y1)**2)
            y = y+1
        x = x+1
    return distance

def H1(state, goal_state, dimesion): #heuristic 1
    state_list = flattern(state.cells)
    problem_list = flattern(goal_state)
    # print(state_list)
    count = 0
    zipped_list = zip(state_list,problem_list)
    for t in zipped_list:
        if t[0] != t[1]:
            count = count + 1
    # print(count)
    return count
    
def flattern(state):
    flattern_list = []
    for row in state:
        for n in row:
            flattern_list.append(n)
    return flattern_list


def generate_goal_state(problem):#generate goal state for heuristic 
    goal_state = []
    current = 0
    for row in range(problem.puzzle.dimension):
        goal_state.append([])
        for col in range(problem.puzzle.dimension):
            goal_state[row].append(current)
            current += 1
    return goal_state
        
def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    goal_state = generate_goal_state(problem)#generate goal state
    #to be explored (FIFO): takes in item, cost+heuristic
    frontier = util.PriorityQueue()
    max_frontier_size = 0
    exploredNodes = [] #holds (state, cost)
    depth = 0  # Initialize depth
    expanded_nodes = 0  # Initialize expanded nodes count
    max_fringe_size = 0  # Initialize max fringe size

    startState = problem.getStartState()
    startNode = (startState, [], 0) #(state, action, cost)
    count = 0
    frontier.push(startNode, 0)

    while not frontier.isEmpty():
        #max_frontier_size = max(max_frontier_size, frontier.count - count)
        #begin exploring first (lowest-combined (cost+heuristic) ) node on frontier
        currentState, actions, currentCost = frontier.pop()
        #count+=1

        #put popped node into explored list
        currentNode = (currentState, currentCost)
        exploredNodes.append((currentState, currentCost))
        depth = max(depth, len(actions))  # Update depth
        expanded_nodes += 1  # Increment expanded nodes count
        if problem.isGoalState(currentState):
            b_factor = Branching_factor(depth, expanded_nodes)
            # return depth, expanded_nodes, max_fringe_size, b_factor
            return depth, expanded_nodes, max_fringe_size, b_factor

        else:
            #list of (successor, action, stepCost)
            successors = problem.getSuccessors(currentState)

            #examine each successor
            for succState, succAction, succCost in successors:
                newAction = actions + [succAction]
                newCost = problem.getCostOfActions(newAction)
                newNode = (succState, newAction, newCost)

                #check if this successor has been explored
                already_explored = False
                for explored in exploredNodes:
                    #examine each explored node tuple
                    exploredState, exploredCost = explored

                    if (succState == exploredState) and (newCost >= exploredCost):
                        already_explored = True

                #if this successor not explored, put on frontier and explored list
                if not already_explored:
                    dimension = problem.puzzle.dimension
                    frontier.push(newNode, newCost + heuristic(succState, goal_state,dimension))
                    exploredNodes.append((succState, newCost))
                    max_fringe_size = max(max_fringe_size, len(frontier.heap))

                b_factor = Branching_factor(depth, expanded_nodes)    
    # return depth, expanded_nodes, max_fringe_size, b_factor
    return depth, expanded_nodes, max_fringe_size, b_factor

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
"""/*=====End Change Task 4=====*/"""

