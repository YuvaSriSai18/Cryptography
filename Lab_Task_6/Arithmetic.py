def big_integer_operations(a, b, mod=None):
    # Addition
    addition = a + b

    # Subtraction
    subtraction = a - b

    # Multiplication
    multiplication = a * b

    # Division (floating-point)
    division = a / b

    # Integer Division
    integer_division = a // b

    # Modular Division (if mod is provided)
    modular_division = None
    if mod is not None:
        modular_division = pow(a, -1, mod) * b % mod if b != 0 else None  # Modular inverse exists only if GCD(a, mod) = 1

    return {
        "Addition": addition,
        "Subtraction": subtraction,
        "Multiplication": multiplication,
        "Division": division,
        "Integer Division": integer_division,
        "Modular Division": modular_division
    }


# Example
a = 182841384165841685416854134135
b = 135481653441354138548413384135
mod = 1000000007  # Example modulus for modular division

results = big_integer_operations(a, b, mod)
for key, value in results.items():
    print(f"{key}: {value}")
