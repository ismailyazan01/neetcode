class ListNode:
    def __init__(self, val):
        """
        Definition for a singly linked list node.

        Parameters:
        - val: The value of the node.
        """
        self.val = val
        self.next = None


class LinkedLists:
    def __init__(self):
        """
        Implementation of a singly linked list.

        Attributes:
        - head: The head of the linked list, initialized with a dummy node.
        - tail: The tail of the linked list, initially set to the dummy node.
        """
        self.head = ListNode(-1)
        self.tail = self.head

    def insertEnd(self, val):
        """
        Insert a new node with the given value at the end of the linked list.

        Parameters:
        - val: The value to be inserted.
        """
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index):
        """
        Remove a node at the specified index in the linked list.

        Parameters:
        - index: The index of the node to be removed.
        """
        i = 0
        curr = self.head
        while i < index and curr:
            i += 1
            curr = curr.next

        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next

    def print(self):
        """
        Print the elements of the linked list.
        """
        curr = self.head.next
        while curr:
            print(curr.val, " -> ", end="")
            curr = curr.next
        print()


# Example Usage:

# Create a singly linked list
sll = LinkedLists()

# Insert elements at the end
sll.insertEnd(1)
sll.insertEnd(2)
sll.insertEnd(3)

print("Original Linked List:")
sll.print()

# Remove element at index 1
sll.remove(1)

print("Linked List after removing element at index 1:")
sll.print()
