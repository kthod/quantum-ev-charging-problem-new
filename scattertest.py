from qiskit import Aer

backend = Aer.get_backend('ibmq_qasm_simulator')
print(backend.configuration().to_dict())