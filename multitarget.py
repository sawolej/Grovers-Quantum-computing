from qiskit import QuantumCircuit, Aer, execute
import matplotlib.pyplot as plt
from qiskit.visualization import plot_histogram
import math
import numpy as np

#definition of groovers function

def grover_search(target_states, iterations):

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
            qc.h(n - 1)
            if n > 2:
                qc.mct(list(range(n - 1)), n - 1)  # Multi-controlled Toffoli for 3+ qubits
            else:
                qc.cx(0, 1)  # CNOT for 2 qubits
            qc.h(n - 1)

            for i in range(n):
                if target_state[i] == 0:
                    qc.x(i)
            qc.barrier()
        qc.barrier()

        # Diffuser
        qc.h(range(n))
        qc.x(range(n))
        qc.h(n - 1)
        if n > 2:
            qc.mct(list(range(n - 1)), n - 1)  # Multi-controlled Toffoli for 3+ qubits
        else:
            qc.cx(0, 1)  # CNOT for 2 qubits
        qc.h(n - 1)
        qc.x(range(n))
        qc.h(range(n))
        qc.barrier()

    # Measuring results
    qc.measure(range(n), range(n))

    return qc



def multi_target_grover(targets):

    summed_results = {}
    percentage_results = {}

    target_states = targets
    n = len(targets[0])
    num_of_goals = len(targets)
    searched_space = 2**n
    print("(math.pi/4)*math.sqrt(searched_space/num_of_goals)")
    print((math.pi/4)*math.sqrt(searched_space/num_of_goals))
    iterations = int(((math.pi/4)*math.sqrt(searched_space/num_of_goals)))#round((math.pi/4)*math.sqrt(searched_space/num_of_goals))#iterations = 2 * n + 1
    print("iterations")
    print(iterations)
    if(iterations<1):
        iterations=1
    #summed result dictionary
    for i in range(searched_space):
        binary = format(i, '0{}b'.format(n))
        summed_results[binary] = 0
        percentage_results[binary] = 0.0

    # Calling groover search for every target and summing the results
    grover_circuit = grover_search(target_states[::-1], iterations)
    print(grover_circuit.draw(fold=-1))


    # Simulation of quantum circuit
    simulator = Aer.get_backend('qasm_simulator')
    shots = 1024
    job = execute(grover_circuit, simulator, shots=shots)
    result = job.result()
    counts = result.get_counts(grover_circuit)

    counter = 0
    for key in summed_results:
        if key in counts.keys():
            summed_results[key] += counts[key]
            percentage_results[key] += counts[key]*100.0 / shots * 1.0
            counter += percentage_results[key]

    #plotting the results
    print(percentage_results)

    keys = percentage_results.keys()
    values = percentage_results.values()

    # Konwersja wartości na tablicę numpy
    values = np.array(list(values))

    plt.bar(keys, values)
    plt.xlabel('Targets')
    plt.ylabel('Probability')
    plt.title("Grover's search")
    plt.show()
