import sys
import os
import pandas as pd

# Add the 'scripts' folder to the Python path
sys.path.append(os.path.join(os.getcwd(), 'Preprocessing_scripts'))

from first_script import process_pdb_files  # Assuming 1.py functions are in first_script.py
from second_script import calculate_distances  # Assuming 2.py functions are in second_script.py
from third_script import calculate_biological_properties  # Assuming 3.py functions are in third_script.py
from fourth_script import convert_to_distance_table  # Assuming 4.py functions are in fourth_script.py
from fifth_script import categorize_bins  # Assuming 5.py functions are in fifth_script.py
from sixth_script import generate_vector_cas  # Assuming 6.py functions are in sixth_script.py

def process_pdb_folder(folder_path):
    # Iterate through each PDB file in the "sample_pdb" folder
    for pdb_file in os.listdir(folder_path):
        if pdb_file.endswith(".pdb"):
            pdb_file_path = os.path.join(folder_path, pdb_file)
            
            print(f"Processing {pdb_file}...")
            
            # Step 1: Process PDB Files
            intermediate_data_1 = process_pdb_files(pdb_file_path)
            
            # Step 2: Calculate Distances (assuming this involves residue pairs, etc.)
            intermediate_data_2 = calculate_distances(intermediate_data_1)
            
            # Step 3: Calculate Biological Properties (Area, Perimeter, etc.)
            intermediate_data_3 = calculate_biological_properties(intermediate_data_2)
            
            # Step 4: Convert to Distance Table
            distance_table = convert_to_distance_table(intermediate_data_3)
            
            # Step 5: Categorize Bin Data (Bins are created and filled based on distance values)
            categorized_bins = categorize_bins(distance_table)
            
            # Step 6: Generate Vector for Cas9 (concatenate bin histograms into vectors)
            vectors_df = generate_vector_cas(categorized_bins)
            
            # Save the intermediate results as CSVs
            # Step 1: Save intermediate data from Step 1 (or the results from that step)
            intermediate_data_1.to_csv(f"{pdb_file}_intermediate_data_1.csv", index=False)
            
            # Step 2: Save intermediate data from Step 2
            intermediate_data_2.to_csv(f"{pdb_file}_distances_table.csv", index=False)
            
            # Step 3: Save intermediate data from Step 3 (biological properties)
            intermediate_data_3.to_csv(f"{pdb_file}_biological_properties.csv", index=False)
            
            # Step 4: Save distance table from Step 4
            distance_table.to_csv(f"{pdb_file}_distance_table.csv", index=False)
            
            # Step 5: Save categorized bin data from Step 5
            categorized_bins.to_csv(f"{pdb_file}_bins_histogram.csv", index=True)
            
            # Step 6: Save the final concatenated vector from Step 6
            vectors_df.to_csv(f"{pdb_file}_vector_df.csv", index=False)
            
            print(f"Finished processing {pdb_file}. Intermediate CSVs saved.")

# Specify the folder containing the PDB files (you can update this path)
folder_path = "Data"

# Run the processing function on the folder
process_pdb_folder(folder_path)
