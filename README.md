# CMT307 Applied Machine Learning — ASHRAE Great Energy Predictor III
Cardiff University | Spring 2025/26 | Task 9: Energy Usage Prediction

---

## Team

| Name | Notebook | Focus |
|------|----------|-------|
| Shriya | `Shriya_Train_Core_Audit.ipynb` | `train.csv` audit & time features |
| Wahid | `Wahid_Building_Metadata_Audit.ipynb` | `building_metadata.csv` audit |
| Tanisha | `Tanisha_Weather_Audit.ipynb` | Weather data audit |
| Zahra | `Zahra_Data_Merging.ipynb` | Data merging — team lead |
| Shivalika | `Shivalika_Time_Series_Patterns.ipynb` | Time series + LightGBM |
| Ayan | `Ayan_Anomaly_Investigation.ipynb` | Anomaly detection + Random Forest |

> Shivalika and Ayan start from Sprint 2 — they depend on Zahra's merged output.

---

## How to Work

1. Open **Google Colab Enterprise** — Cardiff project: `cu-student-comsc-colab-cmt307`
2. Upload your notebook from the `notebooks/` folder (File → Upload notebook)
3. Run the setup cell at the top to download your data files
4. Do your work under the correct sprint section
5. At the end: **File → Download → Download .ipynb**
6. On your computer: move the file to `notebooks/`, then push to GitHub (see below)

---

## Pushing to GitHub

```bash
git add notebooks/YourName_Notebook.ipynb
git commit -m "sprint 1: brief description of what you did"
git push
```

You need to have cloned the repo and set up git on your machine once. Ask Zahra for the repo link.

---

## Data Files

All six files are on OneDrive. Your notebook's setup cell already has the links — just run it.

| File | Rows | Description |
|------|------|-------------|
| `train.csv` | 20.2M | Hourly meter readings 2016 |
| `test.csv` | 41.7M | Meter readings 2017–2018 (predict these) |
| `building_metadata.csv` | 1,449 | Building type, size, site |
| `weather_train.csv` | 139K | Hourly weather at 16 sites, 2016 |
| `weather_test.csv` | 277K | Hourly weather at 16 sites, 2017–2018 |
| `sample_submission.csv` | — | Submission format |

Meter types: `0` Electricity · `1` Chilled Water · `2` Steam · `3` Hot Water

---

## Evaluation Metric

**RMSLE** — Root Mean Squared Log Error. Use `np.log1p(meter_reading)` throughout.

---

## Report Tasks

| Task | Description | Weight |
|------|-------------|--------|
| T1-1 | Descriptive analysis | 10% |
| T1-2 | Results analysis and discussion | 10% |
| T2-1 | Preprocessing — missing values, outliers, features | 10% |
| T2-2 | Literature review | 10% |
| T3-1 | Model implementation and tuning | 15% |
| T3-2 | Model evaluation | 5% |
| T4 | Report structure and clarity | 20% |
| Part 2 | Peer assessment and self-reflection | 20% |

Max 4500 words · 10 pages · 10pt font · 20mm margins
