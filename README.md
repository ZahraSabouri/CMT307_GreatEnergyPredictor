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

The helper file `shared/data_loader.py` also contains OneDrive download links used during development. If running in Google Colab, upload the notebooks and either mount/download the data to the matching paths or adapt the first data-loading cell to point to the Colab data folder.

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

The most reliable full reproduction order is:

1. `Zahra_Integration_and_Ensemble.ipynb`, initial merge cells  
   Creates `merged_train.csv` from the original train, building metadata, and weather training files. The unused Kaggle `test.csv` merge is not part of the final workflow.

2. `Ayan_Anomalies_and_RandomForest.ipynb`, anomaly-detection section  
   Produces the anomaly report used by the central cleaning pipeline. Save the combined anomaly table as:

   ```text
   outputs/anomaly_report.csv
   ```

3. `Zahra_Integration_and_Ensemble.ipynb`, central preprocessing cells  
   Applies metadata imputation, weather imputation, feature engineering, anomaly cleaning, target transformation, and chronological train/validation split. This saves:

   ```text
   data_processed/final_train.csv
   data_processed/final_val.csv
   ```

4. `Shivalika_TimeSeries_and_LightGBM.ipynb`, feature-engineering section  
   Adds lag and rolling features and saves the train set plus the held-out validation period. The historical filename `final_test_with_features.csv` refers to the validation split, not the Kaggle test set.

   ```text
   data_processed/final_train_with_features.csv
   data_processed/final_test_with_features.csv
   ```

5. Model notebooks:

   | Notebook | Models trained/evaluated | Saved results |
   |---|---|---|
   | `Wahid_Building_Metadata_and_Models.ipynb` | Linear Regression, XGBoost, CatBoost baseline. | `outputs/linear_boosting_model_results.csv`, saved model files. |
   | `Shivalika_TimeSeries_and_LightGBM.ipynb` | LightGBM and XGBoost with lag/rolling features. | LightGBM/XGBoost metrics and saved model files. |
   | `Ayan_Anomalies_and_RandomForest.ipynb` | Random Forest and tuned CatBoost comparison. | `outputs/baseline_evaluation_results.csv`, Random Forest/CatBoost metrics. |
   | `Zahra_Integration_and_Ensemble.ipynb`, ensemble section | Hard voting and soft voting ensemble using saved model predictions. | `outputs/comparison_table.csv`, `outputs/ensemble_val_predictions.csv`. |

The report's best validation result is the soft-voting CatBoost + LightGBM ensemble, with RMSLE approximately `0.4997` on the November-December 2016 held-out validation period.

## Notes on Runtime

The original dataset is large:

- `train.csv`: about 20.2 million rows.
- `test.csv`: about 41.7 million rows.
- The processed and feature-engineered CSVs can be several GB.

Run the notebooks on a machine or Colab runtime with enough memory. If memory is limited, run the audit notebooks first, then run modelling notebooks on sampled data only for verification. The reported results were produced from the full processed training split unless a notebook explicitly states that a sample was used for hyperparameter search.
