# factorial_module.py

def factorial_iterative(n: int) -> int:
    """
    Compute the factorial of a non-negative integer using iterative method.

    Args:
        n (int): The integer for which factorial is to be computed.

    Returns:
        int: The factorial of n.

    Raises:
        ValueError: If n is negative.

    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

def factorial_recursion(n: int) -> int:
    """
    Compute the factorial of a non-negative integer using recursion.

    Args:
        n (int): The integer for which factorial is to be computed.

    Returns:
        int: The factorial of n.

    Raises:
        ValueError: If n is negative.

    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    if n == 0:
        return 1
    return n * factorial_recursion(n - 1)

def clumsy(n):
    """
    Compute the "clumsy factorial" of a non-negative integer using a specific pattern.

    The clumsy factorial is defined such that:
    - clumsy(0) = 0
    - clumsy(1) = 1
    - clumsy(2) = 2
    - clumsy(3) = 6
    For n >= 4, it follows the pattern:
    clumsy(n) = n * (n - 1) // (n - 2) + (n - 3) - clumsy(n - 4)

    Args:
        n (int): The integer for which clumsy factorial is to be computed.

    Returns:
        int: The clumsy factorial of n.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.

    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be non-negative")

    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 6
    else:
        result = n * (n - 1) // (n - 2) + (n - 3)
        n -= 4
        while n >= 4:
            result -= n * (n - 1) // (n - 2)
            result += (n - 3)
            n -= 4
        if n == 1:
            return result - 1
        elif n == 2:
            return result - 2
        elif n == 3:
            return result - 6
        else:
            return result
