# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, we implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

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
    """/*=====Start Change Task 3=====*/"""
    limit = 1000
    #states to be explored (LIFO). holds nodes in form (state, action)
    frontier = util.Stack()
    #previously explored states (for path checking), holds states
    exploredNodes = []
    expanded_nodes = 0
    maxDepth = 0
    max_Fringe_size = 0
    """/*=====End Change Task 3=====*/"""
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
            """/*=====Start Change Task 3=====*/"""
            expanded_nodes +=1
            """/*=====End Change Task 3=====*/"""
            if len(actions) > limit: #if depth limit reached
                return None
            if problem.isGoalState(currentState):
                
                return len(actions), len(exploredNodes), max_Fringe_size
            else:
                #get list of possible successor nodes in 
                #form (successor, action, stepCost)
                successors = problem.getSuccessors(currentState)
                
                #push each successor to frontier
                for succState, succAction, succCost in successors:
                    newAction = actions + [succAction]
                    newNode = (succState, newAction)
                    frontier.push(newNode)
                    """/*=====Start Change Task 3=====*/"""
                    max_Fringe_size = max(max_Fringe_size, len(frontier.list))
                    """/*=====Start Change Task 3=====*/"""

                    

    return len(actions), len(expanded_nodes), max_Fringe_size
"""/*=====Start Change Task 3=====*/"""
def iterativeDeepeningDFS(problem):
    max_depth = 0
    expanded_nodes = 0
    max_fringe_size = 0
    
    while True:
        result, nodes_expanded, fringe_size = depthLimitedSearch(problem, max_depth)
        expanded_nodes += nodes_expanded
        max_fringe_size = max(max_fringe_size, fringe_size)
        
        if result == "cutoff":
            max_depth += 1
        elif result != "failure":
            return max_depth, expanded_nodes, max_fringe_size
        else:
            return None

def depthLimitedSearch(problem, limit):
    return recursiveDLS(problem.getStartState(), problem, limit, 0)

def recursiveDLS(node, problem, limit, depth):
    if problem.isGoalState(node):
        return [], 1, 0  # Return the solution, nodes expanded (1), and max fringe size (0)
    elif depth == limit:
        return "cutoff", 1, 1  # Here we have a fringe size of 1, as the current node is still in the fringe
    else:
        cutoff_occurred = False
        nodes_expanded = 0
        max_fringe_size = 0
        for successor, action, _ in problem.getSuccessors(node):
            result, nodes, fringe = recursiveDLS(successor, problem, limit, depth + 1)
            nodes_expanded += nodes
            max_fringe_size = max(max_fringe_size, fringe + 1)  # +1 for the current node
            if result == "cutoff":
                cutoff_occurred = True
            elif result != "failure":
                return [action] + result, nodes_expanded, max_fringe_size  # Return the solution and statistics
        if cutoff_occurred:
            return "cutoff", nodes_expanded, max_fringe_size
        else:
            return "failure", nodes_expanded, max_fringe_size

"""/*=====End Change Task 3=====*/"""
def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""

    #to be explored (FIFO)
    frontier = util.Queue()
    
    #previously expanded states (for cycle checking), holds states
    exploredNodes = []
    """/*=====Start Change Task 3=====*/"""
    depth = 0
    expanded_nodes = 0
    max_fringe_size = 0
    """/*=====Start Change Task 3=====*/"""
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
            """/*=====Start Change Task 3=====*/"""
            expanded_nodes += 1
            """/*=====End Change Task 3=====*/"""
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
                    """/*=====Start Change Task 3=====*/"""
                    max_fringe_size = max(max_fringe_size, len(frontier.list))
                    """/*=====Start Change Task 3=====*/"""


    return depth, expanded_nodes, max_fringe_size

        
