# Unique Paths Brute-Force Recursive Approach
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
    # Base cases: If at the last row or last column, return 0 paths.
    if r == rows or c == cols:
        return 0
    # If at the bottom-right corner, return 1 path.
    if r == rows - 1 and c == cols - 1:
        return 1

    # Recursive case: Sum of paths moving down and moving right.
    return uniquePathsBruteForce(r + 1, c, rows, cols) + uniquePathsBruteForce(r, c + 1, rows, cols)


# Unique Paths Memoization (Top-Down) Approach
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
    # Base cases: If at the last row or last column, return 0 paths.
    if r == rows or c == cols:
        return 0
    # If result is already in the cache, return it.
    if cache[r][c] > 0:
        return cache[r][c]
    # If at the bottom-right corner, return 1 path.
    if r == rows - 1 and c == cols - 1:
        return 1

    # Recursive case: Calculate paths and store result in the cache.
    cache[r][c] = memoizationTopDown(r + 1, c, rows, cols, cache) + memoizationTopDown(r, c + 1, rows, cols, cache)
    return cache[r][c]


# Unique Paths Bottom-Up Dynamic Programming Approach
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
    # Initialize the previous row with zeros.
    prevRow = [0] * cols

    # Iterate over rows in reverse order.
    for r in range(rows - 1, -1, -1):
        # Initialize the current row with zeros.
        curRow = [0] * cols
        # Set the last column of the current row to 1.
        curRow[cols - 1] = 1
        # Iterate over columns in reverse order to calculate paths.
        for c in range(cols - 2, -1, -1):
            # Calculate paths by summing rightward and downward paths.
            curRow[c] = curRow[c + 1] + prevRow[c]
        # Update the previous row for the next iteration.
        prevRow = curRow

    # Return the number of unique paths starting from the top-left corner.
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
print(f"Unique Paths (Dynamic Programming Bottom-Up")
