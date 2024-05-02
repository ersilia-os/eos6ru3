import os
import csv
import numpy as np
import faiss
from faiss import write_index
from tqdm import tqdm

root = os.path.abspath(os.path.dirname(__file__))
CHECKPOINTS_DIR = os.path.join(root, "..", "..", "checkpoints")


def get_faiss_index(file_name):
    print(file_name)
    with open(os.path.join(CHECKPOINTS_DIR, file_name), "r") as f:
        reader = csv.reader(f)
        h = next(reader)
        size_of_vectors = len(h)
        index = faiss.IndexFlatL2(size_of_vectors)
        R = []
        for r in tqdm(reader):
            R += [r]
        X = np.array(R, dtype=np.float32)
        index.add(X)
    print("Index done")
    faiss_file = file_name.split(".")[0] + ".index"
    write_index(index, os.path.join(CHECKPOINTS_DIR, faiss_file))


get_faiss_index("R0_scaled.csv")
get_faiss_index("R1_scaled.csv")
get_faiss_index("R2_scaled.csv")