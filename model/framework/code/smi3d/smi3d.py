import os
import csv
import argparse
import subprocess
import tempfile
import shutil
from rdkit import Chem
from rdkit.Chem import inchi
from rdkit import RDLogger
import sys

RDLogger.DisableLog('rdApp.*')  

root = os.path.dirname(os.path.abspath(__file__))

python_path = sys.executable

tmp_dir = tempfile.mkdtemp(prefix='smi3d_')


def main() -> None:
    args = parseArgs()

    input_file = os.path.join(tmp_dir, 'input.sdf')
    output_file = os.path.join(tmp_dir, 'output.sdf')

    with open(args.in_file, 'r') as f:
        reader = csv.reader(f)
        smiles_list = [row[0] for row in reader]
        if smiles_list[0].lower().startswith("smiles") or smiles_list[0].lower().endswith("smiles"):
            smiles_list = smiles_list[1:]

    idxs = []
    mols = []
    for i, smi in enumerate(smiles_list):
        mol = Chem.MolFromSmiles(smi)
        if mol is None:
            continue
        idxs += [i]
        mol.SetProp("_InputIndex", str(i))
        mol.SetProp("_InputSMILES", str(smi))
        mol.SetProp("_InputInChIKey", str(inchi.InchiToInchiKey(inchi.MolToInchi(Chem.MolFromSmiles(smi)))))
        mol.SetProp("_SMILES", str(Chem.MolToSmiles(mol)))
        mol.SetProp("_InChIKey", str(inchi.InchiToInchiKey(inchi.MolToInchi(mol))))
        mols += [mol]

    writer = Chem.SDWriter(input_file)
    for m in mols:
        writer.write(m)
    writer.close()

    if args.num_confs == 1:
        cmd = "{0} {1}/tools/gen_3d_structs.py -i {2} -o {3} -t {4}".format(python_path, root, input_file, output_file, args.max_time)
    else:
        cmd = "{0} {1}/tools/gen_confs.py -i {2} -o {3} -t {4} -n {5}".format(python_path, root, input_file, output_file, args.max_time, args.num_confs)

    subprocess.Popen(cmd, shell=True).wait()

    shutil.copyfile(output_file, args.out_file)
    shutil.rmtree(tmp_dir)


def parseArgs() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Generates conformers for a given list of SMILES strings.')

    parser.add_argument('-i',
                        dest='in_file',
                        required=True,
                        metavar='<file>',
                        help='Molecule input file in CSV format. A column named "smiles" is required.')
    parser.add_argument('-o',
                        dest='out_file',
                        required=True,
                        metavar='<file>',
                        help='Output file in SDF SDF format.')
    parser.add_argument('-t',
                        dest='max_time',
                        required=False,
                        metavar='<int>',
                        type=int,
                        default=60,
                        help='Max. allowed molecule processing time (default: 60 sec)')
    parser.add_argument('-q',
                        dest='quiet',
                        required=False,
                        action='store_true',
                        default=False,
                        help='Disable progress output (default: false)')
    parser.add_argument('-n',
                        dest='num_confs',
                        required=False,
                        metavar='<int>',
                        type=int,
                        default=10,
                        help='Number of conformers to generate (default: 10)')
    
    return parser.parse_args()


if __name__ == '__main__':
    main()