import pandas as pd
import numpy as np
import math

df = pd.read_csv("06_GOOSEALAYING/d06_input.txt", header=None,)
data = df.to_numpy()

col_is = list()
row1 = list(str(data[0]).strip("[']"))
row2 = list(str(data[1]).strip("[']"))
row3 = list(str(data[2]).strip("[']"))
row4 = list(str(data[3]).strip("[']"))
operations = list(str(data[4]).strip("[']"))
for i in range(len(operations)):
    if operations[i] == '+' or operations[i] == '*':
        col_is.append(i)
col_is.append(len(operations)+1)

sum_ops = 0
for j in range(len(col_is)-1):
    i = col_is[j]
    i_next = col_is[j+1]
    vals = list()
    for n in range(i_next-i-1):
        vals.append(int((str(row1[i+n])+str(row2[i+n])+str(row3[i+n])+str(row4[i+n])).strip(" ")))
    if operations[i] == '+':
        sum_ops += sum(vals)
    elif operations[i] == '*':
        sum_ops += math.prod(vals)
        
print(sum_ops)
    