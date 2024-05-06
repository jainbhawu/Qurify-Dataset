import numpy as np

qubit2 = 0
conversion_factor = 1e-6
delays2 = np.append(
                    (np.linspace(0.0, 51.0, num=26)).astype(float),
                    (np.linspace(53, 100.0, num=25)).astype(float),
                )

delays2 = [float(_) * conversion_factor for _ in delays2]
delays3 = np.append(
                    (np.linspace(0.0, 25.5, num=26)).astype(float),
                    (np.linspace(26.5, 50, num=25)).astype(float),
                )
delays3 = [float(_) * conversion_factor for _ in delays3]

num_echoes = 1
estimated_t2hahn2 = 30 * conversion_factor
exp2_0echoes = T2Hahn([qubit2], delays2, num_echoes=0)
exp2_0echoes.analysis.set_options(p0={"amp": 0.5, "tau": estimated_t2hahn2, "base": 0.5})
print("The first circuit of hahn echo experiment with 0 echoes:")
qc=exp2_0echoes.circuits()[0]
print(qc)
