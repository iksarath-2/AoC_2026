import pandas as pd
import numpy as np

df = pd.read_csv("07_SWIMMINGSWAN/d07_input.txt", header=None)
data = df.to_numpy()

leny = data.size
lenx = len(list(str(data[0]).strip("[']")))
datarr = np.empty([leny,lenx],dtype=str)

for i in range(lenx):
    for j in range(leny):
        datarr[j][i] = list(str(data[j]).strip("[']"))[i]

for i in range(lenx):
    if datarr[0][i] == 'S':
        datarr[1][i] = '|'
                
bs_count = 0
for j in range(2,leny):
    for i in range(lenx):
        if datarr[j-1][i] == '|':
            if datarr[j][i] == '.':
                datarr[j][i] = '|'
            if datarr[j][i] == '^':
                datarr[j][i-1] = '|'
                datarr[j][i+1] = '|'
                bs_count += 1     
               
np.savetxt("07_SWIMMINGSWAN/d07_beams_p1.txt",datarr,fmt='%s') 
print(bs_count)    