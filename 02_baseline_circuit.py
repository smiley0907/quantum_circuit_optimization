# Cell 2: Create Baseline Circuit

def create_baseline_circuit(n):
    qc = QuantumCircuit(n)

    # Core quantum circuit structure
    qc.h(0)

    for q in range(n - 1):
        qc.cx(q, q + 1)

    # Deliberately introduced redundant single-qubit gates
    for q in range(n):
        qc.h(q)
        qc.h(q)

        qc.x(q)
        qc.x(q)

    # Deliberately introduced redundant two-qubit gates
    for q in range(n - 1):
        qc.cx(q, q + 1)
        qc.cx(q, q + 1)

    return qc
