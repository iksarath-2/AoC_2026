import pandas as pd
import numpy as np

df = pd.read_csv("03_FRENCHHEN/d03_input.txt", header=None)
data = df.to_numpy()

bjsum = 0
for row in data:
    bank = list(str(row).strip("[']"))
    joltage = np.array([],dtype=int)
    for battery in bank:
        joltage = np.append(joltage, int(battery))
    bjstr = ""
    prev = 0
    for i in range(12,0,-1):
        prev = max(joltage[0:len(joltage)-i+1])
        bjstr = bjstr + str(prev)
        found = False
        for batteri in range(len(joltage)):
            if not found and joltage[batteri] == prev:
                joltage = joltage[batteri+1:len(joltage)]
                found = True
    bjsum += int(bjstr)
print(bjsum)