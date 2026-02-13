# 2. Implement Breadth First Search (BFS) and Depth First Search (DFS).
#Breadth-First Search (BFS)
from collections import deque
from doctest import Example

def bfs(graph, start):
    visited = set()           # Track visited nodes
    queue = deque([start])    # Use a queue to explore nodes level by level
    result = []               # Store the order of visited nodes

    while queue:
        node = queue.popleft()  # Dequeue a node

        if node not in visited:
            visited.add(node)   # Mark node as visited
            result.append(node) # Record the node in the result

            # Add unvisited neighbors to the queue
            queue.extend(graph[node])

    return result

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
print("BFS:", bfs(graph, 'A'))


# Depth-First Search (DFS)

def dfs_iterative(graph, start):
    visited = set()         # Track visited nodes
    stack = [start]         # Use a stack for LIFO order
    result = []             # Store the order of visited nodes

    while stack:
        node = stack.pop()  # Pop a node from the stack

        if node not in visited:
            visited.add(node)   # Mark node as visited
            result.append(node) # Record the node in the result

            # Add unvisited neighbors to the stack (in reverse for correct order)
            stack.extend(reversed(graph[node]))

    return result

# Example usage
print("DFS (Iterative):", dfs_iterative(graph, 'A'))

# Example Output for the Graph
#     A
#    / \
#   B   C
#  / \   \
# D   E   F
#      \
#       F

# BFS: ['A', 'B', 'C', 'D', 'E', 'F']
# DFS (Recursive): ['A', 'B', 'D', 'E', 'F', 'C']
# DFS (Iterative): ['A', 'B', 'D', 'E', 'F', 'C']

# Explanation of the Code
# BFS
# 1.	Queue:
# •	The queue ensures that nodes are visited level by level.
# 2.	Visited:
# •	Keeps track of nodes already processed to avoid infinite loops.
# 3.	Result:
# •	Records the order in which nodes are visited.
# DFS (Recursive)
# 1.	Recursively visit each neighbour until all reachable nodes are explored.
# 2.	Uses implicit stack space through recursive calls.
# DFS (Iterative)
# 1.	Stack:
# •	LIFO order ensures depth-first traversal.
# 2.	Visited:
# •	Prevents revisiting nodes.