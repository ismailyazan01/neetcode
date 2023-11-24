class Stack:
    def __init__(self):
        """
        Implementation of a stack using a list.

        Attributes:
        - stack (list): The list used to represent the stack.
        """
        self.stack = []  # Initialize an empty list to serve as the stack.

    def push(self, n):
        """
        Add an element to the top of the stack.

        Parameters:
        - n: The value to be added to the stack.
        """
        self.stack.append(n)  # Append the specified value 'n' to the end of the list, representing the addition to the top of the stack.

    def pop(self):
        """
        Remove and return the element from the top of the stack.

        Returns:
        - The value of the element removed from the top of the stack.
        """
        return self.stack.pop()  # Remove and return the last element from the list, simulating the removal of the top element from the stack.


# Example Usage:

# Create a stack
stack = Stack()  # Instantiate an object of the Stack class, creating a new stack using the defined methods.

# Push elements onto the stack
stack.push(1)  # Add the value 1 to the top of the stack.
stack.push(2)  # Add the value 2 to the top of the stack.
stack.push(3)  # Add the value 3 to the top of the stack.

print("Original Stack:")
print(stack.stack)  # Print the current state of the stack.

# Pop an element from the stack
popped_value = stack.pop()  # Remove and retrieve the top element from the stack.
print(f"Popped Value: {popped_value}")  # Print the value of the removed element.

print("Stack after Pop:")
print(stack.stack)  # Print the current state of the stack after the pop operation.
