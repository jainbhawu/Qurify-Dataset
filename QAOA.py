
from qiskit import QuantumCircuit, QuantumRegister, Aer

reg = QuantumRegister(3, name='reg')
qc = QuantumCircuit(reg)
qc.x(reg[0])
for i in range(0, 2):
    qc.x(reg[i])
qc.x(reg[1])
qc.x(reg[0])
qc.x(reg[2])
qc.y(reg[1])

backend = Aer.get_backend('qasm_simulator')
qc = transpile(qc, backend, initial_layout=[3, 4, 2])
job = backend.run(qc)
qc2matrix(qc, output_file_path='example-matrix.csv')