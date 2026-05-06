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
    "building_metadata.csv": "https://cf-my.sharepoint.com/:x:/g/personal/sabouriz_cardiff_ac_uk/IQBK8fFORza5Q4_97St_AANFAd99aWRgC1zgvgjj3i3leDY?e=Nw5caf",
    "sample_submission.csv": "https://cf-my.sharepoint.com/:x:/g/personal/sabouriz_cardiff_ac_uk/IQDHztyqs5OLRZzfF6h3KgjRAc8aGdXgAzLI9FWobnecYWk?e=dXxpOf",
    "test.csv": "https://cf-my.sharepoint.com/:x:/g/personal/sabouriz_cardiff_ac_uk/IQCbjO6qXY6qTYbStUYJJUF6ATo5GTF3NDBKMPWZd-aZOCE?e=rnq4OW",
    "train.csv": "https://cf-my.sharepoint.com/:x:/g/personal/sabouriz_cardiff_ac_uk/IQAZUdJPeR5kR6zuSEWshIZGAWI-m9MyDlt-eVHUJte35v4?e=I0Yxne",
    "weather_test.csv": "https://cf-my.sharepoint.com/:x:/g/personal/sabouriz_cardiff_ac_uk/IQAqRfg2ZCneQL2OqvEk6LHVAZXBz2mu97VLrhRZHtMijqA?e=RBlWF7",
    "weather_train.csv": "https://cf-my.sharepoint.com/:x:/g/personal/sabouriz_cardiff_ac_uk/IQB0qhBcd456RJrhn9dxCVOfAQui3rF7Xa8owpzEJbEsJ48?e=k0DU3Q",

    # Processed pipeline files
    "building_metadata_processed.csv": "https://cf-my.sharepoint.com/:x:/g/personal/sabouriz_cardiff_ac_uk/IQCACHSBedzvR5O4P57J0d5hAd72C0FniTJJX0VVstzLUOY?e=jkaaHX",
    "final_test.csv": "https://cf-my.sharepoint.com/:x:/g/personal/sabouriz_cardiff_ac_uk/IQDuc9ZYOD2wSbYkSRE0tllLAW_X4sijWc5xcMa8IoDyaXw?e=EUAuxt",
    "final_test_with_features.csv": "https://cf-my.sharepoint.com/:x:/g/personal/sabouriz_cardiff_ac_uk/IQDe18jGGih8SKSMt53CtU_PAU_siG8PbMKixmVbOpBVgUU?e=A7CDD2",
    "final_train.csv": "https://cf-my.sharepoint.com/:x:/g/personal/sabouriz_cardiff_ac_uk/IQAuHiXJX_-CQYDc8qd0AHpAAYVoECeJadryY0VB4pYBd6I?e=tVGPAc",
    "final_train_with_features.csv": "",
    "final_val.csv": "https://cf-my.sharepoint.com/:x:/g/personal/sabouriz_cardiff_ac_uk/IQDBA6R9AtvOQqIn67SnS9qXAWyqYDB_3oWOneGVYtsYj9o?e=hia7DH",
    "merged_test.csv": "https://cf-my.sharepoint.com/:x:/g/personal/sabouriz_cardiff_ac_uk/IQCSunGTLwbBSqDFv-dyYIt_AeAWm9yII4FeSSj4ivRGZZI?e=gBf4Rh",
    "merged_train.csv": "https://cf-my.sharepoint.com/:x:/g/personal/sabouriz_cardiff_ac_uk/IQBfpx0HUAaCSo2S3nPqwQCAAVeLEVtQZCz88E2XXfpmR2o?e=WxhgPh",
    "weather_test_processed.csv": "https://cf-my.sharepoint.com/:x:/g/personal/sabouriz_cardiff_ac_uk/IQC9KJl8LfcTS4HdAXsr0kH2AXQnrznG2WxJOk9a3KKQCj4?e=LfSt2v",
    "weather_train_processed.csv": "https://cf-my.sharepoint.com/:x:/g/personal/sabouriz_cardiff_ac_uk/IQDotlYpc0k8TpUitUFMlR4wAdZ5YS0-8PFJyFOSwqTv9Jc?e=4L5o44",

    # Output CSVs
    "anomaly_report.csv": "https://cf-my.sharepoint.com/:x:/g/personal/sabouriz_cardiff_ac_uk/IQCcjfTXfmWzQbZ4VkRyzZxJAUZ5KSy1sJLQRuRa-CLbWiw?e=c5HNX2",
    "baseline_evaluation_results.csv": "https://cf-my.sharepoint.com/:x:/g/personal/sabouriz_cardiff_ac_uk/IQB1KInY1RwPSKqt5ov1NIbeAZWVox1oc7zvFzG6RS6afTE?e=9fnI92",
    "comparison_table.csv": "https://cf-my.sharepoint.com/:x:/g/personal/sabouriz_cardiff_ac_uk/IQBvdAZGIepAQqram5xKLc6qAUn6BabRDe0H29qMUKXYh5Q?e=aNa84U",
    "ensemble_val_predictions.csv": "https://cf-my.sharepoint.com/:x:/g/personal/sabouriz_cardiff_ac_uk/IQC3Cl9QkIDPSJ9AAFHK4Kn2AbEyibVAnx85z4A0Aig25Mc?e=YtKYNV",
    "linear_boosting_model_results.csv": "https://cf-my.sharepoint.com/:x:/g/personal/sabouriz_cardiff_ac_uk/IQC4CujT5kjDR7bWZOxc4vB8AY_2o7xHz-aPkA-0hHduvgk?e=nTxZDk",
    "random_forest_model_results.csv": "https://cf-my.sharepoint.com/:x:/g/personal/sabouriz_cardiff_ac_uk/IQD2-x0hgHF0QKJEgVqgkaHlAcW4d6S7cJ17AvXxFZ-rJnE?e=VzaSQj",

    # Saved models
    "catboost_model.pkl": "https://cf-my.sharepoint.com/:u:/g/personal/sabouriz_cardiff_ac_uk/IQD3VQplSaO6TYxBUPTPm6uNAfMh1eW_SnzfGnMdZSidZmE?e=3c4WXh",
    "cat_tuned_model.pkl": "https://cf-my.sharepoint.com/:u:/g/personal/sabouriz_cardiff_ac_uk/IQC15FRcnAh9TZOtep353Pb4AW2lDpWUJ5RBrnQTYkzLfTQ?e=BeQTd9",
    "cat_tuned_model.pkl.bak": "https://cf-my.sharepoint.com/:u:/g/personal/sabouriz_cardiff_ac_uk/IQAae1AFkO76Qr2H7G9xZ_VsAcRduT9RK1wkA-_0LNV_7f4?e=tLh127",
    "lightgbm_model.pkl": "https://cf-my.sharepoint.com/:u:/g/personal/sabouriz_cardiff_ac_uk/IQAwLgplkhzpRaWF9yQatU35AVIo4ifBaU0PUFqtnQSVrRg?e=UCz7pn",
    "lightgbm_model.pkl.bak": "https://cf-my.sharepoint.com/:u:/g/personal/sabouriz_cardiff_ac_uk/IQACr0nBnMLuTaKN8rdNuYgZAY2HAkLQO8ajeGalosyT9AA?e=6uHYYM",
    "lr_model.pkl": "https://cf-my.sharepoint.com/:u:/g/personal/sabouriz_cardiff_ac_uk/IQDmA2fLBsz6S5R0XzhAk33PARVLOBFU2SNtCMDDmUH9SoM?e=8PlU8i",
    "rf_model.pkl": "https://cf-my.sharepoint.com/:u:/g/personal/sabouriz_cardiff_ac_uk/IQBgBBzqopsaQqhFv6e12spjASu3nsbZ51a1XlbnGQRnbao?e=B6RxoS",
    "rf_model2.pkl": "https://cf-my.sharepoint.com/:u:/g/personal/sabouriz_cardiff_ac_uk/IQBzBK97wzjaQ5cBqja4mK5aAT3mhVsHhxwA_DMdP_iOecY?e=cWhgVC",
    "rf_model_depth10.pkl": "https://cf-my.sharepoint.com/:u:/g/personal/sabouriz_cardiff_ac_uk/IQAn6CeT9PkhSIt4wY3qrmzJAbxtYrNCF7GeomMX1mW9nLs?e=2aT4vg",
    "rf_model_depth20.pkl": "https://cf-my.sharepoint.com/:u:/g/personal/sabouriz_cardiff_ac_uk/IQCwPO7LoRaNS49aB0ClODq5ATO_hm46dnBEGZYgiyNSnMw?e=YQiohO",
    "rf_tuned_model.pkl": "https://cf-my.sharepoint.com/:u:/g/personal/sabouriz_cardiff_ac_uk/IQC_UoSMEA0SQL3Pn8foAuXmAXlwH8uLWeVBVJ0jj6-Bizc?e=ZYPmxP",
    "xgb_model.pkl": "https://cf-my.sharepoint.com/:u:/g/personal/sabouriz_cardiff_ac_uk/IQCOye-Kd1egRZb0uYEdL9FcATaJx_LcBcayd0ECJjIxgBs?e=iwxa3D",

    # Output figures
    "actual_vs_predicted_sv2_hv2.png": "https://cf-my.sharepoint.com/:i:/g/personal/sabouriz_cardiff_ac_uk/IQB9z_wQk6OiR6SoZ3elkZ69AdFdO9oSMtzr7wqumPlEHOA?e=xTEIpV",
    "ensemble_comparison.png": "https://cf-my.sharepoint.com/:i:/g/personal/sabouriz_cardiff_ac_uk/IQDUMqDOikAnRIUBtIPJFQMxAWqYA2Z4vKQncghK9ry4Vh8?e=ziu3Uj",
    "residuals_sv2_hv2.png": "https://cf-my.sharepoint.com/:i:/g/personal/sabouriz_cardiff_ac_uk/IQDFbwvWFE_XRbSLIRC9ARNDARKk-p95DzJXxiAehzyxCHw?e=QR0wX0",
    "rmsle_per_meter_type_all_models.png": "https://cf-my.sharepoint.com/:i:/g/personal/sabouriz_cardiff_ac_uk/IQCjtF3Efm_wTrfP0McaVCcAAVA66RX05mgxTfCH7QiUb9M?e=5ysYjL",
    "scatter_lightgbm_predicted_vs_actual.png": "https://cf-my.sharepoint.com/:i:/g/personal/sabouriz_cardiff_ac_uk/IQAqW0mdYONBT5EKKpiUPAOpAQjxL5ps3XhJZk_WLIHvZkc?e=QZMho8",
    "shivalika_time_series_patterns.png": "https://cf-my.sharepoint.com/:i:/g/personal/sabouriz_cardiff_ac_uk/IQBGwVRsDbrTT6WTwwPvWBBvAYOQ7nz-6dJ76XvLeNjRLFI?e=ZXX33M",
    "wahid_imputation_results.png": "https://cf-my.sharepoint.com/:i:/g/personal/sabouriz_cardiff_ac_uk/IQAb5COVBcMBSomcdSk-NMAeAYPVggek6BAUf0TEpjPOIIw?e=buYPU5",
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