def bruteForce(nums):
    """
    Find the maximum subarray sum using the brute force approach.

    Parameters:
    - nums (list): A list of integers representing the input array.

    Returns:
    - int: The maximum subarray sum.
    """
    # Initialize a variable to store the maximum subarray sum
    maxSum = nums[0]

    # Iterate through each element in the input array
    for i in range(len(nums)):
        # Initialize a variable to store the current subarray sum
        currentSum = 0
        # Iterate through each element in the input array starting from i
        for j in range(i, len(nums)):
            # Update the current subarray sum
            currentSum += nums[j]
            # Update the maximum subarray sum
            maxSum = max(maxSum, currentSum)
    # Return the final maximum subarray sum
    return maxSum


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


def closeDuplicatesBruteForce(nums, k):
    """
    Check if there are duplicates within 'k' distance in the given array using the brute force approach.

    Parameters:
    - nums (list): A list of integers representing the input array.
    - k (int): An integer representing the maximum distance allowed between duplicate elements.

    Returns:
    - bool: True if there are duplicates within 'k' distance, False otherwise.
    """
    # Iterate through each element in the input array
    for L in range(len(nums)):
        # Iterate through each element within the maximum distance 'k' from the current element
        for R in range(L + 1, min(len(nums), L + k)):
            # Check if the elements at positions L and R are equal, indicating a duplicate within 'k' distance
            if nums[L] == nums[R]:
                return True
    # No duplicates found within 'k' distance
    return False


def closeDuplicatesSlidingWindow(nums, k):
    """
    Check if there are duplicates within 'k' distance in the given array using the sliding window technique.

    Parameters:
    - nums (list): A list of integers representing the input array.
    - k (int): An integer representing the maximum distance allowed between duplicate elements.

    Returns:
    - bool: True if there are duplicates within 'k' distance, False otherwise.
    """
    # Create a set to store elements within the sliding window
    window = set()
    # Initialize the left pointer of the window
    L = 0

    # Iterate through each element in the input array
    for R in range(len(nums)):
        # Check if the window size exceeds 'k'; if so, remove the leftmost element from the window
        if R - L + 1 > k:
            window.remove(nums[L])
            L += 1

        # Check if the current element is already in the window; if so, there are duplicates within 'k' distance
        if nums[R] in window:
            return True

        # Add the current element to the window
        window.add(nums[R])

    # No duplicates found within 'k' distance
    return False


def longestSubarray(nums):
    """
    Finds the length of the longest subarray with the same element.

    Parameters:
    - nums (list): List of integers.

    Returns:
    - int: Length of the longest subarray.
    """
    # Initialize variables for length and left index
    length, L = 0, 0

    # Iterate over the array
    for R in range(len(nums)):
        # Check if the element at L is different from the element at R
        if nums[L] != nums[R]:
            # If different, update the left index to the current position
            L = R
        # Update the maximum length considering the current subarray
        length = max(length, R - L + 1)
    # Return the final length of the longest subarray
    return length


def shortestSubarray(nums, target):
    """
    Finds the length of the shortest subarray whose sum is at least the target.

    Parameters:
    - nums (list): List of integers.
    - target (int): Target sum.

    Returns:
    - int: Length of the shortest subarray.
    """
    # Initialize variables for left index and total sum
    L, total = 0, 0
    # Initialize the length to be one more than the length of the array
    length = len(nums) + 1

    # Iterate over the array
    for R in range(len(nums)):
        # Add the current element to the total sum
        total += nums[R]
        # Check if the total sum is greater than or equal to the target
        while total >= target:
            # Update the length to be the minimum of the current length and the new subarray length
            length = min(R - L + 1, length)
            # Subtract the leftmost element from the total sum and move the left index to the right
            total -= nums[L]
            L += 1
    # If the length is still the initial value, no valid subarray found, return 0
    return 0 if length == len(nums) + 1 else length


def isPalindrome(word):
    """
    Checks if a given word is a palindrome.

    Parameters:
    - word (str): Input word.

    Returns:
    - bool: True if the word is a palindrome, False otherwise.
    """
    # Initialize left and right pointers
    L, R = 0, len(word) - 1

    # Iterate while the left pointer is less than the right pointer
    while L < R:
        # Check if characters at left and right pointers are different
        if word[L] != word[R]:
            # If different, the word is not a palindrome
            return False
        else:
            # Move the pointers towards each other
            L += 1
            R -= 1

    # If the loop completes, the word is a palindrome
    return True


def targetSum(nums, target):
    """
    Finds indices of two numbers in a list that add up to a target sum.

    Parameters:
    - nums (list): List of integers.
    - target (int): Target sum.

    Returns:
    - list: List containing indices of the two numbers.
    """
    # Initialize left and right pointers
    L, R = 0, len(nums) - 1

    # Iterate while the left pointer is less than the right pointer
    while L < R:
        # Check if the sum of numbers at left and right pointers is less than the target
        if nums[L] + nums[R] < target:
            # If less, move the left pointer to the right
            L += 1
        elif nums[L] + nums[R] > target:
            # If greater, move the right pointer to the left
            R -= 1
        else:
            # If equal, return the indices of the two numbers
            return [L, R]

    # If no such indices are found, return an empty list
    return []


