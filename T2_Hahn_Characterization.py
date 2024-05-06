import qiskit
from qiskit_experiments.library.characterization.t2hahn import T2Hahn
qubit = 0
conversion_factor = 1e-6 # our delay will be in micro-sec
delays = list(range(0, 50, 1) )
delays = [float(_) * conversion_factor for _ in delays]
number_of_echoes = 1

# Create a T2Hahn experiment. Print the first circuit as an example
exp1 = T2Hahn(physical_qubits=(qubit,), delays=delays, num_echoes=number_of_echoes)
qc=exp1.circuits()[0]
print(qc)
