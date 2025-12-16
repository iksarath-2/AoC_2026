import pandas as pd
import numpy as np

df = pd.read_csv("09_DANCINGLADY/d09_input_TEST.txt", header=None)
data = df.to_numpy()

def A(xy1, xy2):
    x = abs(xy2[0]-xy1[0]+1)
    y = abs(xy2[1]-xy1[1]+1)
    return x*y

xvals = list()
yvals = list()
for i in range(data.shape[0]):
    xvals.append(data[i][0])
    yvals.append(data[i][1])

print(f"xmax = {max(xvals)}, xmin = {min(xvals)}")
print(f"ymax = {max(yvals)}, ymin = {min(yvals)}")

paper = np.empty([max(yvals)+2, max(xvals)+3],dtype=str)
paper.fill('.')

for rt1 in range(data.shape[0]):
    for rt2 in range(data.shape[0]):
        if rt1 != rt2:
            if data[rt1][0] == data[rt2][0]:
                paper[data[rt1][1]:data[rt2][1]+1,data[rt1][0]] = 'X'
            elif data[rt1][1] == data[rt2][1]:
                paper[data[rt1][1],data[rt1][0]:data[rt2][0]+1] = 'X'
    print(f"{rt1+1} out of {data.shape[0]}")

for j in range(paper.shape[0]):
    firstx = -1
    lastx = -1
    for i in range(paper.shape[1]):
        if paper[j,i] == 'X' and firstx == -1:
            firstx = i
        if paper[j,i] == 'X':
            lastx = i
    paper[j,firstx:lastx+1] = 'X'
    print(f"{j+1} out of {paper.shape[0]}")

for i in range(data.shape[0]):
    paper[data[i][1]][data[i][0]] = '#'

np.savetxt("09_DANCINGLADY/d09_p2_TEST.txt",paper,fmt='%s')

## takes far too long for the actual input...