# GHZ Circuit
nq = 4
qc = QuantumCircuit(nq)
qc.h(0)
for i in range(1, nq):
    qc.cx(i-1, i)

qc.draw("mpl")
