class Heap:
    def __init__(self):
        """
        Implementation of a min-heap using an array.

        Attributes:
        - heap (list): The list used to represent the heap. The first element (index 0) is not used.
        """
        self.heap = [0]

    def push(self, val):
        """
        Add an element to the heap and maintain the heap property.

        Parameters:
        - val: The value to be added to the heap.
        """
        self.heap.append(val)
        i = len(self.heap) - 1

        while i > 1 and self.heap[i] < self.heap[i // 2]:
            temp = self.heap[i]
            self.heap[i] = self.heap[i // 2]
            self.heap[i // 2] = temp
            i = i // 2

    def pop(self):
        """
        Remove and return the smallest element from the heap, and maintain the heap property.

        Returns:
        - The smallest value from the heap.
        """
        if len(self.heap) == 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()

        popped = self.heap[1]
        self.heap[1] = self.heap.pop()
        self.percolate(1)
        return popped

    def top(self):
        """
        Return the smallest element from the heap without removing it.

        Returns:
        - The smallest value from the heap.
        """
        if len(self.heap) > 1:
            return self.heap[1]
        return None

    def heapify(self, arr):
        """
        Build a heap from a given array.

        Parameters:
        - arr (list): The array from which to build the heap.
        """
        arr.append(arr[0])
        self.heap = arr
        curr = (len(self.heap) - 1) // 2
        while curr > 0:
            self.percolate(curr)
            curr -= 1

    def percolate(self, i):
        """
        Maintain the heap property starting from the given index.

        Parameters:
        - i (int): The index from which to percolate down.
        """
        while i * 2 < len(self.heap):
            left_child_index = i * 2
            right_child_index = i * 2 + 1
            smallest = i

            if (
                right_child_index < len(self.heap)
                and self.heap[right_child_index] < self.heap[smallest]
            ):
                smallest = right_child_index

            if self.heap[left_child_index] < self.heap[smallest]:
                temp = self.heap[i]
                self.heap[i] = self.heap[left_child_index]
                self.heap[left_child_index] = temp
                i = left_child_index
            else:
                break


# Example Usage:

# Create a heap
heap = Heap()

# Push elements onto the heap
heap.push(3)
heap.push(1)
heap.push(4)
heap.push(2)

print("Original Min-Heap:")
print(heap.heap[1:])

# Pop the smallest element from the heap
popped_value = heap.pop()
print(f"Popped Value: {popped_value}")
print("Heap after Pop:")
print(heap.heap[1:])

# Return the smallest element without removing it
top_value = heap.top()
print(f"Top Value: {top_value}")

# Build a heap from an array
arr = [7, 2, 9, 1, 5]
heap.heapify(arr)
print("Min-Heap after Heapify:")
print(heap.heap[1:])
