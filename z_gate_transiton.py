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
qc2 = QuantumCircuit(1)
qc2.h(0)
qc2.z(0)
qc2.x(0)
fig = qc2.draw("mpl")
plt.show()
# Optionally save the circuit image; uncomment if desired.
# fig.savefig("z_gate_circuit.png", dpi=200, bbox_inches="tight")
visualize_transition(qc2, trace=True)
