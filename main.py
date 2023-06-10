from multitarget import multi_target_grover
from classicGrover import classic_grover
import random


def random_binary_arrays(n, x_bits):

    arrays = set()

    while len(arrays) < n:
        num_range = 2**x_bits - 1

        num = random.randint(0, num_range)

        binary = bin(num)[2:]

        binary = binary.zfill(x_bits)

        binary_tuple = tuple(int(bit) for bit in binary)

        arrays.add(binary_tuple)

    return [list(array) for array in arrays]

def main():
    qubits = 4
    num_targets = 4
    targets =random_binary_arrays(num_targets,qubits)
    print(targets)

    multi_target_grover(targets)
    # classic_grover()

main()