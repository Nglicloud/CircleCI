def multiply_and_check_odd_even(a, b):
    # Multiplication
    result = a * b
    
    # Check if the result is odd or even
    if result % 2 == 0:
        return result, "even"
    else:
        return result, "odd"

if __name__ == "__main__":
    # Example usage
    a = 8
    b = 7
    result, parity = multiply_and_check_odd_even(a, b)
    print(f"The result of multiplying {a} and {b} is {result}, which is {parity}.")
