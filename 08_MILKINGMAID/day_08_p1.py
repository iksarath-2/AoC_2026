import pandas as pd
import numpy as np

df = pd.read_csv("08_MILKINGMAID/d08_input.txt", header=None)
data = df.to_numpy()
print(data.shape)

def d(xyz1, xyz2):
    for i in range(3):
        s += (xyz1[i]-xyz2[i])**2
    dist = np.sqrt(s)
    return dist

# make a dictionary of junction box index with coordinates...