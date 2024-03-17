def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_largest_integer(filename):
    integers = []
    cur_number = ''
    with open(filename, 'r') as file:
        for line in file:
            for char in line:
                if char.isdigit():
                    cur_number += char
                elif cur_number != '':
                    integers.append(int(cur_number))
                    cur_number = ''
    return max(integers)

def generate_prime_numbers_up_to(n):
    primes = [i for i in range(2, n + 1) if is_prime(i)]
    return primes

def find_smallest_prime(primes):
    return min(primes)

def find_largest_prime(primes):
    return max(primes)

def write_prime_numbers_to_file(primes, filename, prime_sum, largest_prime, smallest_prime, largest_integer_is_prime):
    with open(filename, 'w') as file:
        file.write("List of Prime Numbers:\n")
        file.write(', '.join(map(str, primes)) + '\n')
        file.write(f"Sum of Prime Numbers: {prime_sum}\n")
        file.write(f"Largest Prime Number: {largest_prime}\n")
        file.write(f"Smallest Prime Number: {smallest_prime}\n")
        file.write(f"Is the Largest Integer Prime: {largest_integer_is_prime}\n")

output_filename = "output.txt"
prime_numbers_filename = "prime_numbers.txt"

try:
    largest_integer = find_largest_integer(output_filename)
    if largest_integer is None:
        raise ValueError("No integers found in the file.")

    primes = generate_prime_numbers_up_to(largest_integer)
    prime_sum = sum(primes)
    smallest_prime = find_smallest_prime(primes)
    largest_prime = find_largest_prime(primes)
    largest_integer_is_prime = is_prime(largest_integer)

    write_prime_numbers_to_file(primes, prime_numbers_filename, prime_sum, largest_prime, smallest_prime, largest_integer_is_prime)

    print("Prime numbers list along with sum, largest, and smallest prime numbers written to 'prime_numbers.txt'.")

except FileNotFoundError:
    print(f"File '{output_filename}' not found.")

except ValueError as ve:
    print(ve)

except Exception as e:
    print(f"An error occurred: {e}")
