def fibonacciBruteForce(n):
    """
    Calculate the nth Fibonacci number using a brute-force recursive approach.

    Parameters:
    - n (int): The index of the Fibonacci number to be calculated.

    Returns:
    - int: The nth Fibonacci number.
    """
    if n <= 1:
        return n
    return fibonacciBruteForce(n - 1) + fibonacciBruteForce(n - 2)


def fibonacciMemoizationTopDown(n, cache=None):
    """
    Calculate the nth Fibonacci number using memoization (top-down) to optimize the recursive approach.

    Parameters:
    - n (int): The index of the Fibonacci number to be calculated.
    - cache (dict): A dictionary to store computed Fibonacci values for memoization.

    Returns:
    - int: The nth Fibonacci number.
    """
    if cache is None:
        cache = {}
    if n <= 1:
        return n
    if n in cache:
        return cache[n]

    cache[n] = fibonacciMemoizationTopDown(n - 1, cache) + fibonacciMemoizationTopDown(n - 2, cache)
    return cache[n]


def fibonacciBottomUp(n):
    """
    Calculate the nth Fibonacci number using a bottom-up dynamic programming approach.

    Parameters:
    - n (int): The index of the Fibonacci number to be calculated.

    Returns:
    - int: The nth Fibonacci number.
    """
    if n < 2:
        return n

    dp = [0, 1]
    i = 2
    while i <= n:
        temp = dp[1]
        dp[1] = dp[1] + dp[0]
        dp[0] = temp
        i += 1
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
