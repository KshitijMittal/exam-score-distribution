import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# generate random scores
np.random.seed(42)
scores = np.random.normal(70, 15, 50)

# keep scores between 0 and 100
for i in range(len(scores)):
    if scores[i] < 0:
        scores[i] = 0
    if scores[i] > 100:
        scores[i] = 100

# round to integers
scores = np.round(scores).astype(int)

# convert to python list for clean printing
scores_list = [int(s) for s in scores]

print("Student Scores:")
print(scores_list)
print()

# calculate mean
total = 0
for score in scores:
    total = total + score
mean = total / len(scores)
print(f"Mean: {mean:.2f}")

# calculate median
scores_sorted = sorted(scores)
n = len(scores_sorted)
if n % 2 == 0:
    median = (scores_sorted[n // 2 - 1] + scores_sorted[n // 2]) / 2
else:
    median = scores_sorted[n // 2]
print(f"Median: {median:.2f}")

# calculate mode (most common score)
score_count = {}
for score in scores:
    if score in score_count:
        score_count[score] += 1
    else:
        score_count[score] = 1

mode = None
max_count = 0
for score, count in score_count.items():
    if count > max_count:
        max_count = count
        mode = score
print(f"Mode: {mode}")
print()

# determine exam difficulty
if mean < 50:
    print("Conclusion: The exam was too hard.")
elif mean > 85:
    print("Conclusion: The exam was too easy.")
else:
    print("Conclusion: The exam was balanced.")
print()

# create plot
plots_dir = Path("plots")
plots_dir.mkdir(exist_ok=True)

plt.figure(figsize=(8, 6))
plt.hist(scores, bins=10, edgecolor="black", color="skyblue")

plt.axvline(mean, color="red", linestyle="--", linewidth=2, label=f"Mean: {mean:.2f}")
plt.axvline(median, color="green", linestyle="--", linewidth=2, label=f"Median: {median:.2f}")

plt.xlabel("Score", fontsize=11, fontweight="bold")
plt.ylabel("Number of Students", fontsize=11, fontweight="bold")
plt.title("Score Distribution", fontsize=13, fontweight="bold")
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(plots_dir / "score_distribution.png", bbox_inches="tight", dpi=300)
print(f"Saved plot to: plots/score_distribution.png")
plt.close()

print("Done!")
