class Stack:
    def __init__(self):
        """
        Implementation of a stack using a list.

        Attributes:
        - stack (list): The list used to represent the stack.
        """
        self.stack = []

    def push(self, n):
        """
        Add an element to the top of the stack.

        Parameters:
        - n: The value to be added to the stack.
        """
        self.stack.append(n)

    def pop(self):
        """
        Remove and return the element from the top of the stack.

        Returns:
        - The value of the element removed from the top of the stack.
        """
        return self.stack.pop()


# Example Usage:

# Create a stack
stack = Stack()

# Push elements onto the stack
stack.push(1)
stack.push(2)
stack.push(3)

print("Original Stack:")
print(stack.stack)

# Pop an element from the stack
popped_value = stack.pop()
print(f"Popped Value: {popped_value}")

print("Stack after Pop:")
print(stack.stack)
