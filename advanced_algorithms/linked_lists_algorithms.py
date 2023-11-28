class ListNode:
    def __init__(self, val=None):
        """
        Initializes a ListNode object with a given value.

        Parameters:
        - val (int, optional): Value of the node. Defaults to None.

        Returns:
        - None
        """
        self.val = val
        self.next = None

    def middleOfList(self, head):
        """
        Finds the middle node of a linked list.

        Parameters:
        - head (ListNode): Head of the linked list.

        Returns:
        - ListNode: Middle node of the linked list.
        """
        # Initialize two pointers, slow and fast, both starting at the head
        slow = fast = head

        # Move slow one step at a time, and fast two steps at a time
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Return the slow pointer, which is now at the middle of the list
        return slow

    def hasCycle(self, head):
        """
        Checks if a linked list has a cycle.

        Parameters:
        - head (ListNode): Head of the linked list.

        Returns:
        - bool: True if the linked list has a cycle, False otherwise.
        """
        # Initialize two pointers, slow and fast, both starting at the head
        slow, fast = head, head

        # Move slow one step at a time, and fast two steps at a time
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # If there's a cycle, the slow and fast pointers will meet
            if slow == fast:
                return True

        # If there's no cycle, return False
        return False

    def cycleStart(self, head):
        """
        Finds the starting node of a cycle in a linked list.

        Parameters:
        - head (ListNode): Head of the linked list.

        Returns:
        - ListNode: Starting node of the cycle, or None if there's no cycle.
        """
        # Initialize two pointers, slow and fast, both starting at the head
        slow, fast = head, head

        # Move slow one step at a time, and fast two steps at a time
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # If there's a cycle, break the loop
            if slow == fast:
                break

        # If there's no cycle, return None
        if not fast or not fast.next:
            return None

        # Move slow2 to the head and advance both slow and slow2 one step at a time
        slow2 = head
        while slow != slow2:
            slow = slow.next
            slow2 = slow2.next

        # Return the node where the two pointers meet, which is the start of the cycle
        return slow


# Example Use Cases for ListNode methods
# Creating linked list with a cycle
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node2  # Creating a cycle

# Creating a linked list without a cycle
nodeA = ListNode('A')
nodeB = ListNode('B')
nodeC = ListNode('C')

nodeA.next = nodeB
nodeB.next = nodeC

# Create a ListNode object without specifying a value (val defaults to None)
list_node = ListNode()

# Use middleOfList method
middle_node = list_node.middleOfList(nodeA)

# Use hasCycle method
has_cycle_1 = list_node.hasCycle(nodeA)
has_cycle_2 = list_node.hasCycle(node1)

# Use cycleStart method
cycle_start_node_1 = list_node.cycleStart(nodeA)
cycle_start_node_2 = list_node.cycleStart(node1)

# Displaying Results
print("Middle of List:")
print(f"Input: {nodeA.val} -> {nodeB.val} -> {nodeC.val}, Result: {middle_node.val}")

print("\nHas Cycle:")
print(f"Input: {nodeA.val} -> {nodeB.val} -> {nodeC.val}, Result: {has_cycle_1}")
print(f"Input: {node1.val} -> {node2.val} -> {node3.val} -> {node4.val} -> \
    {node5.val} (with cycle), Result: {has_cycle_2}")

print("\nCycle Start:")
if cycle_start_node_1 is not None:
    print(f"Input: {nodeA.val} -> {nodeB.val} -> {nodeC.val}, Result: {cycle_start_node_1.val}")
else:
    print(f"Input: {nodeA.val} -> {nodeB.val} -> {nodeC.val}, Result: No cycle")

if cycle_start_node_2 is not None:
    print(f"Input: {node1.val} -> {node2.val} -> {node3.val} -> {node4.val} -> \
        {node5.val} (with cycle), Result: {cycle_start_node_2.val}")
else:
    print(f"Input: {node1.val} -> {node2.val} -> {node3.val} -> {node4.val} -> \
        {node5.val} (with cycle), Result: No cycle")
