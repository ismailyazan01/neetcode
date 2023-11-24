class Sorting:
    def insertionSort(self, arr):
        """
        Perform insertion sort on a list of comparable elements.

        Parameters:
        - arr (list): The input list to be sorted.

        Returns:
        - list: The sorted list.
        """
        for i in range(1, len(arr)):
            j = i - 1  # Set the index `j` to the element before the current `i`.
            while j >= 0 and arr[j + 1] < arr[j]:
                tmp = arr[j + 1]  # Temporary variable to hold the value of the element at `j + 1`.
                arr[j + 1] = arr[j]  # Swap the element at `j + 1` with the element at `j`.
                arr[j] = tmp  # Place the originally larger element at `j + 1` in the correct position.
                j -= 1  # Move to the previous index to continue the comparison.
        return arr  # Return the sorted array.

    def mergeSort(self, arr, s, e):
        """
        Perform merge sort on a list of comparable elements.

        Parameters:
        - arr (list): The input list to be sorted.
        - s (int): Starting index of the subarray to be sorted.
        - e (int): Ending index of the subarray to be sorted.

        Returns:
        - list: The sorted list.
        """
        if e - s + 1 <= 1:
            return arr  # If the subarray has one or zero elements, it is considered sorted.

        m = (e + s) // 2  # Calculate the middle index of the subarray.

        self.mergeSort(arr, s, m)  # Recursively call mergeSort on the left half of the subarray.
        self.mergeSort(arr, m + 1, e)  # Recursively call mergeSort on the right half of the subarray.
        self.merge(arr, s, m, e)  # Merge the sorted left and right halves of the subarray.

        return arr  # Return the fully sorted array.

    def merge(self, arr, s, m, e):
        """
        Merge two sorted subarrays into a single sorted array.

        Parameters:
        - arr (list): The input list containing two sorted subarrays.
        - s (int): Starting index of the first subarray.
        - m (int): Ending index of the first subarray.
        - e (int): Ending index of the second subarray.
        """
        L = arr[s: m + 1]  # Create a left subarray from index s to m (inclusive).
        R = arr[m + 1: e + 1]  # Create a right subarray from index m + 1 to e (inclusive).

        l, r, k = 0, 0, s  # Initialize indices l, r, and k for the left subarray, right subarray, and the merged array, respectively.

        while l < len(L) and r < len(R):
            if L[l] <= R[r]:
                arr[k] = L[l]  # If the current element in the left subarray is less than or equal to the right subarray, assign it to the merged array.
                l += 1
            else:
                arr[k] = R[r]  # If the current element in the right subarray is less than the left subarray, assign it to the merged array.
                r += 1
            k += 1  # Move to the next index in the merged array.

        while l < len(L):
            arr[k] = L[l]  # If there are remaining elements in the left subarray, add them to the merged array.
            l += 1
            k += 1

        while r < len(R):
            arr[k] = R[r]  # If there are remaining elements in the right subarray, add them to the merged array.
            r += 1
            k += 1

    def quickSort(self, arr, s, e):
        """
        Perform quick sort on a list of comparable elements.

        Parameters:
        - arr (list): The input list to be sorted.
        - s (int): Starting index of the subarray to be sorted.
        - e (int): Ending index of the subarray to be sorted.

        Returns:
        - list: The sorted list.
        """
        if e - s + 1 <= 1:
            return arr  # If the subarray has one or zero elements, it is already sorted.

        pivot = arr[e]  # Choose the last element of the subarray as the pivot.
        left = s  # Initialize a pointer for the left side of the subarray.

        for i in range(s, e):
            if arr[i] < pivot:
                temp = arr[left]  # Store the value at the left pointer in a temporary variable.
                arr[left] = arr[i]  # Replace the value at the left pointer with the current element.
                arr[i] = temp  # Place the stored value (temp) in the position of the current element.
                left += 1  # Move the left pointer to the right, as the smaller element is now correctly placed.

        arr[e] = arr[left]  # Swap the pivot with the element at the position of the left pointer.
        arr[left] = pivot

        self.quickSort(arr, s, left - 1)  # Recursively apply quick sort to the left subarray.
        self.quickSort(arr, left + 1, e)  # Recursively apply quick sort to the right subarray.

        return arr

    def bucketSort(self, arr, numBuckets):
        """
        Perform bucket sort on a list of non-negative integers.

        Parameters:
        - arr (list): The input list to be sorted.
        - numBuckets (int): The number of buckets to use for sorting.

        Returns:
        - list: The sorted list.
        """
        counts = [0] * numBuckets  # Initialize an array 'counts' to store the count of elements in each bucket.

        for n in arr:
            counts[n] += 1  # Count the occurrences of each element in the input array and update the 'counts' array.

        i = 0  # Initialize the index 'i' for iterating through the input array.

        for n in range(len(counts)):
            for j in range(counts[n]):
                arr[i] = n  # Replace the elements in the input array with sorted elements from the buckets.
                i += 1  # Move to the next position in the input array.
        return arr


# Example Usage:
sorting = Sorting()

# Insertion Sort
arr_insertion = [64, 34, 25, 12, 22, 11, 90]
print("Insertion Sort:", sorting.insertionSort(arr_insertion))

# Merge Sort
arr_merge = [64, 34, 25, 12, 22, 11, 90]
print("Merge Sort:", sorting.mergeSort(arr_merge, 0, len(arr_merge) - 1))

# Quick Sort
arr_quick = [64, 34, 25, 12, 22, 11, 90]
print("Quick Sort:", sorting.quickSort(arr_quick, 0, len(arr_quick) - 1))

# Bucket Sort
arr_bucket = [64, 34, 25, 12, 22, 11, 90]
num_buckets = 10
print("Bucket Sort:", sorting.bucketSort(arr_bucket, num_buckets))
