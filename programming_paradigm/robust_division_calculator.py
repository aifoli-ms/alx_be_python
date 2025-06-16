# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Safely divide two numbers with error handling.

    Args:
        numerator: The numerator (as a string or number).
        denominator: The denominator (as a string or number).

    Returns:
        A string containing the result or an error message.
    """
    try:
        num = float(numerator)
        denom = float(denominator)
        result = num / denom
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."