def uniformCostSearch(problem):
    """Search the node of least total cost first."""

    #to be explored (FIFO): holds (item, cost)
    frontier = util.PriorityQueue()
    """/*=====Start Change Task 3=====*/"""
    depth = 0
    #previously expanded states (for cycle checking), holds state:cost
    exploredNodes = {}
    max_fringe_size = 0
    """/*=====End Change Task 3=====*/"""
    startState = problem.getStartState()
    startNode = (startState, [], 0) #(state, action, cost)
    
    frontier.push(startNode, 0)
    
    while not frontier.isEmpty():
        #begin exploring first (lowest-cost) node on frontier
        currentState, actions, currentCost = frontier.pop()
        """/*=====Start Change Task 3=====*/"""
        depth = max(depth, len(actions))
        """/*=====End Change Task 3=====*/"""
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
                    """/*=====Start Change Task 3=====*/"""
                    max_fringe_size = max(max_fringe_size, len(frontier.heap))
                    """/*=====End Change Task 3=====*/"""
                    frontier.update(newNode, newCost)

                
    
    return depth, len(exploredNodes), max_fringe_size

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0
"""/*=====Start Change Task 1=====*/"""
def H5(state, goal_state): # calculate manhattan distance + blank tile move penalty nilsson
    board = state.cells
    n = len(state.cells)
    score = 0

    for i in range(n):
        for j in range(n):
            if board[i][j] == 0: 
                continue
            goal_value = i * n + j + 1 
            if board[i][j] != goal_value:
                if board[i][j] != 0:  
                    dx = abs((board[i][j] - 1) % n - j)
                    dy = abs((board[i][j] - 1) // n - i)
                    score += dx + dy  # Manhattan distance
                else: 
                    score += 2  # blank tile move penalty
    return score
def H4(state, goal_state): # calculate number of rows and columns out of place
    outofrows = 0
    outofcols = 0
    x = 0
    for row in state.cells:
        y = 0
        for n in row:
            if n != 0:
                x1 = int(n/3)
                y1 = goal_state[x1].index(n)
                if x1 != x:
                    outofrows +=1
                if y1 != y:
                    outofcols +=1
            y +=1
        x +=1
    return outofcols + outofrows

def H3(state, goal_state): # calculate manhattan distance
  x=0
  distance = 0
  for row in state.cells:
      y=0
      for n in row:
          if n != 0:
            x1 = int(n/3)
            y1 = goal_state[x1].index(n)
            distance += util.manhattanDistance((x,y), (x1,y1))
          y = y+1
      x = x+1
  return distance

def H2(state, goal_state): # calculate euclidean distance
    x=0
    distance = 0
    for row in state.cells:
        y=0
        for n in row:
            if n != 0:
                x1 = int(n/3)
                y1 = goal_state[x1].index(n)
                distance += math.sqrt((x -x1)**2 + (y - y1)**2)
            y = y+1
        x = x+1
    return distance

def H1(state, goal_state): # calculate number of misplaced tiles
    state_list = flattern(state.cells)
    problem_list = flattern(goal_state)
    count = -1
    zipped_list = zip(state_list,problem_list)
    for t in zipped_list:
        if t[0] != t[1]:
            count = count + 1
    return count
    
def flattern(state): #flatterns 2d list into 1d list
    flattern_list = []
    for row in state:
        for n in row:
            flattern_list.append(n)
    return flattern_list
"""/*=====End Change Task 1=====*/"""

  
def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    """/*=====Start Change Task 1=====*/"""
    goal_state = [[0,1,2],[3,4,5],[6,7,8]] #goal state
    """/*=====End Change Task 1=====*/"""
    #to be explored (FIFO): takes in item, cost+heuristic
    """/*=====Start Change Task 2=====*/"""
    frontier = util.PriorityQueue() #holds (state, action, cost)
    max_frontier_size = 0 #holds max frontier size
    exploredNodes = [] #holds (state, cost)
    depth = 0  # Initialize depth
    expanded_nodes = 0  # Initialize expanded nodes count
    max_fringe_size = 0  # Initialize max fringe size
    """/*=====End Change Task 2=====*/"""
    startState = problem.getStartState()
    startNode = (startState, [], 0) #(state, action, cost)
    count = 0 #count number of nodes popped from frontier
    frontier.push(startNode, 0) #push start node to frontier

    while not frontier.isEmpty():
        #begin exploring first (lowest-combined (cost+heuristic) ) node on frontier
        currentState, actions, currentCost = frontier.pop()
        #put popped node into explored list
        currentNode = (currentState, currentCost) #holds (state, cost)
        exploredNodes.append((currentState, currentCost)) 
        depth = max(depth, len(actions))  # Update depth
        expanded_nodes += 1  # Increment expanded nodes count
        if problem.isGoalState(currentState):
            b_factor = Branching_factor(depth, expanded_nodes) #calculate branching factor
            return depth, expanded_nodes, max_fringe_size, b_factor #return depth, expanded nodes, max fringe size, and branching factor

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
                    frontier.push(newNode, newCost + heuristic(succState, goal_state))
                    exploredNodes.append((succState, newCost))
                    """/*=====Start Change Task 2=====*/"""
                    max_fringe_size = max(max_fringe_size, len(frontier.heap))
                    """/*=====End Change Task 2=====*/"""
                """/*=====Start Change Task 2=====*/"""
                b_factor = Branching_factor(depth, expanded_nodes) #calculate branching factor 
                """/*=====End Change Task 2=====*/"""  
    return depth, expanded_nodes, max_fringe_size, b_factor

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
