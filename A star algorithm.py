import heapq

# Goal state
goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]


# Heuristic: count misplaced tiles
def h(state):
    count = 0

    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                count += 1

    return count


# Find blank (0)
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


# Generate next states
def get_neighbors(state):
    neighbors = []

    x, y = find_blank(state)

    moves = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    for dx, dy in moves:
        nx, ny = x + dx, y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:
            new = [row[:] for row in state]

            new[x][y], new[nx][ny] = new[nx][ny], new[x][y]

            neighbors.append(new)

    return neighbors


# A* Algorithm
def astar(start):
    open_list = []

    heapq.heappush(
        open_list,
        (h(start), start, 0)
    )  # (f, state, g)

    visited = []

    while open_list:
        f, state, g = heapq.heappop(open_list)

        print("Current state:")

        for row in state:
            print(row)

        print("----")

        if state == goal:
            print("Goal reached!")
            return

        visited.append(state)

        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                g_new = g + 1
                f_new = g_new + h(neighbor)

                heapq.heappush(
                    open_list,
                    (f_new, neighbor, g_new)
                )

    print("No solution found")


# Example input
start = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

astar(start)