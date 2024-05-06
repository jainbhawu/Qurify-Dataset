from qiskit import QuantumRegister, QuantumCircuit
from numpy import pi

qreg_q = QuantumRegister(2, 'q')
qc = QuantumCircuit(qreg_q)

qc.h(qreg_q)

qc.p(pi / 2, qreg_q[0])
qc.barrier()

qc.p(pi / 4, qreg_q[1])
