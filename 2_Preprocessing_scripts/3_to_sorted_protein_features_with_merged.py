import os
import pandas as pd

def generate_sorted_protein_features(input_folder):
    """
    Generate sorted protein features with merged residue pairs for all CSV files in the specified folder.
    Each input file should end with "_lower_diag_features.csv".
    
    Parameters:
        input_folder (str): Path to the folder containing input CSV files.
    
    Output:
        Returns a dictionary of protein names and their corresponding processed DataFrames.
    """
    # Create a dictionary to store the processed DataFrames
    processed_data = {}

    # Iterate through each CSV file in the folder
    for csv_file in os.listdir(input_folder):
        if csv_file.endswith("_lower_diag_features.csv"):
            file_path = os.path.join(input_folder, csv_file)

            # Load the flattened array from the CSV file into a DataFrame
            df = pd.read_csv(file_path, header=None, names=["Residue_Pair", "Distance"])

            # Extract protein name from the filename and remove "_lower_diag_features"
            protein_name = os.path.splitext(os.path.basename(file_path))[0].replace("_lower_diag_features", "")
            print(f"Processing protein: {protein_name}")

            # Sort the DataFrame alphabetically by Residue_Pair
            df = df.sort_values(by="Residue_Pair")

            # Make a copy of the Residue_Pair column
            df['Pair_num'] = df['Residue_Pair']

            # Add the protein name as a new column
            df["Protein"] = protein_name

            # Remove residue numbers only from Residue_Pair column
            df["Residue_Pair"] = df["Residue_Pair"].str.replace(r'\d+', '', regex=True)

            # Reset the DataFrame index
            df.reset_index(drop=True, inplace=True)

            # Create a dictionary to store processed pairs
            processed_pairs = {}

            # Create a new column "Merged_Residue_Pair" and initialize with empty strings
            df["Merged_Residue_Pair"] = ""

            # Iterate through the DataFrame to find converse pairs within the same column
            for index, row in df.iterrows():
                residue_pair = row["Residue_Pair"]

                # Check if the residue_pair has already been processed
                if residue_pair not in processed_pairs:
                    # Generate the converse pair by splitting and rejoining
                    part1, part2 = residue_pair.split('-')
                    converse_pair = f"{part2}-{part1}"

                    # Update the Merged_Residue_Pair values for both pairs
                    df.loc[df["Residue_Pair"].isin([residue_pair, converse_pair]), "Merged_Residue_Pair"] = residue_pair
                    df = df.sort_values(by="Residue_Pair")

                    # Mark both pairs as processed
                    processed_pairs[residue_pair] = True
                    processed_pairs[converse_pair] = True

            # Store the processed DataFrame in the dictionary
            processed_data[protein_name] = df

    # Return the dictionary of processed data
    return processed_data

