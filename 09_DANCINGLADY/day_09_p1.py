import pandas as pd
import numpy as np

df = pd.read_csv("09_DANCINGLADY/d09_input.txt", header=None)
data = df.to_numpy()

def A(xy1, xy2):
    x = abs(xy2[0]-xy1[0]+1)
    y = abs(xy2[1]-xy1[1]+1)
    return x*y

areas = np.zeros([data.shape[0],data.shape[0]])
arealist = list()
for rt1 in range(data.shape[0]):
    for rt2 in range(data.shape[0]):
        if rt1 != rt2:
            area = A(data[rt1],data[rt2])
            areas[rt1,rt2] = area
            areas[rt1,rt2] = area
            arealist.append(area)

print(max(arealist))