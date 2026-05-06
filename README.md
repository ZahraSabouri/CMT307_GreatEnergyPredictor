# CMT307 Applied Machine Learning: ASHRAE Energy Prediction

Cardiff University, CMT307 Applied Machine Learning, 2025/26  
Task: predict hourly building energy use using the ASHRAE Great Energy Predictor III dataset.

This README explains how to run the submitted code required by the assessment brief:

1. Code used to produce statistics and plots for the descriptive analysis.
2. Code used to preprocess the original data, train models, and evaluate them on a held-out test set.

The final report uses Root Mean Squared Logarithmic Error (RMSLE). All modelling notebooks train on `log1p(meter_reading)` and convert predictions back to the original scale before evaluation.

## Repository Contents

```text
.
|-- README.md
|-- requirements.txt
|-- notebooks/
|   |-- Shriya_Train_Audit_and_Verification.ipynb
|   |-- Tanisha_Weather_and_Literature_Review.ipynb
|   |-- Wahid_Building_Metadata_and_Models.ipynb
|   |-- Zahra_Integration_and_Ensemble.ipynb
|   |-- Shivalika_TimeSeries_and_LightGBM.ipynb
|   `-- Ayan_Anomalies_and_RandomForest.ipynb
`-- shared/
    |-- data_loader.py
    `-- metrics.py
```

Large data files, processed CSV files, saved model files, and generated outputs are not included in the code zip because they are reproducible and too large for submission.

Each notebook begins with a linked **Notebook Summary** for its own sections. The full project execution map is kept in this README so the global run order is documented once instead of repeated in every notebook.

## Data Setup

Download the ASHRAE Great Energy Predictor III files and place them here:

```text
data/ashrae-energy-prediction/
|-- train.csv
|-- test.csv
|-- building_metadata.csv
|-- weather_train.csv
|-- weather_test.csv
`-- sample_submission.csv
```

Important: the Kaggle `test.csv` file is unlabeled, so it was not used for the model evaluation reported in the project. All reported training/testing results use a chronological split of `train.csv`: January-October 2016 for training and November-December 2016 as the held-out test/validation period. The Kaggle `test.csv`, `weather_test.csv`, and `sample_submission.csv` are only needed if someone wants to generate optional Kaggle-style prediction files.

The notebooks expect this relative path when run from the `notebooks/` folder:

```text
../data/ashrae-energy-prediction/
```

The helper file `shared/data_loader.py` provides a central registry for all raw CSV files, processed CSV files, output CSVs, saved models, and generated figures used by the notebooks. In the submitted version, every value in the `LINKS` dictionary is intentionally an empty string. This avoids submitting private development links and leaves clear placeholders if direct-download links need to be added later.

The data loader checks for local files first, so no links are needed when the files already exist in the expected folders. If running in Google Colab or another environment where a file is missing, add a direct-download URL to the matching `LINKS` entry in `shared/data_loader.py`, then use the loader function or run the notebook cell again.

Useful examples:

```python
from shared.data_loader import list_files, load_train, load_final_train_with_features

print(list_files())          # registered raw, processed, output, and model files
train = load_train()         # loads data/ashrae-energy-prediction/train.csv
features = load_final_train_with_features()
```

## Environment Setup

Python 3.10 or newer is recommended.

Before running the notebooks, create the output folders if they do not already exist:

```bash
mkdir data_processed outputs
```

## Part 1: Descriptive Analysis Statistics

Run these notebooks to reproduce the statistics, checks, and plots used for the descriptive analysis in the report.

| Notebook | Main purpose | Main inputs | Main outputs |
|---|---|---|---|
| `Shriya_Train_Audit_and_Verification.ipynb` | Audits `train.csv` and `test.csv`, checks meter-reading patterns, validates merged train/test files. | Raw train/test data and merged files. | Dataset shape checks, meter summaries, time-feature checks. |
| `Tanisha_Weather_and_Literature_Review.ipynb` | Audits weather missingness and produces processed weather files. | `weather_train.csv`, `weather_test.csv`. | `data_processed/weather_train_processed.csv`, `data_processed/weather_test_processed.csv`. |
| `Wahid_Building_Metadata_and_Models.ipynb` | Audits building metadata, missing values, building categories, and feature transformations. | `building_metadata.csv`. | `data_processed/building_metadata_processed.csv`, metadata EDA tables/plots. |
| `Shivalika_TimeSeries_and_LightGBM.ipynb` | Produces time-series EDA: hourly, monthly, weekday/weekend, timeline, and heatmap patterns. | `data_processed/merged_train.csv`. | Time-series plots and lag/rolling feature checks. |
| `Ayan_Anomalies_and_RandomForest.ipynb` | Investigates zero streaks, Site 0 electricity calibration issue, extreme outliers, and sudden jumps. | `data_processed/merged_train.csv`. | Anomaly tables, including zero-streak building/meter pairs. |

