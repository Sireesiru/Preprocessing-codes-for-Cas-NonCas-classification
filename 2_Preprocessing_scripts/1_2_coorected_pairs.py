import os
import numpy as np
import pandas as pd
from Bio import PDB
import math

pdb_folder = "sample_pdb"

# Initialize a PDB parser
parser = PDB.PDBParser(QUIET=True)

# List of PDB files in the folder
pdb_files = [filename for filename in os.listdir(pdb_folder) if filename.endswith(".pdb")]

# Iterate through each PDB file
for pdb_file in pdb_files:
    pdb_path = os.path.join(pdb_folder, pdb_file)
    print(f"Processing: {pdb_file}")
    
    # Parse the PDB structure
    structure = parser.get_structure("protein", pdb_path)

    # Extract C-alpha coordinates and residue names
    c_alpha_coordinates = []
    residue_names = []

    for model in structure:
        for chain in model:
            c_alpha_coords_chain = []
            residue_names_chain = []
            for residue in chain:
                if residue.get_id()[0] == " " and residue.has_id("CA"):
                    c_alpha_coords_chain.append(residue["CA"].get_coord())
                    residue_names_chain.append(residue.get_resname() + str(residue.get_id()[1]))
            c_alpha_coordinates.append(c_alpha_coords_chain)
            residue_names.append(residue_names_chain)

    # Calculate complete C-alpha to C-alpha distances
    num_residues = len(c_alpha_coordinates[0])
    distances = np.zeros((num_residues, num_residues), dtype=float)
    for i in range(num_residues):
        for j in range(i + 1, num_residues):  # Iterate only over the lower triangle
            dist = np.linalg.norm(c_alpha_coordinates[0][i] - c_alpha_coordinates[0][j])
            distances[i, j] = distances[j, i] = dist  # Store distances symmetrically

    # Create the flattened array with residue pair names and distances
    num_pairs = (num_residues * (num_residues - 1)) // 2  # Number of pairs in lower triangle only
    flattened_array = np.empty((2, num_pairs), dtype=object)
    idx = 0
    for i in range(num_residues):
        for j in range(i + 1, num_residues):
            formatted_dist = "{:.3f}".format(distances[i, j])  # Save distances up to 3 decimal points
            flattened_array[0, idx] = f"{residue_names[0][i]}-{residue_names[0][j]}"
            flattened_array[1, idx] = formatted_dist
            idx += 1

    # Correcting Residue Pair Format
    corrected_pairs = []
    for pair in flattened_array[0]:
        parts = pair.split("-")
        if (len(parts) == 4) and any(part.isdigit() for part in parts):
            cor_pair = f"{(parts[0])}{abs(int(parts[1]))}-{(parts[2])}{abs(int(parts[3]))}"
            corrected_pairs.append(cor_pair)
        elif (len(parts) == 3) and parts[1].isdigit():
            cor_pair = f"{parts[0]}{parts[1]}-{parts[2]}"
            corrected_pairs.append(cor_pair)
        elif (len(parts) == 3) and parts[2].isdigit():
            cor_pair = f"{parts[0]}-{parts[1]}{parts[2]}"
            corrected_pairs.append(cor_pair)
        else:
            corrected_pairs.append(pair)

    # Update the pair names with corrected format
    flattened_array[0] = corrected_pairs

    # Save the final corrected and flattened array as a CSV file
    output_file = os.path.join(pdb_folder, os.path.splitext(pdb_file)[0] + "_lower_diag_features.csv")
    np.savetxt(output_file, flattened_array.T, delimiter=",", fmt="%s")

    print(f"Processed and saved: {output_file}")

