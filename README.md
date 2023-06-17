# Grovers-Quantum-computing

Implementation of Adapted Grover's Algorithm for Multitarget Unordered Database Searching - Team Project for uni class. 


## Description

This project involves the implementation and investigation of Grover's algorithm in a multi-target quantum search context. The algorithm was implemented using Qiskit, a popular framework for quantum computing, which allows us to define, manipulate, and simulate quantum circuits.

More analysis coming.

## Requirements

This project is implemented in Python 3 using the Qiskit package for quantum computing simulations. The other dependencies are matplotlib for visualization, numpy for mathematical operations and the standard math module.

Here's a list of the dependencies:

* qiskit
* matplotlib
* numpy
* math

## Installation & Setup

To setup the environment for the project, follow these steps:

1. Clone the repository to your local environment. You can do this by running the following command in your terminal:

```
git clone https://github.com/sawolej/Grovers-Quantum-computing.git
```
  
2. Navigate to the cloned repository by using:

```
cd <cloned-repo-directory>
```

3. We recommend creating a virtual environment to isolate the project dependencies. You can create it by using:

```
python3 -m venv env
```

4. Activate the virtual environment:

    - On macOS and Linux:
    ```
    source env/bin/activate
    ```

    - On Windows:
    ```
    .\env\Scripts\activate
    ```

5. Install the required dependencies:

```
pip install qiskit matplotlib numpy

```

## Running the Simulator

After completing the setup, you can run the Grover's Algorithm simulator by executing the `main.py` script:

```
python main.py
```

Initially this script will execute the Multi-Target Grover's Algorithm with a 4-qubit system and two targets. The targets are randomly generated. Results will be displayed in the console, including the quantum circuit diagram and a histogram of the simulation results.

## Customizing the Simulator

You can modify the number of qubits and targets by changing the `qubits` and `num_targets` variables in the `main()` function within the `main.py` script.


## Understanding the Results

The simulator uses the Qiskit library's qasm_simulator to simulate the quantum circuits. The output histogram visualizes the probabilities of each state after running the Grover's algorithm. Ideally, the target states should have significantly higher probabilities.

Please note that this simulator uses a basic implementation of Milti-Target Grover's Algorithm and does not cater to potential physical real-world restrictions or errors in a practical quantum computer.

## Troubleshooting

If you encounter any issues, please check that you have the correct versions of Python and all required packages installed. Also, make sure you've followed the installation and setup instructions correctly. If the problem persists, feel free to raise an issue on the GitHub repository.

## References

The simulator uses the [Qiskit library](https://qiskit.org/) to build and simulate quantum circuits. Refer to the Qiskit documentation for detailed information about the quantum operations and methods used in this project.




