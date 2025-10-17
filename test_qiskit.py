# %pip install qiskit
# %pip install matplotlib
# %pip install qiskit[visualization]

import qiskit
from qiskit_aer import AerSimulator
from qiskit import version
from qiskit import QuantumCircuit
from qiskit.providers.basic_provider import BasicSimulator
from qiskit.visualization import visualize_transition, plot_histogram
from qiskit.quantum_info import Statevector
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------------------------------
# This script demonstrates the creation, visualization, and
# simulation of a simple quantum circuit using Qiskit.
#
# Steps:
#   1. Print Qiskit version.
#   2. Build a 2-qubit Bell state circuit.
#   3. Draw the circuit.
#   4. Simulate the circuit and print measurement results.
# -----------------------------------------------------------

# 1. Print Qiskit version for reproducibility and debugging.
print(f"Qiskit version: {qiskit.__version__}")

# 2. Create a simple quantum circuit with 1 qubit.
qc = QuantumCircuit(1)
qc.h(0)

# Draw the circuit and display it.
fig = qc.draw("mpl")
plt.show()

# Optionally save the circuit image; uncomment if desired.
# fig.savefig("circuit.png", dpi=200, bbox_inches="tight")

# Note: visualize_transition works best in Jupyter. To save an animation from a script,
# you can pass a filename argument if supported by your Qiskit version, e.g.:
# visualize_transition(qc, trace=True, filename="transition.gif")
