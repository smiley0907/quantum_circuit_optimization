# Cell 6: Display Baseline and Optimized Circuits

n = 4

baseline = create_baseline_circuit(n)
optimized = optimize_circuit(baseline)

print("BASELINE CIRCUIT")
print(baseline)

print("\nBASELINE GATE COUNT:")
print(get_gate_count(baseline))

print("\nOPTIMIZED CIRCUIT")
print(optimized)

print("\nOPTIMIZED GATE COUNT:")
print(get_gate_count(optimized))
