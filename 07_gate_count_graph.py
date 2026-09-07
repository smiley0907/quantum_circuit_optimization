# Cell 7: Plot Baseline versus Optimized Gate Count

plt.figure(figsize=(8, 5))

plt.plot(
    results_df["Qubits"],
    results_df["Baseline Gate Count"],
    marker="o",
    label="Baseline Gate Count"
)

plt.plot(
    results_df["Qubits"],
    results_df["Optimized Gate Count"],
    marker="o",
    label="Optimized Gate Count"
)

plt.xlabel("Number of Qubits")
plt.ylabel("Gate Count")
plt.title("Baseline versus Optimized Gate Count")
plt.xticks(qubit_sizes)
plt.grid(True)
plt.legend()

plt.show()
