def is_prime(n):
    """Check if a number n is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
input_number = int(input("Enter a number to check if it's prime: "))
if is_prime(input_number):
    print(f"True: {input_number} is a prime number.")
else:
    print(f"False: {input_number} is not a prime number.")

    