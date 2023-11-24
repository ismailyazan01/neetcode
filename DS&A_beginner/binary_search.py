class BinarySearch:
    def binarySearch(self, arr, target):
        """
        Perform binary search on a sorted array to find the target element.

        Parameters:
        - arr (list): The sorted input array.
        - target: The target element to search for.

        Returns:
        - int: The index of the target element if found, otherwise -1.
        """
        # Initialize the left and right pointers
        l = 0
        r = len(arr) - 1

        # Continue the search as long as the left pointer is less than or equal to the right pointer
        while l <= r:
            # Calculate the middle index
            m = (l + r) // 2

            # Check if the middle element is greater than the target
            if arr[m] > target:
                r = m - 1  # Adjust the right pointer
            # Check if the middle element is less than the target
            elif arr[m] < target:
                l = m + 1  # Adjust the left pointer
            else:
                return m  # Target found, return the index

        return -1  # Target not found, return -1

    def binarySearchRange(self, low, upp):
        """
        Perform binary search on a range to find a specific condition.

        Parameters:
        - low: The lower bound of the search range.
        - upp: The upper bound of the search range.

        Returns:
        - int: The result of the search or -1 if not found.
        """
        # Continue the search as long as the lower bound is less than or equal to the upper bound
        while low <= upp:
            # Calculate the middle value
            mid = (low + upp) // 2

            # Check the condition using the isCorrect method
            if self.isCorrect(mid) > 0:
                upp = mid - 1  # Adjust the upper bound
            elif self.isCorrect(mid) < 0:
                low = mid + 1  # Adjust the lower bound
            else:
                return mid  # Condition satisfied, return the result

        return -1  # Condition not satisfied, return -1

    def isCorrect(self, n):
        """
        Check if a given number is correct based on a predefined condition.

        Parameters:
        - n: The number to check.

        Returns:
        - int: 1 if n is greater than the correct number, -1 if less, 0 if equal.
        """
        numGuessAns = 10

        # Compare the given number with the correct answer
        if n > numGuessAns:
            return 1  # Given number is greater
        elif n < numGuessAns:
            return -1  # Given number is less
        else:
            return 0  # Given number is equal to the correct answer


# Example usage:
bs = BinarySearch()

# Binary Search
result_index = bs.binarySearch([1, 3, 5, 7, 12, 152, 158, 198, 199, 200, 201, 212], 212)
print(f"Binary Search Result: Element found at index {result_index}")

# Binary Search Range
result = bs.binarySearchRange(1, 20)
print(f"Binary Search Range Result: {result}")
