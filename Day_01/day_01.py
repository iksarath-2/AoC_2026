import pandas as pd

df = pd.read_csv("Day_01/d01_input.txt", header=None, index_col=None )
data = df.to_numpy()
current = 50
count_part_1 = 0
count_part_2 = 0

for row in data:
    l = list(str(list(row)).strip("[']"))
    i = int(str(list(row)).strip("[']RL"))
    if l[0] == 'R':
        count_part_2 += (current+i)//100
        current = (current+i)%100
    else:
        count_part_2 -= (current-i)//100
        current = (current-i)%100            
    if current == 0:
        count_part_1 += 1
    
print("Part 1 answer: " + str(count_part_1))
print("Part 2 answer: " + str(count_part_2))