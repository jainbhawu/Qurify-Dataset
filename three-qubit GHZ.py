from qiskit import QuantumCircuit
circ = QuantumCircuit(3)
circ.h(0)
circ.cx(0, 1)
circ.cx(0, 2)

circ.draw()