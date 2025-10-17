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

# 2. Create a 3-qubit quantum circuit
# Qubit 0: X gate
# Qubit 1: No gates (stays |0⟩)
# Qubit 2: H gate then Z gate
qc = QuantumCircuit(3)

# Apply gates
qc.x(0)      # X gate on qubit 0
# qubit 1 has no gates
qc.h(2)      # H gate on qubit 2
qc.z(2)      # Z gate on qubit 2

# Display the circuit
print("Quantum Circuit:")
print(qc.draw())
print("\n" + "="*60 + "\n")

# Show step-by-step evolution
print("Step-by-step State Evolution:")
print("-" * 60)

# Initial state |000⟩
initial_state = Statevector.from_label('000')
print(f"Initial state: |000⟩")
print(f"State vector: {initial_state.data}")
print()

# After X gate on qubit 0
qc_step1 = QuantumCircuit(3)
qc_step1.x(0)
state1 = initial_state.evolve(qc_step1)
print(f"After X on qubit 0: |100⟩")
print(f"State vector: {state1.data}")
print()

# After H gate on qubit 2
qc_step2 = QuantumCircuit(3)
qc_step2.x(0)
qc_step2.h(2)
state2 = initial_state.evolve(qc_step2)
print(f"After H on qubit 2: (|100⟩ + |101⟩)/√2")
print(f"State vector: {state2.data}")
print()

# Final state after Z gate on qubit 2
final_state = initial_state.evolve(qc)
print(f"After Z on qubit 2 (FINAL STATE): (|100⟩ - |101⟩)/√2")
print(f"State vector: {final_state.data}")
print()

print("="*60)
print("\nFinal State Vector (in computational basis |000⟩ to |111⟩):")
print("-" * 60)
for i, amp in enumerate(final_state.data):
    if abs(amp) > 1e-10:  # Only show non-zero amplitudes
        basis_state = format(i, '03b')
        probability = abs(amp)**2
        print(f"|{basis_state}⟩: {amp:.4f} (probability: {probability:.4f} = {probability*100:.1f}%)")

print("\n" + "="*60)
print("\nMeasurement Probabilities:")
print("-" * 60)
print(f"|100⟩: 50.0%")
print(f"|101⟩: 50.0%")

# Draw circuit diagram
fig = qc.draw("mpl")
plt.tight_layout()
plt.show()

# Visualize the transition
visualize_transition(qc, trace=True, saveas=None, fpg=20, spg=1)
