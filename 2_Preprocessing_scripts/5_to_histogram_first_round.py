import os
import pandas as pd
import numpy as np

def categorize_value(value):
    """
    Categorizes the distance value into one of 33 bins.
    """
    try:
        value = float(value)
    except (ValueError, TypeError):
        return "NaN"

    if value == 0:
        return 0
    elif 0 < value <= 5:
        return 1 
    elif 5 < value <= 10:
        return 2
    elif 10 < value <= 15:
        return 3
    elif 15 < value <= 20:
        return 4
    elif 20 < value <= 25:
        return 5
    elif 25 < value <= 30:
        return 6
    elif 30 < value <= 35:
        return 7
    elif 35 < value <= 40:
        return 8
    elif 40 < value <= 45:
        return 9
    elif 45 < value <= 50:
        return 10
    elif 50 < value <= 55:
        return 11
    elif 55 < value <= 60:
        return 12
    elif 60 < value <= 65:
        return 13
    elif 65 < value <= 70:
        return 14
    elif 70 < value <= 75:
        return 15
    elif 75 < value <= 80:
        return 16
    elif 80 < value <= 85:
        return 17
    elif 85 < value <= 90:
        return 18
    elif 90 < value <= 95:
        return 19
    elif 95 < value <= 100:
        return 20
    elif 100 < value <= 105:
        return 21
    elif 105 < value <= 110:
        return 22
    elif 110 < value <= 115:
        return 23
    elif 115 < value <= 120:
        return 24
    elif 120 < value <= 125:
        return 25
    elif 125 < value <= 130:
        return 26
    elif 130 < value <= 135:
        return 27
    elif 135 < value <= 140:
        return 28
    elif 140 < value <= 145:
        return 29
    elif 145 < value <= 150:
        return 30
    elif 150 < value <= 155:
        return 31
    elif 155 < value <= 160:
        return 32
    elif value > 160:
        return 33

def generate_bins_histogram(processed_data):
    """
    Generate a bin histogram for distances in each protein.

    Parameters:
        processed_data (dict): A dictionary with protein names as keys and DataFrames as values.

    Returns:
        dict: A dictionary of DataFrames with binned histogram counts for each protein.
    """
    result_dfs = {}

    # Iterate through each protein in the processed data
    for protein_name, distances_df in processed_data.items():
        # Initialize an empty DataFrame for the result
        result_df = pd.DataFrame(columns=distances_df.columns, index=[f"bin{i + 1}" for i in range(34)])

        # Iterate through each column and categorize the values
        for column in distances_df.columns:
            # Apply the categorization function to the column values
            bin_indices = distances_df[column].apply(categorize_value)

            # Count the frequency of values in each bin
            bin_counts = bin_indices.value_counts().sort_index()

            # Fill the result_df with the frequency counts
            for index, count in bin_counts.items():
                result_df.at[f"bin{index + 1}", column] = count

        # Fill NaN values with 0
        result_df = result_df.fillna(0)

        # Store the result_df for the current protein
        result_dfs[protein_name] = result_df

    # Return the dictionary of bin histograms
    return result_dfs
