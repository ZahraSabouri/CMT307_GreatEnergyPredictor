"""
shared/data_loader.py
CMT307 - ASHRAE Great Energy Predictor III

Central file registry and simple loading helpers.

Add OneDrive/SharePoint direct-download URLs to LINKS when needed. The link
strings are intentionally empty so they can be filled in manually. Local files
are used first, so the loaders work without links when the files already exist.
"""

from pathlib import Path
from urllib.request import urlretrieve

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DATA_DIR = PROJECT_ROOT / "data" / "ashrae-energy-prediction"
PROCESSED_DATA_DIR = PROJECT_ROOT / "data_processed"
OUTPUTS_DIR = PROJECT_ROOT / "outputs"


RAW_DATA_FILES = (
    "building_metadata.csv",
    "sample_submission.csv",
    "test.csv",
    "train.csv",
    "weather_test.csv",
    "weather_train.csv",
)

PROCESSED_DATA_FILES = (
    "building_metadata_processed.csv",
    "final_test.csv",
    "final_test_with_features.csv",
    "final_train.csv",
    "final_train_with_features.csv",
    "final_val.csv",
    "merged_test.csv",
    "merged_train.csv",
    "weather_test_processed.csv",
    "weather_train_processed.csv",
)

OUTPUT_FILES = (
    "actual_vs_predicted_sv2_hv2.png",
    "anomaly_report.csv",
    "baseline_evaluation_results.csv",
    "catboost_model.pkl",
    "cat_tuned_model.pkl",
    "cat_tuned_model.pkl.bak",
    "comparison_table.csv",
    "ensemble_comparison.png",
    "ensemble_val_predictions.csv",
    "lightgbm_model.pkl",
    "lightgbm_model.pkl.bak",
    "linear_boosting_model_results.csv",
    "lr_model.pkl",
    "random_forest_model_results.csv",
    "residuals_sv2_hv2.png",
    "rf_model.pkl",
    "rf_model2.pkl",
    "rf_model_depth10.pkl",
    "rf_model_depth20.pkl",
    "rf_tuned_model.pkl",
    "rmsle_per_meter_type_all_models.png",
    "scatter_lightgbm_predicted_vs_actual.png",
    "shivalika_time_series_patterns.png",
    "wahid_imputation_results.png",
    "xgb_model.pkl",
)


FILE_PATHS = {
    **{filename: RAW_DATA_DIR / filename for filename in RAW_DATA_FILES},
    **{filename: PROCESSED_DATA_DIR / filename for filename in PROCESSED_DATA_FILES},
    **{filename: OUTPUTS_DIR / filename for filename in OUTPUT_FILES},
}


LINKS = {
    # Raw ASHRAE files
    "building_metadata.csv": "",
    "sample_submission.csv": "",
    "test.csv": "",
    "train.csv": "",
    "weather_test.csv": "",
    "weather_train.csv": "",

    # Processed pipeline files
    "building_metadata_processed.csv": "",
    "final_test.csv": "",
    "final_test_with_features.csv": "",
    "final_train.csv": "",
    "final_train_with_features.csv": "",
    "final_val.csv": "",
    "merged_test.csv": "",
    "merged_train.csv": "",
    "weather_test_processed.csv": "",
    "weather_train_processed.csv": "",

    # Output CSVs
    "anomaly_report.csv": "",
    "baseline_evaluation_results.csv": "",
    "comparison_table.csv": "",
    "ensemble_val_predictions.csv": "",
    "linear_boosting_model_results.csv": "",
    "random_forest_model_results.csv": "",

    # Saved models
    "catboost_model.pkl": "",
    "cat_tuned_model.pkl": "",
    "cat_tuned_model.pkl.bak": "",
    "lightgbm_model.pkl": "",
    "lightgbm_model.pkl.bak": "",
    "lr_model.pkl": "",
    "rf_model.pkl": "",
    "rf_model2.pkl": "",
    "rf_model_depth10.pkl": "",
    "rf_model_depth20.pkl": "",
    "rf_tuned_model.pkl": "",
    "xgb_model.pkl": "",

    # Output figures
    "actual_vs_predicted_sv2_hv2.png": "",
    "ensemble_comparison.png": "",
    "residuals_sv2_hv2.png": "",
    "rmsle_per_meter_type_all_models.png": "",
    "scatter_lightgbm_predicted_vs_actual.png": "",
    "shivalika_time_series_patterns.png": "",
    "wahid_imputation_results.png": "",
}


