import pandas as pd
import numpy as np

df = pd.read_csv("05_GOLDRING/d05_input.txt", header=None)
data = df.to_numpy()

ids = np.astype(data[190:len(data)],int)

rs_temp = data[0:190]
rs = np.empty([190,2],dtype=int)
for r in range(190):
    [rs[r,0], rs[r,1]] = str(rs_temp[r]).strip("[']").split('-')

## part 1
count = 0
for id in ids:
    counted = False
    for r in rs:
        if r[0] <= id and r[1] >= id and not counted:
            count += 1
            counted = True
# print(count)

## part 2

# first we need to order the id rs by starting id:
sorted_rs = np.sort(rs, 0)
print(sorted_rs.size)

# If the 2nd ID of the current r is >= the 1st ID of the next r
# then update the 2nd ID of the current r to the first ID of the previous -1
for i in range(len(sorted_rs)-1):
    if sorted_rs[i][1] >= sorted_rs[i+1][0]:
        sorted_rs[i][1] = sorted_rs[i+1][0]-1

sum = 0
for r in sorted_rs:
    sum += r[1]-r[0]+1
    
print(sum)
        