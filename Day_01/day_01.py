import pandas as pd

df = pd.read_csv("Day_01/d01_input.txt", header=None, index_col=None )
data = df.to_numpy()
current = 50
count = 0

for row in data:
    l = list(str(list(row)).strip("[']"))
    i = int(str(list(row)).strip("[']RL"))
    if l[0] == 'R':
        current = (current+i)%100
    else:
        current = (current-i)%100
    if current == 0:
        count += 1
    
print(count)