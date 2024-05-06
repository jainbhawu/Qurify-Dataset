from qiskit import QuantumCircuit, Aer, transpile, assemble
import numpy as np

def qft_dagger(circ, n):
    for qubit in range(n//2):
        circ.swap(qubit, n-qubit-1)
    for j in range(n):
        for m in range(j):
            circ.cp(-np.pi/float(2**(j-m)), m, j)  # Use cp instead of cu1
        circ.h(j)
n = 3
qc = QuantumCircuit(n)

qc.h(range(n))
qft_dagger(qc, n)
qc.measure_all()

simulator = Aer.get_backend('qasm_simulator')
tqc = transpile(qc, simulator)
qobj = assemble(tqc)
result = simulator.run(qobj).result()
print(result.get_counts())
