import math
from qiskit import QuantumCircuit, execute, BasicAer




###############################################################
# Make a quantum circuit for state initialization.
###############################################################
circuit = QuantumCircuit(4, 4, name="initializer_circ")


desired_vector = [
    1 / math.sqrt(4) * complex(0, 1),
    1 / math.sqrt(8) * complex(1, 0),
    0,
    0,
    0,
    0,
    0,
    0,
    1 / math.sqrt(8) * complex(1, 0),
    1 / math.sqrt(8) * complex(0, 1),
    0,
    0,
    0,
    0,
    1 / math.sqrt(4) * complex(1, 0),
    1 / math.sqrt(8) * complex(1, 0),
]


circuit.initialize(desired_vector, [0, 1, 2, 3])


circuit.measure([0, 1, 2, 3], [0, 1, 2, 3])


print(circuit)


###############################################################
# Execute on a simulator backend.
###############################################################
shots = 10000


# Desired vector
print("Desired probabilities: ")
print([format(abs(x * x), ".3f") for x in desired_vector])


# Initialize on local simulator
sim_backend = BasicAer.get_backend("qasm_simulator")
job = execute(circuit, sim_backend, shots=shots)
result = job.result()


counts = result.get_counts(circuit)


qubit_strings = [format(i, "04b") for i in range(2**4)]
print("Probabilities from simulator: ")
print([format(counts.get(s, 0) / shots, ".3f") for s in qubit_strings])
