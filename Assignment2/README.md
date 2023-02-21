# Informed Search Algorithm
Implementation of the informed searches using 4 different heuristic function and an additonal heuristic function made by me. 

## 1) Number of misplaced tiles
This heuristic counts the number of tiles in the current state that are not in their goal position, and uses this count as an estimate of how far the current state is from the goal state.  
## 2) Manhattan Distance  
The Manhattan distance heuristic calculates the sum of the distances of every tile to its goal position. This heuristic takes into account both the number of tiles that are out of place and the distance that they are away from their goal position.  


## 3) Number of direct adjacent tile reversals present
This heuristic counts the number of pairs of adjacent tiles that are out of order and also have their goal positions adjacent to each other. This count is used as an estimate of how far the current state is from the goal state. This heuristic is very simple to compute, but can be slow for larger puzzle sizes.  


## 4) Number of misplaced + Manhattan Distance  
This heuristic is a combination of the number of misplaced tiles and the Manhattan distance heuristics. The two values are added together to create a more accurate estimate of the distance from the current state to the goal state. This heuristic can be more accurate than either of the individual heuristics alone, but can also be slower to compute.  


## isMoveBack
The purpose of the additional isMoveBack heuristic function is to avoid generating child nodes that move the empty tile in the opposite direction of the previous move, which would be a move back. If the empty tile is moved back, the state would be identical to the previous state, and there would be no point in exploring that node further since it does not lead to a new state. By avoiding generating such nodes, the search algorithm can reduce the number of nodes it needs to expand, which can lead to faster search times.  
Sometimes even small optimizations can have a big impact on the overall performance of the algorithm.


## Evaluation
To evaluate the informed search algorithm using different heuristics, the following initial state was picked that has the solution at 18 level deep in the search tree. In this initial state there are 15 misplaced tiles present.  
[14, 13, 12, 8]  
[15, -1, 10, 5]  
[6, 11, 1, 9]  
[7, 3, 2, 4]  

| Heuristic | NOT IsMoveBack | IsMoveBack | Improvement |  
| --------  | -------- | -------- |  
| 1) | 0.0049 |  | 0.0031 | 36.73% |  
| 2) | 0.0021 | 0.0019 | 9.52% |  
| 3) | **80.23**  | **0.789** | 99.02% |  
| 4) | 0.026  | 0.00167 | 93.57% |  
Table 1. Time taken by each heuristic function to find the goal state with and without my isMoveBack heuristic function

To calculate the improvement, I used the following formula:
`((NOTIsMoveBack  - IsMoveBack) / NOTIsMoveBack ) * 100 = improvement in percent`


By incorporating the optimization to check if the next move is a move back, the time taken to execute the direct adjacent tile reversal heuristic was reduced by a factor of approximately 99.02%, from 80.23 seconds to 0.789 seconds. This optimization had a significant impact on the overall search performance of the algorithm, allowing it to quickly find the optimal solution. 

## Analysis
In my implementation of informed search, I have used a heap data structure to allow quick retrieval of the lowest cost node, which is more efficient than using a queue data structure. Among the four heuristic functions I tested, the Manhattan distance heuristic performed the best in terms of lowest time taken. This heuristic calculates the sum of the distances of every tile to its goal position.

The second-best performing heuristic was the number of misplaced tiles, which was able to solve an initial state with a solution at depth 18 in a reasonable amount of time. However, combining the h1 and h3 heuristics resulted in slightly slower performance since we had to calculate the heuristic value for both functions at each state.

I also experimented with the number of direct adjacent tile reversals present heuristic, which initially showed very poor results, taking over 80 seconds to solve a puzzle with an 18-level deep solution in the search tree. However, after adding the isMoveBack function to check whether the next move is a move back, I was able to improve the performance of this heuristic by a factor of 80, making it much more efficient.

## Input
The user does no have to specify anything to run the program, but they have the option to initialize the starting state and the user can choose from heuristic settings from `h1` to `h4` as a command line argument.

