import os
import csv
import numpy as np
from sklearn.preprocessing import RobustScaler
import joblib
from tqdm import tqdm

root = os.path.dirname(os.path.abspath(__file__))

CHECKPOINTS_DIR = os.path.join(root, "..", "..", "checkpoints")

def file2array(file_name):
    with open(os.path.join(CHECKPOINTS_DIR, file_name), "r") as f:
        reader = csv.reader(f)
        h = next(reader)
        R = []
        for r in tqdm(reader):
            R += [r]
    return np.array(R), h


def scale(file_name):
    print(file_name)
    X, h = file2array(file_name)
    scaler = RobustScaler()
    scaler.fit(X)
    Xt = scaler.transform(X)
    prefix = file_name.split(".")[0]
    scaler_file = os.path.join(CHECKPOINTS_DIR, prefix+".joblib")
    scaled_file = os.path.join(CHECKPOINTS_DIR, prefix+"_scaled.csv")
    joblib.dump(scaler, scaler_file)
    with open(scaled_file, "w") as f:
        writer = csv.writer(f)
        writer.writerow(h)
        for i in tqdm(range(Xt.shape[0])):
            writer.writerow(list(Xt[i,:]))
        

scale("R0.csv")
scale("R1.csv")
scale("R2.csv")