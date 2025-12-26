# Student Performance Prediction (ML Semester Project)

A tabular regression project: predict a student's final performance from demographics and subject scores.

Goal: build a reproducible pipeline with preprocessing (numeric/categorical), baseline and improved models, compare metrics, and export artifacts (joblib/ONNX).

## Dataset
- File: `StudentsPerformance.csv` (repository root).
- Potential target columns: `G3`, `final_grade`, `exam_score`, `Score`, `math score`, `reading score`, `writing score`.
  If none is present, the notebook can create `final_grade` as the mean of three subject scores (if available).

## Project Structure
- `notebooks/student_performance.ipynb` — main notebook: EDA → preprocessing → baselines → improved models → explainability → export.
- `models/` — saved models (`*.joblib`), `metadata_*.json`, and ONNX exports (`*.onnx`).
- `reports/` — plots and reports generated from the notebook.
- `requirements.txt` — dependencies for the tabular ML stack.

## Setup & Run (local)
1) Create and activate a virtual environment (Python 3.11+/3.12).
2) Install dependencies: `pip install -r requirements.txt`.
3) Open `notebooks/student_performance.ipynb` and execute step by step.

Notes
- The notebook includes a version check cell and optional Colab setup for repairing NumPy/Pandas ABI issues.

## Export & Inference
- The best model is refit on train+val and saved under `models/*.joblib` with `metadata_*.json`.
- ONNX export (when supported) and runtime validation via onnxruntime.
- Inference helpers in the notebook: `predict_row(dict)` and `predict_df(pd.DataFrame)`.

## Metrics
- Primary metrics: RMSE, MAE, R². The notebook compares models, includes diagnostics (residuals, QQ‑plot), and explainability (permutation importance; SHAP if available).
