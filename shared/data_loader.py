"""
shared/data_loader.py
CMT307 — ASHRAE Great Energy Predictor III

OneDrive links and simple load functions.
Optional — you can also copy a link directly into your notebook.
"""

import os
import subprocess
import pandas as pd

# ── OneDrive direct download links ───────────────────────────────────────────
LINKS = {
    'train.csv':
        'https://cf-my.sharepoint.com/:x:/g/personal/sabouriz_cardiff_ac_uk/'
        'IQCN0mKeylWRRJgG70kcJGsfAVME6MEJRyUGNUlFE82yEbU?e=DYNPJs&download=1',
    'test.csv':
        'https://cf-my.sharepoint.com/:x:/g/personal/sabouriz_cardiff_ac_uk/'
        'IQA1Y4e9ih7FSpIlZXrlMOdaAR3LXc6U1mk--5dnj57_PKY?e=irUVmx&download=1',
    'building_metadata.csv':
        'https://cf-my.sharepoint.com/:x:/g/personal/sabouriz_cardiff_ac_uk/'
        'IQAzX58_8DOgQJIFjQuwLL54AYzodt4TR7l769vXMwkZXiY?e=I7VT4N&download=1',
    'weather_train.csv':
        'https://cf-my.sharepoint.com/:x:/g/personal/sabouriz_cardiff_ac_uk/'
        'IQDof_YFkRqSS4XL2U6CaXWaAR7YHZVLGKDxauFU0oFWqj0?e=xam16n&download=1',
    'weather_test.csv':
        'https://cf-my.sharepoint.com/:x:/g/personal/sabouriz_cardiff_ac_uk/'
        'IQA83EpoZbKWS5bncfDEkL-OAWA3abpQ4UqgAgKwFB5epqE?e=54EvTe&download=1',
    'sample_submission.csv':
        'https://cf-my.sharepoint.com/:x:/g/personal/sabouriz_cardiff_ac_uk/'
        'IQCFRSp3NK7gTJr0DZ1mVOBfAUgU2WuQetyALoHSyd126i4?e=LMXRUn&download=1',
    # Zahra posts these links after finishing Sprint 2
    'merged_train.csv':
        'https://cf-my.sharepoint.com/:x:/g/personal/sabouriz_cardiff_ac_uk/'
        'IQBEO1YwS1wSRpWDJxXx7pxTAWOikO90om10ajVK3vyaI3A?e=HfSqS8&download=1',
    'merged_test.csv':
        'https://cf-my.sharepoint.com/:x:/g/personal/sabouriz_cardiff_ac_uk/'
        'IQAumsA7fXDoTrusA_I02AnVAfQHpesGeHycVXvpNgJtE8g?e=ugA9NI&download=1',
    'final_train.csv':
        'https://cf-my.sharepoint.com/:x:/g/personal/sabouriz_cardiff_ac_uk/'
        'IQBYYGFRl0h_SosJj1qenUAvAX-FnuExRdWVqY7z5GKpkVk?e=m0GqQ1&download=1',
    'final_val.csv':
        'https://cf-my.sharepoint.com/:x:/g/personal/sabouriz_cardiff_ac_uk/'
        'IQD__6nco_j7QYjRjEnFRYD4AdsMPf2ajWr7sU5Q1UXrTZM?e=HsP2Co&download=1',
    'final_test.csv':
        'https://cf-my.sharepoint.com/:x:/g/personal/sabouriz_cardiff_ac_uk/'
        'IQA5n4Rv_nfSQoAJcV0PgT6SAVCWmx389gv9xuSHaGcU2UA?e=zz61B5&download=1',
}


def download(filename, dest='/content'):
    url = LINKS.get(filename, '')
    if not url:
        raise ValueError(f"No link for '{filename}'. Add it to LINKS in data_loader.py.")
    path = os.path.join(dest, filename)
    if not os.path.exists(path):
        print(f'Downloading {filename}...')
        subprocess.run(['wget', '-q', '-O', path, url], check=True)
        print(f'Done: {path}')
    return path


def load_train():
    return pd.read_csv(download('train.csv'), parse_dates=['timestamp'])

def load_test():
    return pd.read_csv(download('test.csv'), parse_dates=['timestamp'])

def load_metadata():
    return pd.read_csv(download('building_metadata.csv'))

def load_weather_train():
    return pd.read_csv(download('weather_train.csv'), parse_dates=['timestamp'])

def load_weather_test():
    return pd.read_csv(download('weather_test.csv'), parse_dates=['timestamp'])

def load_merged_train():
    return pd.read_csv(download('merged_train.csv', dest='/content/data_processed'), parse_dates=['timestamp'])

def load_merged_test():
    return pd.read_csv(download('merged_test.csv', dest='/content/data_processed'), parse_dates=['timestamp'])

def load_final_train():
    return pd.read_csv(download('final_train.csv', dest='/content/data_processed'), parse_dates=['timestamp'])

def load_final_val():
    return pd.read_csv(download('final_val.csv', dest='/content/data_processed'), parse_dates=['timestamp'])

def load_final_test():
    return pd.read_csv(download('final_test.csv', dest='/content/data_processed'), parse_dates=['timestamp'])
