def validate_number(n):
    if not isinstance(n, (int, float)):
        raise ValueError("Invalid input: Not a number")
    if n < 0:
        raise ValueError("Invalid input: Negative number")