def uniquePathsBruteForce(r, c, rows, cols):
    """
    Calculate the number of unique paths from the top-left corner to the bottom-right corner
    in a grid using a brute-force recursive approach.

    Parameters:
    - r (int): Current row index.
    - c (int): Current column index.
    - rows (int): Total number of rows in the grid.
    - cols (int): Total number of columns in the grid.

    Returns:
    - int: The number of unique paths.
    """
    if r == rows or c == cols:
        return 0
    if r == rows - 1 and c == cols - 1:
        return 1

    return uniquePathsBruteForce(r + 1, c, rows, cols) + uniquePathsBruteForce(r, c + 1, rows, cols)


def memoizationTopDown(r, c, rows, cols, cache):
    """
    Calculate the number of unique paths from the top-left corner to the bottom-right corner
    in a grid using memoization (top-down) to optimize the recursive approach.

    Parameters:
    - r (int): Current row index.
    - c (int): Current column index.
    - rows (int): Total number of rows in the grid.
    - cols (int): Total number of columns in the grid.
    - cache (list of lists): Cache to store computed results for memoization.

    Returns:
    - int: The number of unique paths.
    """
    if r == rows or c == cols:
        return 0
    if cache[r][c] > 0:
        return cache[r][c]
    if r == rows - 1 and c == cols - 1:
        return 1

    cache[r][c] = memoizationTopDown(r + 1, c, rows, cols, cache) + memoizationTopDown(r, c + 1, rows, cols, cache)
    return cache[r][c]


def dpBottomUp(rows, cols):
    """
    Calculate the number of unique paths from the top-left corner to the bottom-right corner
    in a grid using bottom-up dynamic programming.

    Parameters:
    - rows (int): Total number of rows in the grid.
    - cols (int): Total number of columns in the grid.

    Returns:
    - int: The number of unique paths.
    """
    prevRow = [0] * cols

    for r in range(rows - 1, -1, -1):
        curRow = [0] * cols
        curRow[cols - 1] = 1
        for c in range(cols - 2, -1, -1):
            curRow[c] = curRow[c + 1] + prevRow[c]
        prevRow = curRow
    return prevRow[0]


# Example Usage:

# Calculate unique paths using brute-force approach
result_bruteforce = uniquePathsBruteForce(0, 0, 3, 4)
print(f"Unique Paths (Brute Force): {result_bruteforce}")

# Calculate unique paths using memoization (top-down) approach
cache_topdown = [[0] * 4 for _ in range(3)]  # Initialize cache with zeros
result_memoization_topdown = memoizationTopDown(0, 0, 3, 4, cache_topdown)
print(f"Unique Paths (Memoization Top-Down): {result_memoization_topdown}")

# Calculate unique paths using bottom-up dynamic programming approach
result_bottomup = dpBottomUp(3, 4)
print(f"Unique Paths (Dynamic Programming Bottom-Up): {result_bottomup}")
