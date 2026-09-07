# Cell 3: Calculate Baseline Gate Count

def get_gate_count(qc):
    return sum(qc.count_ops().values())


# Test the baseline circuit with 4 qubits
baseline_4 = create_baseline_circuit(4)

print("Baseline Circuit:")
print(baseline_4)

print("\nBaseline Gate Count:", get_gate_count(baseline_4))
