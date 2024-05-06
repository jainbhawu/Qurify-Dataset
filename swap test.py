from qiskit import QuantumRegister, ClassicalRegister
from qiskit import QuantumCircuit, execute,IBMQ
from qiskit.tools.monitor import job_monitor

backend = Aer.get_backend('qasm_simulator')
  
q = QuantumRegister(3,'q')
c = ClassicalRegister(1,'c')

circuit = QuantumCircuit(q,c)

circuit.h(q[0]) 
circuit.x(q[1]) 
circuit.cswap(q[0],q[1],q[2]) 
circuit.h(q[0])
circuit.measure(q[0],c[0])

print(circuit)

nShots = 8192
job = execute(circuit, backend, shots=nShots)

job_monitor(job)

counts = job.result().get_counts()

if '1' in counts:
    b = counts['1']
else:
    b = 0
    
s = 1-(2/nShots)*(b)

print("Squared Inner Product:",str(s))
print("Counts: ",counts)
