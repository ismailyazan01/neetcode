from collections import deque


class GraphNode:
    def __init__(self, val):
        """
        A class representing a graph node.

        Parameters:
        - val: The value associated with the node.
        """
        self.val = val
        self.neighbors = []

    # Define an empty adjacency list with vertices "A" and "B"
    adjList = {"A": [], "B": []}

    # Define edges to be added to the adjacency list
    edges = [["A", "B"], ["B", "C"], ["B", "E"], ["C", "E"], ["E", "D"]]

    # Create an empty adjacency list
    adjList = {}

    # Populate the adjacency list with edges
    for src, dst in edges:
        # If the source vertex is not in the adjacency list, add it with an empty list as its value
        if src not in adjList:
            adjList[src] = []

        # If the destination vertex is not in the adjacency list, add it with an empty list as its value
        if dst not in adjList:
            adjList[dst] = []

        # Add the destination vertex to the adjacency list of the source vertex
        adjList[src].append(dst)

    # Example Usage:

    # Print the final adjacency list
    print("Adjacency List:")
    for vertex, neighbors in adjList.items():
        print(f"{vertex}: {neighbors}")


    def adjacencyDFS(self, node, target, adjList, visit):
        """
        Depth-First Search (DFS) for adjacency list representation of a graph.

        Parameters:
        - node: The current node being explored.
        - target: The target node to search for.
        - adjList: The adjacency list representation of the graph.
        - visit: A set to track visited nodes.

        Returns:
        - The count of paths from the current node to the target node.
        """
        if node in visit:
            return 0
        if node == target:
            return 1

        count = 0
        visit.add(node)
        for neighbor in adjList[node]:
            count += self.adjacencyDFS(neighbor, target, adjList, visit)
        visit.remove(node)

        return count

    def adjacencyBFS(self, node, target, adjList):
        """
        Breadth-First Search (BFS) for adjacency list representation of a graph.

        Parameters:
        - node: The starting node for BFS.
        - target: The target node to search for.
        - adjList: The adjacency list representation of the graph.

        Returns:
        - The shortest path length from the starting node to the target node.
        """
        length = 0
        visit = set()
        visit.add(node)
        queue = deque()
        queue.append(node)

        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr == target:
                    return length

                for neighbor in adjList[curr]:
                    if neighbor not in visit:
                        visit.add(neighbor)
                        queue.append(neighbor)
            length += 1
        return length

    def dfs(self, grid, r, c, visit):
        """
        Perform Depth-First Search (DFS) to count the number of paths from the top-left to the bottom-right
        in a grid with obstacles.

        Parameters:
        - grid (list of lists): The 2D grid representing the graph.
        - r (int): The current row index.
        - c (int): The current column index.
        - visit (set): A set to keep track of visited nodes.

        Returns:
        - The number of paths from (0, 0) to (ROWS-1, COLS-1).
        """
        ROWS, COLS = len(grid), len(grid[0])
        if min(r, c) < 0 or r == ROWS \
                or c == COLS or (r, c) in visit \
                or grid[r][c] == 1:
            return 0
        if r == ROWS - 1 and c == COLS - 1:
            return 1

        visit.add((r, c))

        count = 0
        count += self.dfs(grid, r + 1, c, visit)
        count += self.dfs(grid, r - 1, c, visit)
        count += self.dfs(grid, r, c + 1, visit)
        count += self.dfs(grid, r, c - 1, visit)

        visit.remove((r, c))
        return count

    def bfs(self, grid):
        """
        Perform Breadth-First Search (BFS) to find the shortest path from the top-left to the bottom-right
        in a grid with obstacles.

        Parameters:
        - grid (list of lists): The 2D grid representing the graph.

        Returns:
        - The length of the shortest path from (0, 0) to (ROWS-1, COLS-1).
        """
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        queue = deque()
        queue.append((0, 0))
        visit.add((0, 0))

        length = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return length

                neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in neighbors:
                    if min(r + dr, c + dc) < 0 or r + dr == ROWS or \
                            c + dc == COLS or (r + dr, c + dc) in visit \
                            or grid[r + dr][c + dc] == 1:
                        continue
                    queue.append((r + dr, c + dc))
                    visit.add((r + dr, c + dc))
            length += 1


# Example Usage:

# Create a graph node
node = GraphNode(1)

# Example of using DFS
grid = [
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
dfs_count = node.dfs(grid, 0, 0, set())
print(f"Number of paths using DFS: {dfs_count}")

# Example of using BFS
grid = [
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
bfs_length = node.bfs(grid)
print(f"Shortest path length using BFS: {bfs_length}")

# Example Usage:

# Create a graph node
node = GraphNode(1)

# Example of using adjacencyDFS
adjList = {
    'A': ['B'],
    'B': ['C', 'E'],
    'C': ['E'],
    'E': ['D']
}
dfs_count = node.adjacencyDFS('A', 'C', adjList, set())
print(f"Number of paths using adjacencyDFS: {dfs_count}")

# Example of using adjacencyBFS
bfs_length = node.adjacencyBFS('A', 'C', adjList)
print(f"Shortest path length using adjacencyBFS: {bfs_length}")
