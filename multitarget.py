from qiskit import QuantumCircuit, Aer, execute
import matplotlib.pyplot as plt
from qiskit.visualization import plot_histogram
import math

#definition of groovers function

def grover_search(target_states, iterations):
    # We assume that all target states have the same length
    n = len(target_states[0])

    qc = QuantumCircuit(n, n)

    # Initialization of the superposition equilibrium state
    qc.h(range(n))

    # Implementation of Grover's algorithm
    for _ in range(iterations):
        # Oracle
        qc.barrier()
        for target_state in target_states:
            for i in range(n):
                if target_state[i] == 0:
                    qc.x(i)
            qc.h(n-1)
            qc.mct(list(range(n - 1)), n - 1)  # This is a controlled-Z gate for multiple controls
            qc.h(n-1)
            for i in range(n):
                if target_state[i] == 0:
                    qc.x(i)
        qc.barrier()

        # Diffuser
        qc.h(range(n))
        qc.x(range(n))
        qc.h(n-1)
        qc.mct(list(range(n - 1)), n - 1)
        qc.h(n-1)
        qc.x(range(n))
        qc.h(range(n))
        qc.barrier()

    # Measuring results
    qc.measure(range(n), range(n))

    return qc

#defining targets


summed_results = {}
def multi_target_grover(targets):

    target_states = targets
    n = len(targets[0])
    num_of_goals = len(targets)
    searched_space = 2**n
    iterations = int((math.pi/4)*math.sqrt(searched_space/num_of_goals))
    #iterations = 2 * n + 1
    print("iterations")
    print(iterations)
    #summed result dictionary
    for i in range(searched_space):
        binary = format(i, '0{}b'.format(n))
        summed_results[binary] = 0

    # Calling groover search for every target and summing the results
    grover_circuit = grover_search(target_states[::-1], iterations)
    #print(grover_circuit.draw())

    # Simulation of quantum circuit
    simulator = Aer.get_backend('qasm_simulator')
    job = execute(grover_circuit, simulator, shots=1024)
    result = job.result()
    counts = result.get_counts(grover_circuit)

    for key in summed_results:
        if key in counts.keys():
            summed_results[key] += counts[key]

    #plotting the results
    print(summed_results)
    plot_histogram(summed_results)
    plt.show()
