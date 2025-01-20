#########################  Second time vector_cas ########################## 

import os
import pandas as pd
import numpy as np

# Specify the folder containing the _result_df.csv files
folder_path = "sample_pdb"

# Initialize an empty list to store the concatenated vectors
vectors_data = []

# Iterate through each CSV file in the folder
for csv_file in os.listdir(folder_path):
    if csv_file.endswith("_bins_histogram.csv"):
        file_path = os.path.join(folder_path, csv_file)
        
        # Extract protein name from the filename
        protein_name = os.path.splitext(os.path.basename(file_path))[0].replace("_bins_histogram", "")
        # Load the CSV file
        result_df = pd.read_csv(file_path, skiprows=list(np.arange(1, 3)))  # Skip the 2nd and 3rd rows
        result_df = result_df.iloc[:-1, :]  # Skip the last row
        result_df = result_df.iloc[:, 1:]
        # Extract values from the DataFrame (excluding the first column)
        values = result_df.values.flatten(order='F')     
        # Append the protein name and the flattened vector to the list
        vectors_data.append(np.concatenate([[protein_name], values]))
        
# Create a DataFrame from the list of concatenated vectors
column_names = ['Protein'] + [f'bit{i+1}' for i in range(len(vectors_data[0])-1)]
#print(column_names)
vector_df = pd.DataFrame(vectors_data, columns=column_names)
#display(vector_df)

# Add a new column "label" to vector_df
vector_df['label'] = None

# Read the sg DataFrame separately
sg = pd.read_csv("COMBINED2000_new/labels.csv")

# Iterate through the rows of vector_df
for index, row in vector_df.iterrows():
    protein_name = row['Protein']

    # Find the corresponding label in sg DataFrame
    matching_row = sg[sg['pro'] == protein_name]

    # Check if a match is found
    if not matching_row.empty:
        label_value = matching_row.iloc[0]['label']
        # Update the "label" column in vector_df
        vector_df.at[index, 'label'] = label_value
vector_df['label'] = vector_df['label'].fillna(0)
display(vector_df)
vector_df.to_csv("sample_pdb/vector_df_second.csv", index=False)