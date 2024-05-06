from qiskit import QuantumCircuit, Aer, transpile, assemble

qc = QuantumCircuit(2)

qc.h(0)

qc.cx(0, 1)

message = '10'
if message == '00':
    pass
elif message == '01':
    qc.z(1)
elif message == '10':
    qc.x(1)
elif message == '11':
    qc.z(1)
    qc.x(1)

qc.cx(0, 1)

qc.h(0)

qc.measure_all()

simulator = Aer.get_backend('qasm_simulator')
tqc = transpile(qc, simulator)
qobj = assemble(tqc)
result = simulator.run(qobj).result()
print(result.get_counts())
