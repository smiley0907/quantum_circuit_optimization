# Cell 4: Remove redundant self-inverse gate pairs

def optimize_circuit(qc):
    optimized = QuantumCircuit(qc.num_qubits)

    instructions = list(qc.data)

    i = 0

    while i < len(instructions):

        current = instructions[i]

        # Check whether a consecutive identical gate exists
        if i + 1 < len(instructions):

            next_instruction = instructions[i + 1]

            current_name = current.operation.name
            next_name = next_instruction.operation.name

            current_qubits = [q._index for q in current.qubits]
            next_qubits = [q._index for q in next_instruction.qubits]

            # H-H, X-X, and CX-CX are redundant pairs
            if (
                current_name == next_name
                and current_name in ["h", "x", "cx"]
                and current_qubits == next_qubits
            ):
                i += 2
                continue

        # Preserve non-redundant operations
        optimized.append(
            current.operation,
            current.qubits,
            current.clbits
        )

        i += 1

    return optimized