The initial state and heuristic arguments have to be inside quotation marks separated by spaces.
### Sample Inputs:
`python3 informed.py`  
or  
`python3 informed.py "14 13 12 8 15 -1 10 5 6 11 1 9 7 3 2 4" "h1 h2 h3 h4"  


Note that if no initial state was given by the user, the program will use an initial state that has the solution at 26 level deep.  

## Output Results

Using h1 - Number of misplaced tiles
Solution found at depth:  18
[14, 13, 12, 8]
[15, -1, 10, 5]
[6, 11, 1, 9]
[7, 3, 2, 4]
None


[14, 13, 12, 8]
[15, 11, 10, 5]
[6, -1, 1, 9]
[7, 3, 2, 4]
down


.
.
.


[15, 14, 13, 12]
[11, 10, 9, 8]
[7, 6, 5, 4]
[3, 2, 1, -1]
down


Time taken:  0.004971981048583984
Using h2 - Sum of the distances of every tile to its goal position
Solution found at depth:  18
[14, 13, 12, 8]
[15, -1, 10, 5]
[6, 11, 1, 9]
[7, 3, 2, 4]
None


[14, 13, 12, 8]
[15, 11, 10, 5]
[6, -1, 1, 9]
[7, 3, 2, 4]
down


.
.
.


[15, 14, 13, 12]
[11, 10, 9, 8]
[7, 6, 5, 4]
[3, 2, 1, -1]
down


Time taken:  0.002129077911376953
Using h3 - Number of direct adjacent tile reversals present
Solution found at depth:  18
[14, 13, 12, 8]
[15, -1, 10, 5]
[6, 11, 1, 9]
[7, 3, 2, 4]
None


[14, 13, 12, 8]
[15, 11, 10, 5]
[6, -1, 1, 9]
[7, 3, 2, 4]
down


.  
.  
.  


[15, 14, 13, 12]
[11, 10, 9, 8]
[7, 6, 5, 4]
[3, 2, 1, -1]
down


Time taken:  80.23334193229675
Using h4 - Combination of h1 and h2
Solution found at depth:  18
[14, 13, 12, 8]
[15, -1, 10, 5]
[6, 11, 1, 9]
[7, 3, 2, 4]
None


[14, 13, 12, 8]
[15, 11, 10, 5]
[6, -1, 1, 9]
[7, 3, 2, 4]
down


.
.
.


[15, 14, 13, 12]
[11, 10, 9, 8]
[7, 6, 5, 4]
[3, 2, 1, -1]
down


Time taken:  0.0257108211517334


Results with adding my isMoveBack() heuristic function:

Using h1 - Number of misplaced tiles
Solution found at depth:  18
[14, 13, 12, 8]
[15, -1, 10, 5]
[6, 11, 1, 9]
[7, 3, 2, 4]
None


[14, 13, 12, 8]
[15, 11, 10, 5]
[6, -1, 1, 9]
[7, 3, 2, 4]
down


.
.
.


[15, 14, 13, 12]
[11, 10, 9, 8]
[7, 6, 5, 4]
[3, 2, 1, -1]
down


Time taken:  0.0031549930572509766
Using h2 - Sum of the distances of every tile to its goal position
Solution found at depth:  18
[14, 13, 12, 8]
[15, -1, 10, 5]
[6, 11, 1, 9]
[7, 3, 2, 4]
None


[14, 13, 12, 8]
[15, 11, 10, 5]
[6, -1, 1, 9]
[7, 3, 2, 4]
down

.
.
.


[15, 14, 13, 12]
[11, 10, 9, 8]
[7, 6, 5, 4]
[3, 2, 1, -1]
down


Time taken:  0.0019431114196777344
Using h3 - Number of direct adjacent tile reversals present
Solution found at depth:  18
[14, 13, 12, 8]
[15, -1, 10, 5]
[6, 11, 1, 9]
[7, 3, 2, 4]
None


[14, 13, 12, 8]
[15, 11, 10, 5]
[6, -1, 1, 9]
[7, 3, 2, 4]
down


.
.
.


[15, 14, 13, 12]
[11, 10, 9, 8]
[7, 6, 5, 4]
[3, 2, 1, -1]
down


Time taken:  0.7890288829803467
Using h4 - Combination of h1 and h2
Solution found at depth:  18
[14, 13, 12, 8]
[15, -1, 10, 5]
[6, 11, 1, 9]
[7, 3, 2, 4]
None


[14, 13, 12, 8]
[15, 11, 10, 5]
[6, -1, 1, 9]
[7, 3, 2, 4]
down


.
.
.


[15, 14, 13, 12]
[11, 10, 9, 8]
[7, 6, 5, 4]
[3, 2, 1, -1]
down


Time taken:  0.0016717910766601562
