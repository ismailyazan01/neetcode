class Recursion:
    def factorial(self, num):
        """
        Calculate the factorial of a non-negative integer using recursion.

        Parameters:
        - num (int): The non-negative integer for which to calculate the factorial.

        Returns:
        - int: The factorial of the input number.
        """
        if num <= 1:
            return 1

        return num * self.factorial(num - 1)

    def fibonacciSequence(self, num):
        """
        Generate the Fibonacci sequence up to the nth term using recursion.

        Parameters:
        - num (int): The non-negative integer specifying the term in the Fibonacci sequence.

        Returns:
        - int: The value of the Fibonacci sequence at the specified term.
        """
        if num <= 1:
            return num

        return self.fibonacciSequence(num - 1) + self.fibonacciSequence(num - 2)


# Example Usage:
recursion = Recursion()

# Factorial
num_factorial = 5
print(f"Factorial of {num_factorial}: {recursion.factorial(num_factorial)}")

# Fibonacci Sequence
num_fibonacci = 6
print(f"Fibonacci Sequence at term {num_fibonacci}: {recursion.fibonacciSequence(num_fibonacci)}")