For a full fresh run, create the merged training file first by running the initial merge cells of `Zahra_Integration_and_Ensemble.ipynb`. Those cells save:

```text
data_processed/merged_train.csv
```

Then run the descriptive notebooks above.

## Part 2: Preprocessing, Model Training, and Evaluation

The most reliable full reproduction order is summarized below. The phase labels match the linked notebook section headings.

| Phase | Run step | Main inputs | Output / purpose |
|---|---|---|---|
| A0 | Optional source-data audits: [Shriya train audit](notebooks/Shriya_Train_Audit_and_Verification.ipynb#shriya-1-train-data-audit), [Tanisha weather audit](notebooks/Tanisha_Weather_and_Literature_Review.ipynb#tanisha-1-weather-data-audit), [Wahid metadata EDA](notebooks/Wahid_Building_Metadata_and_Models.ipynb#wahid-1-building-metadata-eda) | Raw ASHRAE files | Descriptive checks, missingness summaries, and preprocessing decisions used in the report |
| A1 | [Zahra raw merge](notebooks/Zahra_Integration_and_Ensemble.ipynb#zahra-1-raw-data-loading-and-cross-table-merging) | `train.csv`, `building_metadata.csv`, `weather_train.csv` | Creates `data_processed/merged_train.csv` |
| A2 | [Ayan anomaly investigation](notebooks/Ayan_Anomalies_and_RandomForest.ipynb#ayan-1-anomaly-investigation) | `data_processed/merged_train.csv` | Produces anomaly findings used by the central cleaning pipeline |
| B1 | [Zahra central preprocessing](notebooks/Zahra_Integration_and_Ensemble.ipynb#zahra-2-central-preprocessing-pipeline) | `merged_train.csv` and anomaly findings | Creates `data_processed/final_train.csv` and `data_processed/final_val.csv` |
| B2 | [Shivalika lag/rolling features](notebooks/Shivalika_TimeSeries_and_LightGBM.ipynb#shivalika-2-lag-and-rolling-window-feature-engineering) | `final_train.csv`, `final_val.csv` | Creates `data_processed/final_train_with_features.csv` and `data_processed/final_test_with_features.csv` |
| C | Train individual models: [Wahid models](notebooks/Wahid_Building_Metadata_and_Models.ipynb#wahid-3-training-linear-regression-xgboost-and-catboost-models), [Shivalika models](notebooks/Shivalika_TimeSeries_and_LightGBM.ipynb#shivalika-3-lightgbm-and-xgboost-training-and-tuning), [Ayan models](notebooks/Ayan_Anomalies_and_RandomForest.ipynb#ayan-3-random-forest-training-and-randomizedsearchcv-tuning) | Feature-engineered train/validation files | Saves individual model files and model-result CSVs in `outputs/` |
| D | [Zahra ensemble](notebooks/Zahra_Integration_and_Ensemble.ipynb#zahra-3-five-model-ensemble-comparison), then [save best predictions](notebooks/Zahra_Integration_and_Ensemble.ipynb#zahra-4-best-ensemble-predictions-saved) | Saved models and validation features | Creates `outputs/comparison_table.csv` and `outputs/ensemble_val_predictions.csv` |

Important notes:

- The unused Kaggle `test.csv` merge is not part of the final evaluation workflow because Kaggle `test.csv` has no labels.
- The historical filename `final_test_with_features.csv` refers to the held-out November-December 2016 validation split, not the Kaggle test set.
- Run all model sections in phase C before phase D so the ensemble notebook can find the saved model files.

Model notebook details:

| Notebook | Models trained/evaluated | Saved results |
|---|---|---|
| `Wahid_Building_Metadata_and_Models.ipynb` | Linear Regression, XGBoost, CatBoost baseline | `outputs/linear_boosting_model_results.csv`, saved model files |
| `Shivalika_TimeSeries_and_LightGBM.ipynb` | LightGBM and XGBoost with lag/rolling features | LightGBM/XGBoost metrics and saved model files |
| `Ayan_Anomalies_and_RandomForest.ipynb` | Random Forest and tuned CatBoost comparison | `outputs/baseline_evaluation_results.csv`, Random Forest/CatBoost metrics |
| `Zahra_Integration_and_Ensemble.ipynb` | Hard voting and soft voting ensemble using saved model predictions | `outputs/comparison_table.csv`, `outputs/ensemble_val_predictions.csv` |

The report's best validation result is the soft-voting CatBoost + LightGBM ensemble, with RMSLE approximately `0.4997` on the November-December 2016 held-out validation period.

## Notes on Runtime

The original dataset is large:

- `train.csv`: about 20.2 million rows.
- `test.csv`: about 41.7 million rows.
- The processed and feature-engineered CSVs can be several GB.

Run the notebooks on a machine or Colab runtime with enough memory. If memory is limited, run the audit notebooks first, then run modelling notebooks on sampled data only for verification. The reported results were produced from the full processed training split unless a notebook explicitly states that a sample was used for hyperparameter search.
