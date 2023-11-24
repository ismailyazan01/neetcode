# Fibonacci Brute-Force Recursive Approach
def fibonacciBruteForce(n):
    """
    Calculate the nth Fibonacci number using a brute-force recursive approach.

    Parameters:
    - n (int): The index of the Fibonacci number to be calculated.

    Returns:
    - int: The nth Fibonacci number.
    """
    # Base case: if n is 0 or 1, return n
    if n <= 1:
        return n
    # Recursive case: sum of Fibonacci numbers for (n-1) and (n-2)
    return fibonacciBruteForce(n - 1) + fibonacciBruteForce(n - 2)


# Fibonacci Memoization (Top-Down) Approach
def fibonacciMemoizationTopDown(n, cache=None):
    """
    Calculate the nth Fibonacci number using memoization (top-down) to optimize the recursive approach.

    Parameters:
    - n (int): The index of the Fibonacci number to be calculated.
    - cache (dict): A dictionary to store computed Fibonacci values for memoization.

    Returns:
    - int: The nth Fibonacci number.
    """
    # Initialize cache if not provided
    if cache is None:
        cache = {}
    # Base case: if n is 0 or 1, return n
    if n <= 1:
        return n
    # Check if value for n is already in cache
    if n in cache:
        return cache[n]

    # Recursive case: calculate Fibonacci number and store in cache
    cache[n] = fibonacciMemoizationTopDown(n - 1, cache) + fibonacciMemoizationTopDown(n - 2, cache)
    return cache[n]


# Fibonacci Bottom-Up Dynamic Programming Approach
def fibonacciBottomUp(n):
    """
    Calculate the nth Fibonacci number using a bottom-up dynamic programming approach.

    Parameters:
    - n (int): The index of the Fibonacci number to be calculated.

    Returns:
    - int: The nth Fibonacci number.
    """
    # Base case: if n is 0 or 1, return n
    if n < 2:
        return n

    # Initialize a list with base cases [0, 1]
    dp = [0, 1]
    i = 2

    # Iterate to calculate Fibonacci numbers up to n
    while i <= n:
        # Temporarily store the value of the second element
        temp = dp[1]
        # Update the second element by adding the first and second elements
        dp[1] = dp[1] + dp[0]
        # Update the first element with the temporarily stored value
        dp[0] = temp
        # Increment the loop counter
        i += 1

    # Return the calculated nth Fibonacci number
    return dp[1]


# Example Usage:
# Calculate the 5th Fibonacci number using the brute-force approach
result_bruteforce = fibonacciBruteForce(5)
print(f"Brute Force: Fibonacci(5) = {result_bruteforce}")

# Calculate the 5th Fibonacci number using memoization (top-down) approach
result_memoization_topdown = fibonacciMemoizationTopDown(5)
print(f"Memoization (Top-Down): Fibonacci(5) = {result_memoization_topdown}")

# Calculate the 5th Fibonacci number using bottom-up dynamic programming
result_bottomup = fibonacciBottomUp(5)
print(f"Bottom-Up DP: Fibonacci(5) = {result_bottomup}")
