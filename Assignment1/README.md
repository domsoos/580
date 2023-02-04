
# CS 580 - Assignment 1
# Usage
The program accepts the initial state as an array of numbers in quotation marks separated by spaces.
The max depth can also be specified after the initial state argument. The maximum depth refers to the depth of the graph to be expanded. 
The empty slot to be marked as -1.
If no arguments are specified, then the program use a set initial state.
If the goal state is at a deeper level in the graph then the program outputs: 
No Solution found at this level 100

## Depth-first search:
### Sample Input  
The user can specify the initial state of the puzzle and the max depth level to search at by command line arguments.

`python3 depth-first.py "15 14 13 12 11 -1 9 8 7 10 6 5 3 2 1 4" 25`  
or the user can also run it directly as follows:  
`python3 depth-first.py`

### Sample Output:

Solution found at depth: 4
[15, 14, 13, 12]  
[11, -1, 9, 8]  
[7, 10, 6, 5]  
[3, 2, 1, 4]  
None  
  
  
[15, 14, 13, 12]  
[11, 10, 9, 8]  
[7, -1, 6, 5]  
[3, 2, 1, 4]  
down  
  
  
[15, 14, 13, 12]  
[11, 10, 9, 8]  
[7, 6, -1, 5]  
[3, 2, 1, 4]  
right  
  
  
[15, 14, 13, 12]   
[11, 10, 9, 8]  
[7, 6, 5, -1]  
[3, 2, 1, 4]  
right  
  
  
[15, 14, 13, 12]  
[11, 10, 9, 8]  
[7, 6, 5, 4]  
[3, 2, 1, -1]  
down  
  
  
Time taken:  0.4244070053100586  
  
  
** Breadth-First Search
** Sample Input  
The user can specify the initial state of the puzzle and the max depth level to search at by command line arguments.  
`python3 breadth-first.py "15 14 13 12 11 -1 9 8 7 10 6 5 3 2 1 4" 25`  
or the user can also run it directly as follows:  
`python3 breadth-first.py`  

*** Sample Output  
Solution found at depth:  4
[15, 14, 13, 12]  
[11, -1, 9, 8]  
[7, 10, 6, 5]  
[3, 2, 1, 4]  
None  
  
  
[15, 14, 13, 12]  
[11, 10, 9, 8]  
[7, -1, 6, 5]  
[3, 2, 1, 4]  
down  
  
  
[15, 14, 13, 12]  
[11, 10, 9, 8]  
[7, 6, -1, 5]  
[3, 2, 1, 4]  
right  
  
  
[15, 14, 13, 12]  
[11, 10, 9, 8]  
[7, 6, 5, -1]  
[3, 2, 1, 4]  
right  
  
  
[15, 14, 13, 12]  
[11, 10, 9, 8]  
[7, 6, 5, 4]  
[3, 2, 1, -1]  
down  
  
  
Time taken:  0.0018229484558105469  
  
  
## Analysis  
In this case, Breadth-First Search found the same solution faster but in theory Depth-First Search is faster.

DFS may be faster in terms of time complexity since it uses a stack data structure to keep track of the visited nodes.  It may be able to find the solution faster, but the algorithm can become slow or infinite if the search tree has many branches. 

BFS on the other hand should have a slower time complexity, but it has the advantage of finding the optimal solution. BFS use a queue data structure to keep track of the visited nodes, which ensures that each nodes is visited on a given depth. A depth limit argument can also be specified to run this program.

### What to do
Including a depth limit for DFS can make the search faster, but it may not find the solution if the solution is outside of the depth limit in the graph.  
To improve the performance of BFS, bidirectional breadth-first search may speed up the algorithm by simultanously searching from both initial node and goal node and stopping when they meet in the middle. 

In conclusion, the size of the search space for the 15-puzzle game is incredibly large, with 16! = 20,922,789,888,000 possible combinations. Better search algorithms are needed to find the solution more efficiently.
