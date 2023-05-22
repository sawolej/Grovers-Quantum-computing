#initialization
import matplotlib.pyplot as plt
import numpy as np
import math

# importing Qiskit
from qiskit import IBMQ, Aer, transpile, execute
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.providers.ibmq import least_busy

# import basic plot tools
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Load IBM Q account and get the least busy backend device
provider = IBMQ.load_account()
# for device
# provider = IBMQ.get_provider("ibm-q")
# device = least_busy(provider.backends(filters=lambda x: x.configuration().n_qubits >= 3 and
#                                    not x.configuration().simulator and x.status().operational==True))
# print("Running on current least busy device: ", device)

n = 3
grover_circuit = QuantumCircuit(n)

def initialize_s(qc, qubits):
    """Apply a H-gate to 'qubits' in qc"""
    for q in qubits:
        qc.h(q)
    return qc

oracle = QuantumCircuit(n)
oracle.h(2)
oracle.mct(list(range(n - 1)), n - 1)
oracle.h(2)
oracle.to_gate()
oracle.name = "U$_w$"

def diffuser(n):
    diffuser = QuantumCircuit(n)
    for qubit in range(n):
        diffuser.h(qubit)
    for qubit in range(n):
        diffuser.x(qubit)
    diffuser.h(n-1)
    diffuser.mct(list(range(n-1)), n-1)  # multi-controlled-toffoli
    diffuser.h(n-1)
    for qubit in range(n):
        diffuser.x(qubit)
    for qubit in range(n):
        diffuser.h(qubit)
    diffuser.to_gate()
    diffuser.name = "U$_s$"
    return diffuser


backend = Aer.get_backend('qasm_simulator')
grover_circuit = QuantumCircuit(n)
grover_circuit = initialize_s(grover_circuit, [0,1,2]) # step 1
grover_circuit.barrier()
grover_circuit.append(oracle, [0,1,2]) # step 2
grover_circuit.append(diffuser(n), [0,1,2]) # step 3
grover_circuit.measure_all()
print(grover_circuit.draw())

result = execute(grover_circuit, backend).result()
counts = result.get_counts()

# grover_circuit = initialize_s(grover_circuit, (list(range(n - 1))))
# print(grover_circuit.draw())
# oracle(grover_circuit)
# diffuser(grover_circuit)
#
# # Run circuit ont he simulator
# sv_sim = Aer.get_backend('statevector_simulator')
# result = sv_sim.run(grover_circuit).result()
# statevec = result.get_statevector()
# from qiskit.visualization import array_to_latex
# array_to_latex(statevec, prefix="|\\psi\\rangle =")
#
# grover_circuit.measure_all()
#
# qasm_sim = Aer.get_backend('qasm_simulator')
# result = qasm_sim.run(grover_circuit).result()
# counts = result.get_counts()


# Run circuit on the least busy backend. Monitor the execution of the job in the queue
# from qiskit.tools.monitor import job_monitor
# transpiled_grover_circuit = transpile(grover_circuit, device, optimization_level=3)
# job = device.run(transpiled_grover_circuit)
# job_monitor(job, interval=2)
#
# # Get the results from the computation
# results = job.result()
# counts = results.get_counts(grover_circuit)

plot_histogram(counts)
plt.show()




