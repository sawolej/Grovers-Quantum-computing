# Grovers-Quantum-computing

Implementation of Adapted Grover's Algorithm for Multitarget Unordered Database Searching - Team Project for uni class. 

## Description

This project involves the implementation and investigation of Grover's algorithm in a multi-target quantum search context. The algorithm was implemented using Qiskit, a popular framework for quantum computing, which allows us to define, manipulate, and simulate quantum circuits.
More analysis coming

### Dependencies

This project is implemented in Python using the Qiskit package for quantum computing simulations. The other dependencies are matplotlib for visualization, numpy for mathematical operations and the standard math module.

Here's a list of the dependencies:

* qiskit
* matplotlib
* numpy
* math

### Installing

First, you need to have Python installed on your machine. You can download it from the official website: https://www.python.org/

Once Python is installed, you can install the required packages using pip. pip is a package manager for Python and should come with the Python installation.

To install the required packages, you can use the following command:
```
pip install qiskit matplotlib numpy

```


### Executing program

Once the dependencies are installed, you can run the program by executing the Python script. Navigate to the folder containing the script in your command line, and then execute the following command:
```
python main.py
```
Initially it will work for 4-Qubits system and 2 random target states, you can change that in the main function
## Help
For specific questions related to Qiskit, you can consult the Qiskit documentation at https://qiskit.org/documentation/.

It was observed that when the number of target states was exactly half of the search space, the algorithm behaved differently. In such cases, the success probability was essentially random, showing no clear peak.
When target states exceed half of the search space, efficiency undergoes a significant shift. In these cases, we found it more optimal to invert the problem and use Grover’s algorithm to search for the non-target states,


