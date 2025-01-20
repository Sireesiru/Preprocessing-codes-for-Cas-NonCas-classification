import pandas as pd
import numpy as np

def generate_vector_cas(result_dfs):
    """
    Generate concatenated vectors for each protein based on the bin histograms.

    Parameters:
        result_dfs (dict): A dictionary with protein names as keys and DataFrames (bin histograms) as values.

    Returns:
        pd.DataFrame: A DataFrame containing protein names and their corresponding concatenated vectors.
    """
    vectors_data = []

    # Iterate through each protein's bin histogram DataFrame
    for protein_name, result_df in result_dfs.items():
        # Initialize an empty list to store the concatenated vector
        concatenated_vector = []

        # Iterate through each column and concatenate the values
        for column in result_df.columns:
            values = result_df[column].values  # Extract the column values
            concatenated_vector.extend(values)
        
        # Append the concatenated vector along with the protein name
        vectors_data.append({"Protein": protein_name, "Vector": concatenated_vector})

    # Create a DataFrame from the concatenated vectors
    vector_df = pd.DataFrame(vectors_data)

    # Return the DataFrame of concatenated vectors
    return vector_df
