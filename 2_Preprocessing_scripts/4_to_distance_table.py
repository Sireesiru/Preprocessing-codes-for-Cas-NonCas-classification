import os
import pandas as pd
import numpy as np

def generate_distances_table(input_folder, processed_data):
    """
    Generate a distances table from the sorted protein features with merged residue pairs.

    Parameters:
        input_folder (str): Path to the folder containing the input CSV files.
        processed_data (DataFrame): The processed DataFrame from the previous step with merged residue pairs.

    Returns:
        DataFrame: The resulting distance table for each protein.
    """
    # Read residue_converse_pair.csv to get residue_pairs and converse_pairs
    pair_df = pd.read_csv("Cas9_AlphaFold_885/merged/residue_converse_pair.csv", usecols=["residue_pairs", "converse_pairs"])
    residue_pairs = pair_df["residue_pairs"].tolist()
    converse_pairs = pair_df["converse_pairs"].tolist()

    # Create a dictionary to store distance values for each pair
    pair_distances = {}

    # Process each protein from the processed_data
    for protein_name, df22 in processed_data.items():
        # Sort the DataFrame by Merged_Residue_Pair
        df22 = df22.sort_values("Merged_Residue_Pair")

        # Iterate through residue_pairs and converse_pairs
        for pair in residue_pairs:
            # Find the pair in the "Merged_Residue_Pair" column of df22
            matched_rows = df22[df22["Merged_Residue_Pair"] == pair]

            # If a match is found, store the distance values for this pair
            if not matched_rows.empty:
                pair_distances[pair] = matched_rows["Distance"].tolist()
            else:
                # If no match found, find its converse pair
                converse_pair = converse_pairs[residue_pairs.index(pair)]
                matched_rows = df22[df22["Merged_Residue_Pair"] == converse_pair]
                
                if not matched_rows.empty:
                    pair_distances[pair] = matched_rows["Distance"].tolist()

        # Determine the maximum length of arrays in the dictionary
        max_length = max(len(arr) for arr in pair_distances.values())

        # Create an empty DataFrame with zeros
        final_df = pd.DataFrame(0, columns=residue_pairs, index=range(max_length))

        # Iterate through the keys and values in the dictionary to populate the DataFrame
        for key, values in pair_distances.items():
            # Pad the values with zeros to match the maximum length
            values += [0] * (max_length - len(values))
            final_df[key] = values

        final_df.fillna(0, inplace=True)

        # Return the final DataFrame (no saving to file here)
        return final_df