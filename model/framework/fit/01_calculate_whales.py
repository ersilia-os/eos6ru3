import sys
import os
import csv
from tqdm import tqdm
from rdkit import Chem

root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(root, "..", "code", "whales"))
import do_whales
from ChemTools import prepare_mol


CHECKPOINTS_FOLDER = os.path.join(root, "..", "..", "checkpoints")
STRUCTURES_FOLDER = os.path.join(root, "..", "..", "checkpoints", "structures")

chembl_ids = []
for chembl_id in tqdm(os.listdir(STRUCTURES_FOLDER)):
    chembl_ids += [chembl_id]
chembl_ids = sorted(chembl_ids)

with open(os.path.join(CHECKPOINTS_FOLDER, "chembl_ids.txt"), "w") as f:
    for chembl_id in chembl_ids:
        f.write(chembl_id + os.linesep)


def read_molecule_sdf_file(sdf_file):
    suppl = Chem.SDMolSupplier(sdf_file, sanitize=False)
    for m in suppl:
        return prepare_mol(m, do_geometry=False, do_charge=False)[0]


for chembl_id in tqdm(chembl_ids[:3]):
    R0 = []
    R1 = []
    R2 = []
    molecule_folder = os.path.join(STRUCTURES_FOLDER, chembl_id)
    sdf_files = [l for l in os.listdir(molecule_folder)]
    sdf_files = sorted(sdf_files)
    if len(sdf_files) > 3:
        sdf_files = sdf_files[:3]
    if len(sdf_files) == 1:
        sdf_files = [sdf_files[0], sdf_files[0], sdf_files[0]]
    if len(sdf_files) == 2:
        sdf_files = [sdf_files[0], sdf_files[1], sdf_files[0]]
    m0 = read_molecule_sdf_file(os.path.join(molecule_folder, sdf_files[0]))
    m1 = read_molecule_sdf_file(os.path.join(molecule_folder, sdf_files[1]))
    m2 = read_molecule_sdf_file(os.path.join(molecule_folder, sdf_files[2]))
    m0_whales, lab0 = do_whales.whales_from_mol(m0)
    m1_whales, lab1 = do_whales.whales_from_mol(m1)
    m2_whales, lab2 = do_whales.whales_from_mol(m2)
    R0 += [m0_whales]
    R1 += [m1_whales]
    R2 += [m2_whales]


with open(os.path.join(CHECKPOINTS_FOLDER, "R0.csv"), "w") as f:
    writer = csv.writer(f)
    writer.writerow(lab0)
    for r0 in R0:
        writer.writerow(r0)

with open(os.path.join(CHECKPOINTS_FOLDER, "R1.csv"), "w") as f:
    writer = csv.writer(f)
    writer.writerow(lab0)
    for r1 in R1:
        writer.writerow(r1)

with open(os.path.join(CHECKPOINTS_FOLDER, "R2.csv"), "w") as f:
    writer = csv.writer(f)
    writer.writerow(lab2)
    for r2 in R2:
        writer.writerow(r2)
