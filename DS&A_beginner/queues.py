class ListNode:
    def __init__(self, val):
        """
        Definition for a singly linked list node.

        Parameters:
        - val: The value of the node.
        """
        self.val = val
        self.next = None


class Queue:
    def __init__(self):
        """
        Implementation of a simple queue using a linked list.

        Attributes:
        - left: The front of the queue.
        - right: The rear of the queue.
        """
        self.left = self.right = None  # Initialize front and rear as None

    def enqueue(self, val):
        """
        Add an element to the rear of the queue.

        Parameters:
        - val: The value to be added to the queue.
        """
        newNode = ListNode(val)  # Create a new node with the given value

        # If the queue is not empty, link the current rear to the new node
        # Update the rear to the new node
        # If the queue is empty, set both front and rear to the new node
        if self.right:
            self.right.next = newNode
            self.right = self.right.next
        else:
            self.left = self.right = newNode

    def dequeue(self):
        """
        Remove and return the element from the front of the queue.

        Returns:
        - The value of the element removed from the front of the queue.
        """
        if not self.left:
            return None  # If the queue is empty, return None

        val = self.left.val  # Get the value of the front element
        self.left = self.left.next  # Move the front to the next element
        if not self.left:
            self.right = None  # If the queue becomes empty, update the rear to None
        return val

    def print(self):
        """
        Print the elements of the queue.
        """
        cur = self.left  # Start from the front of the queue
        while cur:
            print(cur.val, ' -> ', end="")  # Print the value of the current node
            cur = cur.next  # Move to the next node
        print()


# Example Usage:

# Create a queue
queue = Queue()

# Enqueue elements
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Original Queue:")
queue.print()

# Dequeue an element
dequeued_value = queue.dequeue()
print(f"Dequeued Value: {dequeued_value}")

print("Queue after Dequeue:")
queue.print()
