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
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insertFront(self, val):
        """
        Insert a new node with the given value at the front of the linked list.

        Parameters:
        - val: The value to be inserted.
        """
        newNode = ListNode(val)
        newNode.prev = self.head
        newNode.next = self.head.next

        self.head.next.prev = newNode
        self.head.next = newNode

    def insertEnd(self, val):
        """
        Insert a new node with the given value at the end of the linked list.

        Parameters:
        - val: The value to be inserted.
        """
        newNode = ListNode(val)
        newNode.next = self.tail
        newNode.prev = self.tail.prev

        self.tail.prev.next = newNode
        self.tail.prev = newNode

    def removeFront(self):
        """
        Remove the first node after the dummy head (assume it exists).
        """
        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next

    def removeEnd(self):
        """
        Remove the last node before the dummy tail (assume it exists).
        """
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev

    def print(self):
        """
        Print the elements of the linked list.
        """
        curr = self.head.next
        while curr != self.tail:
            print(curr.val, " -> ")
            curr = curr.next
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
