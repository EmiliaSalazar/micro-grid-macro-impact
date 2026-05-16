# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import csv
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import textwrap

def analyze_csv_ranges(file_path,delim=","):
    """
    Analyze a CSV file to separate columns and find ranges for all columns.
    For numeric columns: calculates min, max, range
    For text columns: shows unique count and sample values
    """

    # Read the CSV file
    try:
        df = pd.read_csv(file_path,delimiter=delim,index_col='ts', parse_dates=True)
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    #print(df.describe())
    print("-" * 80)
    print(f"File: {file_path}")
    print(f"Total rows: {len(df)}")
    print(f"Total columns: {len(df.columns)}")
    print("-" * 80)

    df = df[df.index >= pd.to_datetime("2025-05-15")]

    for i, column in enumerate(df.columns):
        print("-" * 80)
        print(f"Column {i}: {column}")
        print("-" * 80)
        col_data = df[column]

        if pd.api.types.is_numeric_dtype(col_data): # Check if data is numeric
            clean_data = col_data.dropna()
            if len(clean_data)>0:
                min_val = clean_data.min()
                max_val = clean_data.max()
                print(f"Minimim Value: {min_val}")
                print(f"Maximum Value: {max_val}")
                print(f"Mean: {clean_data.mean():.2f}")
            else:
                print("All NaN or empty")
        else: 
            print("Type: Text/Categorcal")

        print(f"Preview of Column:")
        print(col_data[:3])
        print(col_data[-3:])
        print(f"Total values: {len(col_data)}")
        print(f"Unique values: {col_data.nunique()}")
        print(f"Missing values: {col_data.isna().sum()}")
        print(f"Fraction of No Readings {col_data.isna().sum()/len(col_data)} ")
        print(f"Fraction of +-0.1 readings {(abs(col_data) <= 0.1).sum()/len(col_data)} ")



    return df
# %%