TIMESTAMP_FILES = {
    "anomaly_report.csv",
    "ensemble_val_predictions.csv",
    "final_test.csv",
    "final_test_with_features.csv",
    "final_train.csv",
    "final_train_with_features.csv",
    "final_val.csv",
    "merged_test.csv",
    "merged_train.csv",
    "test.csv",
    "train.csv",
    "weather_test.csv",
    "weather_test_processed.csv",
    "weather_train.csv",
    "weather_train_processed.csv",
}


def list_files():
    """Return all registered filenames."""
    return sorted(FILE_PATHS)


def path_for(filename):
    """Return the expected local path for a registered file."""
    try:
        return FILE_PATHS[filename]
    except KeyError as exc:
        known = ", ".join(list_files())
        raise KeyError(f"Unknown file '{filename}'. Known files: {known}") from exc


def download(filename, dest=None):
    """
    Download a registered file if it is missing and return its local path.

    If dest is given, the file is downloaded to that directory. Otherwise the
    project-standard directory from FILE_PATHS is used.
    """
    path = Path(dest) / filename if dest is not None else path_for(filename)
    if path.exists():
        return str(path)

    url = LINKS.get(filename, "").strip()
    if not url:
        raise ValueError(f"No link for '{filename}'. Add it to LINKS in data_loader.py.")

    path.parent.mkdir(parents=True, exist_ok=True)
    print(f"Downloading {filename}...")
    urlretrieve(url, path)
    print(f"Done: {path}")
    return str(path)


def get_path(filename, download_if_missing=True):
    """Return a local path, downloading the file first if needed."""
    path = path_for(filename)
    if path.exists():
        return path
    if download_if_missing:
        return Path(download(filename))
    raise FileNotFoundError(f"Missing file: {path}")


def load_csv(filename, **read_csv_kwargs):
    """Load a registered CSV file with timestamp parsing where applicable."""
    if filename in TIMESTAMP_FILES and "parse_dates" not in read_csv_kwargs:
        read_csv_kwargs["parse_dates"] = ["timestamp"]
    return pd.read_csv(get_path(filename), **read_csv_kwargs)


def load_model(filename):
    """Load a registered pickle/joblib model file."""
    import joblib

    return joblib.load(get_path(filename))


def load_train():
    return load_csv("train.csv")


def load_test():
    return load_csv("test.csv")


def load_metadata():
    return load_csv("building_metadata.csv")


def load_building_metadata():
    return load_metadata()


def load_weather_train():
    return load_csv("weather_train.csv")


def load_weather_test():
    return load_csv("weather_test.csv")


def load_sample_submission():
    return load_csv("sample_submission.csv")


def load_building_metadata_processed():
    return load_csv("building_metadata_processed.csv")


def load_merged_train():
    return load_csv("merged_train.csv")


def load_merged_test():
    return load_csv("merged_test.csv")


def load_final_train():
    return load_csv("final_train.csv")


def load_final_val():
    return load_csv("final_val.csv")


def load_final_test():
    return load_csv("final_test.csv")


def load_final_train_with_features():
    return load_csv("final_train_with_features.csv")


def load_final_test_with_features():
    return load_csv("final_test_with_features.csv")


def load_weather_train_processed():
    return load_csv("weather_train_processed.csv")


def load_weather_test_processed():
    return load_csv("weather_test_processed.csv")


def load_anomaly_report():
    return load_csv("anomaly_report.csv")


def load_baseline_evaluation_results():
    return load_csv("baseline_evaluation_results.csv")


def load_comparison_table():
    return load_csv("comparison_table.csv")


def load_ensemble_val_predictions():
    return load_csv("ensemble_val_predictions.csv")


def load_linear_boosting_model_results():
    return load_csv("linear_boosting_model_results.csv")


def load_random_forest_model_results():
    return load_csv("random_forest_model_results.csv")


def load_catboost_model():
    return load_model("catboost_model.pkl")


def load_cat_tuned_model():
    return load_model("cat_tuned_model.pkl")


def load_lightgbm_model():
    return load_model("lightgbm_model.pkl")


def load_lr_model():
    return load_model("lr_model.pkl")


def load_rf_model():
    return load_model("rf_model.pkl")


def load_rf_model2():
    return load_model("rf_model2.pkl")


def load_rf_model_depth10():
    return load_model("rf_model_depth10.pkl")


def load_rf_model_depth20():
    return load_model("rf_model_depth20.pkl")


def load_rf_tuned_model():
    return load_model("rf_tuned_model.pkl")


def load_xgb_model():
    return load_model("xgb_model.pkl")
