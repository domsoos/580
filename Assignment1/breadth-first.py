import time
from pprint import pprint


# Node class to represent states
class Node(object):
	"""docstring for Node"""
	def __init__(self, state, parent=None, action=None):
		super(Node, self).__init__()
		self.state = state # represent each state as an array in range 0-8, len 9
		self.parent = parent
		self.action = action
		self.empty = state.index(-1)

	# neighbor function to generate possible leaves
	def getNeighbor(self):
		neighbors = []
		actions = {"up": -3, "down": 3, "left": -1, "right": 1}
		for action, index in actions.items():
			newIndex =  self.empty + index
			if 0 <= newIndex < 9:
				new_state = self.state.copy()
				temp = new_state[self.empty]
				new_state[self.empty] = new_state[newIndex]
				new_state[newIndex] = temp
				neighbor = Node(new_state, self, action)
				neighbors.append(neighbor)
		return neighbors


# each node has to store its own parents so that we can create a path


def breadth_first(initialState, goalState):
	start = time.time()
	fringe = [Node(initialState)]
	visited = set(initialState)


	while fringe:
		currentNode = fringe.pop(0) # remove the first node from our open list
		currentState = currentNode.state
		if currentState == goalState:
			print("Solution found")
			print_path(currentNode)
			print("Time taken: ", time.time() - start)
			return currentNode
		visited.add(str(currentState))
		for neighbor in currentNode.getNeighbor():
			if str(neighbor.state) not in visited:
				fringe.append(neighbor)


def print_path(node):
    path = []
    while node:
        path.append((node.state, node.action))
        node = node.parent
    for state, move in path[::-1]:
        print(state[:3])
        print(state[3:6])
        print(state[6:])
        print(move)
        print()
        print()

def getInput():
	print("Please provide input separated by spaces\n")


initialState = [
	8,2,-1,
	3,4,7,
	5,1,6
]

goalState = [
	1,2,3,
	4,5,6,
	7,8,-1
]


if __name__ == '__main__':
	breadth_first(initialState, goalState)

