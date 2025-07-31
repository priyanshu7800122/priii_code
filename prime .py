# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False  # 0 and 1 are not prime
    elif n == 2:
        return True  # 2 is the only even prime
    elif n % 2 == 0:
        return False  # other even numbers are not prime
    
    # Check for factors from 3 to sqrt(n)
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Input from user
num = int(input("Enter a number to check if it's prime: "))

# Output result
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