class PrefixSum:
    def __init__(self, nums):
        """
        Initializes a PrefixSum object with a list of numbers.

        Parameters:
        - nums (list): List of integers.

        Returns:
        - None
        """
        # Initialize an empty list to store prefix sums
        self.prefix = []
        # Initialize a variable to keep track of the running total
        total = 0

        # Iterate through the input numbers
        for n in nums:
            # Update the running total
            total += n
            # Append the current prefix sum to the list
            self.prefix.append(total)

    def rangeSum(self, left, right):
        """
        Calculates the sum of elements in the specified range [left, right] using prefix sums.

        Parameters:
        - left (int): Left index of the range.
        - right (int): Right index of the range.

        Returns:
        - int: Sum of elements in the specified range.
        """
        # Calculate the prefix sum at the right index
        preRight = self.prefix[right]
        # Calculate the prefix sum at the left index (or 0 if left is 0)
        preLeft = self.prefix[left - 1] if left > 0 else 0
        # Return the sum of elements in the specified range
        return preRight - preLeft


# Example Use Cases for bruteForce and kadanes
nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
nums2 = [1, 2, 3, -2, 5]

# Example Use Cases for closeDuplicatesBruteForce and closeDuplicatesSlidingWindow
nums3 = [1, 2, 3, 1, 4, 5]
nums4 = [1, 2, 3, 4, 5]

# Example Use Cases for longestSubarray and shortestSubarray
nums5 = [1, 2, 3, 2, 1]
nums6 = [3, 2, 1, 4, 5]
target1 = 7
target2 = 11

# Example Use Cases for isPalindrome and targetSum
word1 = "radar"
word2 = "hello"
nums7 = [2, 7, 11, 15]
target3 = 9

# Example Use Cases for PrefixSum
nums8 = [1, 2, 3, 4, 5]

# Using Kadane's Algorithm
result_kadanes_1 = kadanes(nums1)
result_kadanes_2 = kadanes(nums2)

# Using Sliding Window Technique
result_sliding_1 = slidingWindow(nums1)
result_sliding_2 = slidingWindow(nums2)

# Using closeDuplicatesBruteForce
result_bruteforce_1 = closeDuplicatesBruteForce(nums3, 3)
result_bruteforce_2 = closeDuplicatesBruteForce(nums4, 3)

# Using closeDuplicatesSlidingWindow
result_slidingwindow_1 = closeDuplicatesSlidingWindow(nums3, 3)
result_slidingwindow_2 = closeDuplicatesSlidingWindow(nums4, 3)

# Using longestSubarray
result_longest_1 = longestSubarray(nums1)
result_longest_2 = longestSubarray(nums2)

# Using shortestSubarray
result_shortest_1 = shortestSubarray(nums1, target1)
result_shortest_2 = shortestSubarray(nums2, target2)

# Using isPalindrome
result_palindrome_1 = isPalindrome(word1)
result_palindrome_2 = isPalindrome(word2)

# Using targetSum
result_targetsum = targetSum(nums7, target3)

# Create a PrefixSum object
prefix_sum = PrefixSum(nums8)

# Calculate range sums using the rangeSum method
result_range_sum_1 = prefix_sum.rangeSum(1, 3)
result_range_sum_2 = prefix_sum.rangeSum(2, 4)

# Displaying Results
print("Kadane's Algorithm:")
print(f"Input: {nums1}, Result: {result_kadanes_1}")
print(f"Input: {nums2}, Result: {result_kadanes_2}")

print("\nSliding Window Technique:")
print(f"Input: {nums1}, Result: {result_sliding_1}")
print(f"Input: {nums2}, Result: {result_sliding_2}")

print("\nClose Duplicates - Brute Force:")
print(f"Input: {nums3}, k: 3, Result: {result_bruteforce_1}")
print(f"Input: {nums4}, k: 3, Result: {result_bruteforce_2}")

print("\nClose Duplicates - Sliding Window:")
print(f"Input: {nums3}, k: 3, Result: {result_slidingwindow_1}")
print(f"Input: {nums4}, k: 3, Result: {result_slidingwindow_2}")

print("Longest Subarray:")
print(f"Input: {nums1}, Result: {result_longest_1}")
print(f"Input: {nums2}, Result: {result_longest_2}")

print("\nShortest Subarray:")
print(f"Input: {nums1}, Target: {target1}, Result: {result_shortest_1}")
print(f"Input: {nums2}, Target: {target2}, Result: {result_shortest_2}")

print("Is Palindrome:")
print(f"Input: '{word1}', Result: {result_palindrome_1}")
print(f"Input: '{word2}', Result: {result_palindrome_2}")

print("\nTarget Sum:")
print(f"Input: {nums7}, Target: {target3}, Result: {result_targetsum}")

print("PrefixSum:")
print(f"Input: {nums8}")
print(f"Range Sum [1, 3]: {result_range_sum_1}")
print(f"Range Sum [2, 4]: {result_range_sum_2}")
