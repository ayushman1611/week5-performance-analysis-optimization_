import pandas as pd

baseline = pd.read_csv("data/baseline_performance.csv")
target = pd.read_csv("data/simulated_optimization_target.csv")

print("BASELINE")
print(baseline.to_string(index=False))

print("\nOPTIMIZATION TARGET")
print(target.to_string(index=False))

peak = baseline.iloc[-1]
opt = target.iloc[-1]

print("\n800-user comparison")
print("Throughput improvement: {:.1f}%".format(
    (opt["Throughput (req/s)"] / peak["Throughput (req/s)"] - 1) * 100
))
print("P95 reduction: {:.1f}%".format(
    (1 - opt["P95 Response Time (s)"] / peak["P95 Response Time (s)"]) * 100
))
print("Database latency reduction: {:.1f}%".format(
    (1 - opt["Database Latency (ms)"] / peak["Database Latency (ms)"]) * 100
))
print("Error-rate reduction: {:.1f}%".format(
    (1 - opt["Error Rate (%)"] / peak["Error Rate (%)"]) * 100
))
