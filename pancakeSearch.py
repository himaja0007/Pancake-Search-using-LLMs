from heapq import heappush, heappop
from collections import deque

# Author: Himaja Payyavula

def flip(arr, i):
    new_arr = arr[:i + 1][::-1] + arr[i + 1:]
    return new_arr

def solvePancakeSortUninformed(input_array):
    start = tuple(input_array)
    goal = tuple(sorted(input_array))
    queue = deque([(start, [])])
    visited = {start}

    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path
        for i in range(len(state)):
            new_state = tuple(flip(list(state), i))
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [f"flip_{i}"]))
    return []

def heuristic(state):
    h = 0
    for i in range(len(state) - 1):
        if abs(state[i] - state[i + 1]) != 1:
            h += 1
    if state[-1] != len(state):  
        h += 1
    return h

def solvePancakeSortHeuristic(input_array):
    start = tuple(input_array)
    goal = tuple(sorted(input_array))

    heap = []
    heappush(heap, (heuristic(start), 0, start, []))
    visited = {start: 0}

    while heap:
        f, g, state, path = heappop(heap)
        if state == goal:
            return path
        for i in range(len(state)):
            new_state = tuple(flip(list(state), i))
            new_g = g + 1
            if new_state not in visited or new_g < visited[new_state]:
                visited[new_state] = new_g
                heappush(heap, (new_g + heuristic(new_state), new_g, new_state, path + [f"flip_{i}"]))
    return []


# -------- Example Run --------
if __name__ == "__main__":
    inputs = [
        [3, 1, 4, 5, 2],
        [1, 2, 3, 4],
        [4, 3, 2, 1],
        [8, 5, 2, 7, 1, 3, 6, 4]
    ]

    for arr in inputs:
        print(f"\nInput: {arr}")
        print(" Uninformed:", solvePancakeSortUninformed(arr))
        print(" Heuristic :", solvePancakeSortHeuristic(arr))
