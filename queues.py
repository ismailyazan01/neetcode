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
        self.left = self.right = None

    def enqueue(self, val):
        """
        Add an element to the rear of the queue.

        Parameters:
        - val: The value to be added to the queue.
        """
        newNode = ListNode(val)

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
            return None

        val = self.left.val
        self.left = self.left.next
        if not self.left:
            self.right = None
        return val

    def print(self):
        """
        Print the elements of the queue.
        """
        cur = self.left
        while cur:
            print(cur.val, ' -> ', end="")
            cur = cur.next
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
