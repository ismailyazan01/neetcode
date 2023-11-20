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
            j = i - 1
            while j >= 0 and arr[j + 1] < arr[j]:
                tmp = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = tmp
                j -= 1
        return arr

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
            return arr

        m = (e + s) // 2

        self.mergeSort(arr, s, m)
        self.mergeSort(arr, m + 1, e)
        self.merge(arr, s, m, e)

        return arr

    def merge(self, arr, s, m, e):
        """
        Merge two sorted subarrays into a single sorted array.

        Parameters:
        - arr (list): The input list containing two sorted subarrays.
        - s (int): Starting index of the first subarray.
        - m (int): Ending index of the first subarray.
        - e (int): Ending index of the second subarray.
        """
        L = arr[s: m + 1]
        R = arr[m + 1: e + 1]

        l, r, k = 0, 0, s

        while l < len(L) and r < len(R):
            if L[l] <= R[r]:
                arr[k] = L[l]
                l += 1
            else:
                arr[k] = R[r]
                r += 1
            k += 1

        while l < len(L):
            arr[k] = L[l]
            l += 1
            k += 1

        while r < len(R):
            arr[k] = R[r]
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
            return arr

        pivot = arr[e]
        left = s

        for i in range(s, e):
            if arr[i] < pivot:
                temp = arr[left]
                arr[left] = arr[i]
                arr[i] = temp
                left += 1

        arr[e] = arr[left]
        arr[left] = pivot

        self.quickSort(arr, s, left - 1)
        self.quickSort(arr, left + 1, e)

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
        counts = [0] * numBuckets

        for n in arr:
            counts[n] += 1

        i = 0
        for n in range(len(counts)):
            for j in range(counts[n]):
                arr[i] = n
                i += 1
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
