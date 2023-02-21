import heapq
import sys, time

# Define the Node class
class Node:
    def __init__(self, state, cost, h, parent, action=None):
        self.state = state
        self.cost = cost
        self.h = h
        self.f = cost + h # full cost for this state
        self.parent = parent
        self.action = action
        self.empty = self.state.index(-1)

    # overloaded < operator so that we can use the heapq data structure, which needs Nodes to be comparable
    def __lt__(self, other):
        return self.f < other.f

    # overloaded == operator so that we can use the Node class with heap, we need objects to be hashable and comparable
    def __eq__(self, other):
        return self.state == other.state

    def isValid(self, index, action):
            if index in [3,7,11,15] and action == "right": # if empty slot is in far right column, cannot right
                return False
            elif index in [0,1,2,3] and action == "up": # if the empty slot is in top row, cannot move up
                return False
            elif index in [0,4,8,12] and action == "left": # if the empty slot is far left column, cannot move left
                return False
            elif index in [12,13,14,15] and action == "down": # if the empty slot is bottom row, cannot move down
                return False
            else:   # otherwise the move is valid
                return True

    # function to check if the action we are about to take it is not the reverse
    def isMoveBack(self, action): 
        if self.parent:
            if (self.parent.action == "left" and action == "right") or (self.parent.action == "right" and action == "left") or (self.parent.action == "up" and action == "down") or (self.parent.action == "down" and action == "up"):
                return True
            else:
                return False

def getNeighbors(currentNode, heuristic):
    neighbors = []
    # move the empty tile up
    if currentNode.isValid(currentNode.empty, "up") and not currentNode.isMoveBack("up"):
        newState = currentNode.state[:]
        newState[currentNode.empty], newState[currentNode.empty-4] = newState[currentNode.empty-4], newState[currentNode.empty]
        neighbors.append(Node(newState, currentNode.cost+1, heuristic(newState), currentNode, "up"))

    # move the empty tile down
    if currentNode.isValid(currentNode.empty, "down") and not currentNode.isMoveBack("down"):
        newState = currentNode.state[:]
        newState[currentNode.empty], newState[currentNode.empty+4] = newState[currentNode.empty+4], newState[currentNode.empty]
        neighbors.append(Node(newState, currentNode.cost+1, heuristic(newState), currentNode, "down"))

    # move the empty tile left
    if currentNode.isValid(currentNode.empty, "left") and not currentNode.isMoveBack("left"):
        newState = currentNode.state[:]
        newState[currentNode.empty], newState[currentNode.empty-1] = newState[currentNode.empty-1], newState[currentNode.empty]
        neighbors.append(Node(newState, currentNode.cost+1, heuristic(newState), currentNode, "left"))

    # move the empty tile right
    if currentNode.isValid(currentNode.empty, "right"):
        newState = currentNode.state[:]
        newState[currentNode.empty], newState[currentNode.empty+1] = newState[currentNode.empty+1], newState[currentNode.empty]
        neighbors.append(Node(newState, currentNode.cost+1, heuristic(newState), currentNode, "right"))
    return neighbors


# 1. Number of misplaced tiles
def h1(state):
    misplaced_tiles = 0
    for i in range(len(state)):
    	# for each position, we check if the tile is the same place as the goal state's tile
        if state[i] != goal[i] and state[i] != -1:
            misplaced_tiles += 1
    #print(f"Misplaced: {misplaced_tiles}")
    return misplaced_tiles

# 2. Sum of the distances of every tile to its goal position
def h2(state):
    distance = 0
    # loop every tile
    for i in range(len(state)):
        if state[i] != -1:
        	# get the current position and goal position of the tile
            currentPosition = i
            goalPosition = goal.index(state[i])
            # calculate the Manhattan distance between the current position and the goal position
            # The Manhattan distance is the sum of the absolute differences between the row and column
            distance += abs((currentPosition % 4) - (goalPosition % 4)) + abs((currentPosition // 4) - (goalPosition // 4))
    # return the total distance as the heuristic value
    return distance

# 3. Number of direct adjacent tile reversals present
def h3(state):
    adjacent_reversals = 0
    # loop through all adjacent pairs of elements in the current state list.
    for i in range(len(state) - 1):
    	# if either of the elements is -1, skip this pair.
        if state[i] == -1 or state[i+1] == -1:
            continue
        # If the current element is greater than the next element and their indices are reversed in a goal state, increment the count of adjacent reversals.
        if state[i] > state[i+1] and goal.index(state[i]) == i+1 and goal.index(state[i+1]) == i:
            adjacent_reversals += 1
    return adjacent_reversals

# 4. Combination of h1 and h2
def h4(state):
    return h1(state) + h2(state)

###  Helper function to calculate the depth   ###
def calculateDepth(node):
    depth = 0
    while node.parent:
        depth += 1
        node = node.parent
    return depth


### Define the Informed Search Algorithm ###
def informed(start_state, heuristic):
    start = time.time()
    fringe = []
    visited = set()

    # add the start state to the heap
    heapq.heappush(fringe, Node(start_state, 0, heuristic(start_state), None))

    while fringe:
        # get the node with the lowest full cost value
        currentNode = heapq.heappop(fringe)

        # goal check
        if currentNode.state == goal:
            print("Solution found at depth: ", calculateDepth(currentNode))
            printPath(currentNode)
            return

        # add the current node to the visited list
        visited.add(tuple(currentNode.state))

        # generate the neighbors of the current node
        neighbors = getNeighbors(currentNode, heuristic)

        # add the neighbors to the fringe if they are not in the visited list
        for neighbor in neighbors:
            if tuple(neighbor.state) not in visited:
                heapq.heappush(fringe, neighbor)

    print("No solution found...")

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


def runAll(initialState):
	print("Using h1 - Number of misplaced tiles")
	start = time.time()
	informed(initialState, h1)
	print("Time taken: ", time.time() - start)
	print("Using h2 - Sum of the distances of every tile to its goal position")
	start = time.time()
	informed(initialState, h2)
	print("Time taken: ", time.time() - start)

	print("Using h3 - Number of direct adjacent tile reversals present")
	start = time.time()
	informed(initialState, h3)
	print("Time taken: ", time.time() - start)

	print("Using h4 - Combination of h1 and h2")
	start = time.time()
	informed(initialState, h4)
	print("Time taken: ", time.time() - start)


goal = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, -1]

initial = [
14, 12, 8, 5,
15, 13, 10, 9,
6, 3, 11, 1,
7, -1, 2, 4
]


if __name__ == '__main__':
	if len(sys.argv)>1:
		initialState = [int(i) for i in sys.argv[1].split()]
		if len(sys.argv)>2:
			heuristics = [str(i) for i in sys.argv[2].split()]

		for heuristic in heuristics:
			print(f"Using {heuristic} heuristic function")
			start = time.time()
			informed(initialState, eval(heuristic)) # type cast string into function object
			print("Time taken: ", time.time() - start)
	else:
		initialState = initial
		runAll(initialState)
