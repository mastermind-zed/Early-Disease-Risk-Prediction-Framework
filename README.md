# Early Disease Risk Prediction Framework

A Machine Learning framework for identifying early risk of **Diabetes Mellitus** using clinical symptoms and laboratory indicators.

## 🚀 Overview
This project develops and evaluates four machine learning models to predict diabetes risk with high accuracy. It focuses on the importance of "Signal-over-Noise" by utilizing clinical features like HbA1c, FPG, and specific symptoms (Polyuria, Polydipsia).

### Key Results
| Model | Accuracy | F1-Score | AUC-ROC |
| :--- | :--- | :--- | :--- |
| **Random Forest** | **99.8%** | **99.8%** | **1.000** |
| **SVM** | **99.8%** | **99.8%** | **0.999** |
| Logistic Regression | 99.1% | 99.3% | 0.994 |
| Decision Tree | 98.6% | 99.0% | 0.980 |

---

## 📁 Repository Structure
```text
├── data/               # Clinical dataset (CSV)
├── models/             # Trained model binaries (.pkl)
├── scripts/            # Python scripts for EDA, training, and reporting
├── results/
│   ├── plots/          # Visualizations (ROC curves, heatmaps)
│   └── metrics/        # CSV and TXT summary of performance
├── reports/            # Final .docx project report
└── archive/            # Raw extraction and original data files
```

---

## 🛠️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/Early-Disease-Risk-Prediction.git
   cd Early-Disease-Risk-Prediction
   ```

2. **Install dependencies:**
   ```bash
   pip install pandas numpy scikit-learn matplotlib seaborn joblib python-docx
   ```

3. **Run the pipeline:**
   - Exploratory Data Analysis: `python scripts/run_eda.py`
   - Model Training: `python scripts/train_models.py`
   - Generate Report: `python scripts/generate_report.py`

---

## 📊 Methodology
The framework follows a five-step process:
1. **Data Preprocessing**: Handling missing values and feature standardization.
2. **EDA**: Correlation analysis and distribution checks.
3. **Model Selection**: Comparative analysis of LR, RF, DT, and SVM.
4. **Evaluation**: Metrics based on a 70/15/15 train-val-test split.
5. **Insights**: Discussion on data quality vs. volume in medical predictions.

## 🔄 Extending to Other Diseases
This framework is designed to be **disease-agnostic**. To predict a different disease (e.g., Heart Disease, Kidney Disease):
1.  **Prepare Data**: Ensure you have a `.csv` file with a binary `Outcome` column (0 or 1).
2.  **Add to Data Folder**: Place the new file in `data/`.
3.  **Update Script**: On line 105 of `scripts/train_models.py`, change the filepath to your new dataset.
4.  **Run Pipeline**: Execute the script to automatically generate new models, ROC curves, and performance metrics for the target disease.

## 📄 License
TBD - Check with project owner.

---
**Developed for Master's Dissertation Research.**
