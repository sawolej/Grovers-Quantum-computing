from multitarget import multi_target_grover
from classicGrover import classic_grover
import random
def random_binary_arrays(n, x_bits):
    # Initialize the result list
    arrays = []

    # Loop n times
    for _ in range(n):
        num_range = 2**x_bits - 1

        num = random.randint(0, num_range)

        binary = bin(num)[2:]

        binary = binary.zfill(x_bits)

        arrays.append([int(bit) for bit in binary])

    # Return the list of lists
    return arrays

def main():
    print(random_binary_arrays(2, 4))

    # multi_target_grover()
    # classic_grover()

main()