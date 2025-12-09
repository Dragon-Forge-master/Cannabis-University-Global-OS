# Cannabis University Global: The Open Standard Project

**Copyright © 2025 Dragon's Forge AI**

### 🔬 Science over Marketing. Data over Hype.

**Cannabis University Global (CUG)** is an open-source initiative dedicated to standardizing cannabis data. We are moving the industry away from arbitrary names ("Indica/Sativa") and towards a standardized, biochemical data model based on the Entourage Effect.

This repository provides the **foundational algorithms, schemas, and visualization tools** needed to build the next generation of safe, reliable cannabis technology.

---

## 📂 Repository Contents

We have seeded this repository with 6 core assets to get the community started:

### 1. The Logic: `recommender_core.py` (Python)
* **What it is:** A vector-matching algorithm that scores strains based on chemical synergy rather than strain names.
* **Key Feature:** Implements "Terpene Weighting" to calculate match scores for specific goals (e.g., Sleep, Focus, Pain).

### 2. The Standard: `strain_schema.json` (JSON)
* **What it is:** The proposed industry standard for storing cannabis data.
* **Key Feature:** Includes fields for Type I-IV classification and detailed lab results, replacing the outdated "Stoner Logic" data models.

### 3. The Safety: `safe_dose_calc.js` (JavaScript)
* **What it is:** A harm-reduction algorithm for edible dosing.
* **Key Feature:** Accounts for metabolic weight and liver conversion rates (11-Hydroxy-THC) to prevent over-consumption.

### 4. The Visuals: `terpene_visualizer.html` (HTML/Canvas)
* **What it is:** A standalone radar chart generator.
* **Key Feature:** Visualizes the "shape" of a high by plotting the top 5 terpenes dynamically.

### 5. The Law: `compliance_rules.json` (JSON)
* **What it is:** A configuration file for global legal limits.
* **Key Feature:** Currently supports CA, UK, and Canada. Designed to be easily expanded by international contributors.

### 6. The Data: `strains_seed_data.csv` (CSV)
* **What it is:** A starter dataset of 10 scientifically verified chemovars.
* **Key Feature:** Properly formatted data ready for import into the Recommender Engine.

---

## 🚀 How to Use

### Prerequisites
* Python 3.8+
* A modern web browser (for the visualizer)

### Quick Start (Python Recommender)
```bash
# Run the Recommender logic
python recommender_core.py
