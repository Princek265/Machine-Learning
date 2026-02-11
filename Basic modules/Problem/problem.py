#26-203 Cabin 9
"""AIM : Implement state space search and production system to solve water jug problem."""

from collections import deque
def water_jug_problem(cap1, cap2, target):
    visited = set()  # Track visited states
    queue = deque([(0, 0)])  # Start with both jugs empty
    while queue:
        x, y = queue.popleft()

        # If target is achieved
        if x == target or y == target:
            return True

        if (x, y) in visited:
            continue
        visited.add((x, y))

        # Add all possible next states
        queue.extend([
            (cap1, y),  # Fill Jug1
            (x, cap2),  # Fill Jug2
            (0, y),     # Empty Jug1
            (x, 0),     # Empty Jug2
            (x - min(x, cap2 - y), y + min(x, cap2 - y)),  # Pour Jug1 -> Jug2
            (x + min(y, cap1 - x), y - min(y, cap1 - x)),  # Pour Jug2 -> Jug1
        ])
    return False  # No solution found

# Example usage
cap1, cap2, target = 4, 3, 2
if water_jug_problem(cap1, cap2, target):
    print(f"It is possible to measure {target} liters.")
else:
    print(f"It is NOT possible to measure {target} liters.")