import pandas as pd
import csv


def read_csv(path):
    df = pd.read_csv(path)
    return df


def read_single_csv_file(csv_file_path):
    return csv.DictReader(open(csv_file_path, "r"))
