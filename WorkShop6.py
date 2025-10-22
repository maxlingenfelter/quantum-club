import qiskit
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt

print(f"Qiskit version: {qiskit.__version__}")

# Create the Bell state circuit
qcBell = QuantumCircuit(2)
qcBell.h(0)
qcBell.h(1)
qcBell.cx(0, 1)
qcBell.h(0)


# Get the statevector
sv = Statevector(qcBell)

# Print the numerical statevector to the console
print("Statevector:")
print(sv)

# --- Visualization ---

# Figure 1: The quantum circuit
fig1 = qcBell.draw("mpl")

# Figure 2: The statevector 'city' plot
# plt.figure(2)
sv.draw(output="city", figsize=(6, 4), title="Statevector City Plot")


# Show both figures
plt.show()
