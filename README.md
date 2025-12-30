# Student Score Distribution Analyzer ✅

This project generates synthetic exam scores for 50 students, computes basic
statistics (Mean, Median, Mode), and visualizes the score spread with a
histogram saved to `plots/score_distribution.png`.

---

## 💡 Key Concepts

- **Average (Mean)** summarizes the central tendency but can be affected by
  outliers.
- **Spread (Histogram)** shows how scores are distributed across ranges and
  reveals skewness, clusters, and multiple modes that a single average may
  hide.

---

## 🔧 Setup & Run

1. Create a virtual environment (recommended):

   ```bash
   python -m venv .venv
   .venv\Scripts\activate   # Windows
   source .venv/bin/activate  # macOS / Linux
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the analyzer:

   ```bash
   python distribution_analysis.py
   ```

---

## 📈 Output

- A histogram is saved to `plots/score_distribution.png` that shows the
  frequency of scores with vertical dashed lines marking the **Mean** and
  **Median**.

---

## 📝 Notes

- The script uses a clipped normal distribution to create realistic scores
  while guaranteeing values remain in the [0, 100] range.
- The script is well-commented and creates the `plots/` directory if it does
  not exist.
