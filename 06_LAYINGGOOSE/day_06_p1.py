import pandas as pd
import numpy as np

df = pd.read_csv("06_LAYINGGOOSE/d06_input.txt", header=None,)
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
col_is.append(len(operations))

sum_ops = 0
for j in range(len(col_is)-1):
    i = col_is[j]
    i_next = col_is[j+1]
    val1 = ''
    val2 = ''
    val3 = ''
    val4 = ''
    for n in range(i_next-i):
        if row1[i+n] != ' ':
            val1 += str(row1[i+n])
        if row2[i+n] != ' ':
            val2 += str(row2[i+n])
        if row3[i+n] != ' ':
            val3 += str(row3[i+n])
        if row4[i+n] != ' ':
            val4 += str(row4[i+n])
    if operations[i] == '+':
        sum_ops += (int(val1)+int(val2)+int(val3)+int(val4))
    elif operations[i] == '*':
        sum_ops += (int(val1)*int(val2)*int(val3)*int(val4))
        
print(sum_ops)
    