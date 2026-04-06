This project implements the Pancake Sorting problem using two search algorithms:
1. Uninformed Search (Breadth-First Search):
• Explores all possible states layer by layer until the sorted goal is found.
• Guarantees the optimal number of flips but can be computationally expensive as the number of pancakes increases.
• Each flip reverses the order of the top k pancakes.
2. Heuristic Search (A* Search):
• Uses a heuristic to estimate how far the current state is from the goal.
• The heuristic function h(n) counts the number of adjacent pancakes that are not consecutive in value, plus an extra penalty if the bottom pancake is not the largest.
• This guides the search toward more promising states, reducing the number of explored nodes compared to BFS.
