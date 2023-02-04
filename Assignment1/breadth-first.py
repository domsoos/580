import time, sys
from pprint import pprint
from copy import deepcopy


# Node class to represent states
class Node(object):
	"""docstring for Node"""
	def __init__(self, state, parent=None, action=None):
		super(Node, self).__init__()
		self.state = state # represent each state as an array in range 0-15, len 16
		self.parent = parent
		self.action = action
		self.empty = state.index(-1) # store the empty spot

	def isValid(self, index, action):
		if index in [3,7,11,15] and action == "right": # if empty slot is in far right column, cannot right
			return False
		elif index in [0,1,2,3] and action == "up": # if the empty slot is in top row, cannot move up
			return False
		elif index in [0,4,8,12] and action == "left": # if the empty slot is far left column, cannot move left
			return False
		elif index in [12,13,14,15] and action == "down": # if the empty slot is bottom row, cannot move down
			return False
		else:	# otherwise the move is valid
			return True

	def isMoveBack(self, action):# function to check if the action we are about to take it is not the reverse, 
		if self.parent:
			if (self.parent.action == "left" and action == "right") or (self.parent.action == "right" and action == "left") or (self.parent.action == "up" and action == "down") or (self.parent.action == "down" and action == "up"):
				return True
			else:
				return False

	# neighbor function to generate possible leaves
	def getNeighbor(self):
		neighbors = []
		actions = {"up": -4, "down": 4, "left": -1, "right": 1} # states are stored as a 1D array, up move would result in an index -4 etc..
		for action, index in actions.items():
			if self.isValid(self.empty, action) and 0 <= self.empty + index < 16 and not self.isMoveBack(action): # we check if the move is valid at all, but also not a move back to the previous state
				newIndex =  self.empty + index
				new_state = deepcopy(self.state)
				temp = new_state[self.empty] # temporary variable for to keep empty slot
				new_state[self.empty] = new_state[newIndex] # place the empty slot into the new index
				new_state[newIndex] = temp #
				neighbor = Node(new_state, self, action)
				neighbors.append(neighbor)
		return neighbors

# each node has to store its own parents so that we can create a path

###  Helper function to calculate the depth   ###
def calculateDepth(node):
    depth = 0
    while node.parent:
        depth += 1
        node = node.parent
    return depth

### Breadth-First Search Function to find the solution to each puzzle by visiting each node at a given level ###
def breadthFirst(initialState, goalState, depth_limit):
    start = time.time()
    fringe = [Node(initialState)]
    visited = set(initialState)

    while fringe:
        currentNode = fringe.pop(0) # pop the first element off the fringe
        currentState = currentNode.state
        string = str(currentState)
        if string in visited:
        	continue
        if currentState == goalState:
            print("Solution found at depth: ", calculateDepth(currentNode))
            printPath(currentNode)
            print("Time taken: ", time.time() - start)
            return currentNode
        visited.add(str(currentState))
        current_depth = calculateDepth(currentNode)
        if current_depth >= depth_limit:
            print("Hit the limit: ", depth_limit)
            continue
        for neighbor in currentNode.getNeighbor():
            #print(f"for current empty: {currentNode.empty} neighbor empty {neighbor.empty}")
            if str(neighbor.state) not in visited:
                fringe.append(neighbor)
    print("No solution found at the given depth: ", depth_limit)

### Function to print the state of a node   ###
def printState(node):
    print(node.state[:4])
    print(node.state[4:8])
    print(node.state[8:12])
    print(node.state[12:])
    print(node.action)
    print()

### Function to print the path of the node by traversing the parents and then printing out the reverse path starting with initial  ###
def printPath(node):
    path = []
    while node:
        path.append((node.state, node.action))
        node = node.parent
    for state, move in path[::-1]:
        print(state[:4])
        print(state[4:8])
        print(state[8:12])
        print(state[12:])
        print(move)
        print()
        print()


initialS = [
4, -1, 13, 2,
15, 14, 3, 8,
7, 10, 6, 5,
9, 12, 1, 11
]



initial = [
15, 14, 13, 12,
-1, 11, 10, 8,
7, 6, 9, 5,
3, 2, 1, 4
]

initialS = [#GoalState = [
11, 5, 2, 1,
14, 8, 10,-1,
15, 4, 13, 6,
9, 12, 3, 7,
]

goalState = [
15, 14, 13, 12,
11, 10, 9, 8,
7, 6, 5, 4,
3, 2, 1, -1
]


if __name__ == '__main__':
	if len(sys.argv)>1:
		initialState = [int(i) for i in sys.argv[1].split()]
		if len(sys.argv)>2:
			maxDepth = int(sys.argv[2])
	else:
		initialState = initial
	breadthFirst(initialState, goalState, 200)
