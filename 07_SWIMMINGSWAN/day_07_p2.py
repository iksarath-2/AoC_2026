import pandas as pd
import numpy as np

df = pd.read_csv("07_SWIMMINGSWAN/d07_input.txt", header=None)
data = df.to_numpy()

leny = data.size
lenx = len(list(str(data[0]).strip("[']")))
datarr = np.empty([leny,lenx],dtype=int)

for i in range(lenx):
    for j in range(leny):
        if list(str(data[j]).strip("[']"))[i] == '.':
            datarr[j][i] = 0
        else:
            datarr[j][i] = -1

for i in range(lenx):
    if datarr[0][i] == -1:
        datarr[1][i] = 1
                
tl_count = 0
for j in range(2,leny):
    for i in range(lenx):
        if datarr[j-1][i] >= 0:
            if datarr[j][i] == -1:
                datarr[j][i-1] = datarr[j][i-1]+datarr[j-1][i]
                datarr[j][i+1] = datarr[j][i+1]+datarr[j-1][i]
            else:
                datarr[j][i] = datarr[j][i]+datarr[j-1][i]
                
for i in range(lenx):
    tl_count += datarr[leny-1][i]  
               
np.savetxt("07_SWIMMINGSWAN/d07_beams_p2.txt",datarr,fmt='%s')
print(tl_count)