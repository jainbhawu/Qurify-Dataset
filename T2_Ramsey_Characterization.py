import numpy as np
import qiskit
from qiskit_experiments.library import T2Ramsey
qubit = 0
# set the desired delays
delays = list(np.arange(1e-6, 50e-6, 2e-6))
# Create a T2Ramsey experiment. Print the first circuit as an example
exp1 = T2Ramsey((qubit,), delays, osc_freq=1e5)
qc=exp1.circuits()[0]
print(qc)
