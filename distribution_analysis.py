"""Student Score Distribution Analyzer"""

import os
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def generate_scores(n_students: int = 50, seed: int = 42) -> np.ndarray:
    """Generate `n_students` integer scores (0-100)."""
    rng = np.random.default_rng(seed)
    # Normal distribution centered at 70
    raw = rng.normal(loc=70, scale=15, size=n_students)
    clipped = np.clip(raw, 0, 100)
    return np.rint(clipped).astype(int)

def compute_statistics(scores: np.ndarray) -> dict:
    """Compute mean, median, and mode."""
    # Scipy handles mode perfectly fine on its own
    mode_res = stats.mode(scores, keepdims=True)
    mode_val = int(mode_res.mode[0])
    
    return {
        "mean": float(np.mean(scores)),
        "median": float(np.median(scores)),
        "mode": mode_val
    }

def plot_distribution(scores: np.ndarray, stats_dict: dict, out_path: str) -> None:
    """Create and save a histogram."""
    plt.figure(figsize=(8, 6))
    plt.hist(scores, bins=10, edgecolor="black")

    # Add vertical lines
    plt.axvline(stats_dict["mean"], color="red", linestyle="--", label=f"Mean: {stats_dict['mean']:.2f}")
    plt.axvline(stats_dict["median"], color="green", linestyle="--", label=f"Median: {stats_dict['median']:.2f}")

    plt.xlabel("Score")
    plt.ylabel("Number of Students")
    plt.title("Score Distribution")
    plt.legend()

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    plt.savefig(out_path, bbox_inches="tight")
    plt.close()

def difficulty_conclusion(mean_val: float) -> str:
    if mean_val < 50: return "Conclusion: The exam was too hard."
    if mean_val > 85: return "Conclusion: The exam was too easy."
    return "Conclusion: The exam was balanced."

def main():
    scores = generate_scores(50)
    stats_dict = compute_statistics(scores)
    
    print("Student Scores:", list(scores))
    print(f"Mean: {stats_dict['mean']:.2f}")
    print(f"Median: {stats_dict['median']:.2f}")
    print(f"Mode: {stats_dict['mode']}")
    print(difficulty_conclusion(stats_dict['mean']))

    out_path = os.path.join("plots", "score_distribution.png")
    plot_distribution(scores, stats_dict, out_path)
    print(f"Histogram saved to: {out_path}")

if __name__ == "__main__":
    main()