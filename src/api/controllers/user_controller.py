def add_numbers(a, b):
    """
    Function to add two numbers.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The sum of the two numbers.
    """
    return a + b

# Example usage
if __name__ == "__main__":
    num1 = 5
    num2 = 10
    result = add_numbers(num1, num2)
    print(f"The sum of {num1} and {num2} is {result}")