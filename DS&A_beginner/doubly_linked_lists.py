class ListNode:
    def __init__(self, val):
        """
        Definition for a doubly linked list node.

        Parameters:
        - val: The value of the node.
        """
        self.val = val
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        """
        Implementation of a doubly linked list.

        Attributes:
        - head: The head of the linked list, initialized with a dummy node.
        - tail: The tail of the linked list, initialized with a dummy node.
        """
        self.head = ListNode(-1)    # Initialize the head with a dummy node (sentinel)
        self.tail = ListNode(-1)    # Initialize the tail with a dummy node (sentinel)
        self.head.next = self.tail  # Connect the head to the tail
        self.tail.prev = self.head  # Connect the tail to the head

    def insertFront(self, val):
        """
        Insert a new node with the given value at the front of the linked list.

        Parameters:
        - val: The value to be inserted.
        """
        newNode = ListNode(val)     # Create a new node with the given value
        newNode.prev = self.head    # Set the new node's previous pointer to the head
        newNode.next = self.head.next  # Set the new node's next pointer to the node after the head

        self.head.next.prev = newNode   # Update the previous pointer of the next node after the head
        self.head.next = newNode        # Update the next pointer of the head to the new node

    def insertEnd(self, val):
        """
        Insert a new node with the given value at the end of the linked list.

        Parameters:
        - val: The value to be inserted.
        """
        newNode = ListNode(val)     # Create a new node with the given value
        newNode.next = self.tail    # Set the new node's next pointer to the tail
        newNode.prev = self.tail.prev  # Set the new node's previous pointer to the node before the tail

        self.tail.prev.next = newNode   # Update the next pointer of the previous node before the tail
        self.tail.prev = newNode        # Update the previous pointer of the tail to the new node

    def removeFront(self):
        """
        Remove the first node after the dummy head (assume it exists).
        """
        self.head.next.next.prev = self.head  # Update the previous pointer of the second node
        self.head.next = self.head.next.next  # Update the next pointer of the head

    def removeEnd(self):
        """
        Remove the last node before the dummy tail (assume it exists).
        """
        self.tail.prev.prev.next = self.tail  # Update the next pointer of the second-to-last node
        self.tail.prev = self.tail.prev.prev  # Update the previous pointer of the tail

    def print(self):
        """
        Print the elements of the linked list.
        """
        curr = self.head.next   # Start from the node after the head
        while curr != self.tail:  # Iterate until the tail is reached
            print(curr.val, " -> ")   # Print the value of the current node
            curr = curr.next   # Move to the next node
        print()


# Example Usage:

# Create a doubly linked list
dll = LinkedList()

# Insert elements at the front
dll.insertFront(1)
dll.insertFront(2)
dll.insertFront(3)

print("Original Doubly Linked List:")
dll.print()

# Remove the front element
dll.removeFront()

print("Doubly Linked List after removing the front element:")
dll.print()

# Insert elements at the end
dll.insertEnd(4)
dll.insertEnd(5)

print("Doubly Linked List after inserting elements at the end:")
dll.print()

# Remove the end element
dll.removeEnd()

print("Doubly Linked List after removing the end element:")
dll.print()
