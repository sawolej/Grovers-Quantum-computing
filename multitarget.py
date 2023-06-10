from qiskit import QuantumCircuit, Aer, execute
import matplotlib.pyplot as plt
from qiskit.visualization import plot_histogram

#definition of groovers function

def grover_search(target_state):
    # Initialization of a quantum object with 4
    print("qubits")
    n = len(target_state)
    print(n)
    qc = QuantumCircuit(n, n)

    # Initialization of the superposition equilibrium state
    qc.h(range(n))

    # Number of iterations
    iterations = 2*n + 1 #9 #int((3.14/4) * (2 ** 0.5) * (2 ** (4/2)))
    #iterations = 9

    # Implementation of Groovers algorithm
    for _ in range(iterations):
        qc.barrier()
        for i in range(n):
            if target_state[i] == 0:
                qc.x(i)
        qc.h(n-1)
        qc.mct(list(range(n - 1)), n - 1)
        qc.h(n-1)
        for i in range(n):
            if target_state[i] == 0:
                qc.x(i)
        qc.barrier()

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
    #summed result dictionary
    for i in range(2**n):
        binary = format(i, '0{}b'.format(n))
        summed_results[binary] = 0

    # Calling groover search for every target and summing the results
    for target_state in target_states:
        grover_circuit = grover_search(target_state[::-1])
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
