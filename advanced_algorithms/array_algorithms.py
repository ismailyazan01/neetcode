def kadanes(nums):
    """
    Find the maximum subarray sum using Kadane's algorithm.

    Parameters:
    - nums (list): A list of integers representing the input array.

    Returns:
    - int: The maximum subarray sum.
    """
    # Initialize variables to store the maximum subarray sum
    maxSum = nums[0]
    # Initialize a variable to track the current subarray sum
    currentSum = 0

    # Iterate through each element in the input array
    for n in nums:
        # Update the current subarray sum by taking the maximum of (currentSum + n) and 0
        currentSum = max(currentSum, 0) + n
        # Update the maximum subarray sum
        maxSum = max(maxSum, currentSum)
    # Return the final maximum subarray sum
    return maxSum


def slidingWindow(nums):
    """
    Find the maximum subarray sum and its indices using the sliding window technique.

    Parameters:
    - nums (list): A list of integers representing the input array.

    Returns:
    - Tuple: A tuple containing three elements:
        - int: The maximum subarray sum.
        - int: The starting index of the maximum subarray.
        - int: The ending index of the maximum subarray.
    """
    # Initialize variables to store the maximum subarray sum, current subarray sum, and indices
    maxSum, currentSum, maxL, maxR, L = nums[0], 0, 0, 0, 0

    # Iterate through each element in the input array
    for R in range(len(nums)):
        # Check if the current subarray sum is negative; if so, reset the starting index
        if currentSum < 0:
            currentSum = 0
            L = R

        # Update the current subarray sum by adding the current element
        currentSum += nums[R]
        # Update the maximum subarray sum and its corresponding indices
        if currentSum > maxSum:
            maxSum = currentSum
            maxL, maxR = L, R

    # Return a tuple containing the maximum subarray sum and its corresponding indices
    return maxSum, maxL, maxR


# Example Use Cases
nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
nums2 = [1, 2, 3, -2, 5]

# Using Kadane's Algorithm
result_kadanes_1 = kadanes(nums1)
result_kadanes_2 = kadanes(nums2)

# Using Sliding Window Technique
result_sliding_1 = slidingWindow(nums1)
result_sliding_2 = slidingWindow(nums2)

# Displaying Results
print("Kadane's Algorithm:")
print(f"Input: {nums1}, Result: {result_kadanes_1}")
print(f"Input: {nums2}, Result: {result_kadanes_2}")

print("\nSliding Window Technique:")
print(f"Input: {nums1}, Result: {result_sliding_1}")
print(f"Input: {nums2}, Result: {result_sliding_2}")
