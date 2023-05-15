from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram

# Define the Oracle circuit
oracle = QuantumCircuit(2, name='oracle')
oracle.cz(0, 1)

# Define the Diffuser circuit
diffuser = QuantumCircuit(2, name='diffuser')
diffuser.h([0,1])
diffuser.z([0,1])
diffuser.cz(0,1)
diffuser.h([0,1])
diffuser.z([0,1])

# Combine the Oracle and Diffuser to get Grover's algorithm
grover_circuit = QuantumCircuit(2, 2)
grover_circuit.h([0,1])
grover_circuit.append(oracle, [0,1])
grover_circuit.append(diffuser, [0,1])
grover_circuit.measure([0,1], [0,1])

# Display the circuit
print(grover_circuit)

# Execute the circuit on a Qasm simulator
simulator = Aer.get_backend('qasm_simulator')
counts = execute(grover_circuit, backend=simulator, shots=1024).result().get_counts()

# Display the results
plot_histogram(counts)