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
        l = 0
        r = len(arr) - 1

        while l <= r:
            m = (l + r) // 2

            if arr[m] > target:
                r = m - 1
            elif arr[m] < target:
                l = m + 1
            else:
                return m

        return -1

    def binarySearchRange(self, low, upp):
        """
        Perform binary search on a range to find a specific condition.

        Parameters:
        - low: The lower bound of the search range.
        - upp: The upper bound of the search range.

        Returns:
        - int: The result of the search or -1 if not found.
        """
        while low <= upp:
            mid = (low + upp) // 2

            if self.isCorrect(mid) > 0:
                upp = mid - 1
            elif self.isCorrect(mid) < 0:
                low = mid + 1
            else:
                return mid

        return -1

    def isCorrect(self, n):
        """
        Check if a given number is correct based on a predefined condition.

        Parameters:
        - n: The number to check.

        Returns:
        - int: 1 if n is greater than the correct number, -1 if less, 0 if equal.
        """
        numGuessAns = 10

        if n > numGuessAns:
            return 1
        elif n < numGuessAns:
            return -1
        else:
            return 0


# Example usage:
bs = BinarySearch()
result_index = bs.binarySearch([1, 3, 5, 7, 12, 152, 158, 198, 199, 200, 201, 212], 212)
print(f"Binary Search Result: Element found at index {result_index}")

result = bs.binarySearchRange(1, 20)
print(f"Binary Search Range Result: {result}")
