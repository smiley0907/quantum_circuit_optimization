# Cell 5: Evaluate Baseline and Optimized Circuits

qubit_sizes = [4, 8, 12, 16]

results = []

for n in qubit_sizes:

    # Create baseline circuit
    baseline = create_baseline_circuit(n)

    # Optimize circuit
    optimized = optimize_circuit(baseline)

    # Calculate gate counts
    baseline_count = get_gate_count(baseline)
    optimized_count = get_gate_count(optimized)

    # Calculate reduction
    absolute_reduction = baseline_count - optimized_count
    percentage_reduction = (
        absolute_reduction / baseline_count
    ) * 100

    results.append([
        n,
        baseline_count,
        optimized_count,
        absolute_reduction,
        percentage_reduction
    ])


results_df = pd.DataFrame(
    results,
    columns=[
        "Qubits",
        "Baseline Gate Count",
        "Optimized Gate Count",
        "Absolute Gate Count Reduction",
        "Gate Count Reduction (%)"
    ]
)

results_df
