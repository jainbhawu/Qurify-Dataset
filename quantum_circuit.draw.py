from qiskit import QuantumCircuit, Aer, transpile, assemble

n = 3
qc = QuantumCircuit(n+1, n)
qc.h(range(n+1))
qc.barrier()
qc.x(n)
qc.barrier()
qc.h(range(n))
qc.barrier()
qc.measure(range(n), range(n))
simulator = Aer.get_backend('qasm_simulator')
tqc = transpile(qc, simulator)
qobj = assemble(tqc)
result = simulator.run(qobj).result()
print(result.get_counts())
