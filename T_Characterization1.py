import numpy as np
import qiskit
from qiskit_experiments.library.characterization import Tphi

# An Aer simulator
from qiskit.providers.fake_provider import FakePerth
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel

# Create a pure relaxation noise model for AerSimulator
noise_model = NoiseModel.from_backend(
    FakePerth(), thermal_relaxation=True, gate_error=False, readout_error=False
)

# Create a fake backend simulator
backend = AerSimulator.from_backend(FakePerth(), noise_model=noise_model)

# Time intervals to wait before measurement for t1 and t2
delays_t1 = np.arange(1e-6, 300e-6, 10e-6)
delays_t2 = np.arange(1e-6, 50e-6, 2e-6)
exp = Tphi(physical_qubits=(0,), delays_t1=delays_t1, delays_t2=delays_t2, num_echoes=1)
qc=exp.component_experiment(1).circuits()[-1]
qc.draw("mpl")
