import pandas as pd
import numpy as np

df = pd.read_csv("04_COLLYBIRD/d04_input.txt", header=None)
data = df.to_numpy()
shelves = np.empty([137,137],dtype=str)
shelves.fill('.')

for row in range(135):
    shelf = list(str(data[row]).strip("[']"))
    for col in range(135):
        shelves[col+1,row+1] = str(shelf[col])
possible = True
collect = 0
while(possible):
    rolls = shelves
    possible = False
    for row in range(135):
        for col in range(135):
            if shelves[col+1,row+1] == '@':
                count = 0
                col += 1
                row += 1
                adjacents = [shelves[col-1,row-1], shelves[col-1,row],
                            shelves[col-1,row+1], shelves[col,row-1],
                            shelves[col,row+1], shelves[col+1,row-1],
                            shelves[col+1,row], shelves[col+1,row+1]]
                col -= 1
                row -= 1
                for roll in adjacents:
                    if str(roll) == '@':
                        count += 1
                if count < 4:
                    collect += 1
                    rolls[col+1,row+1] = '.'
                    possible = True                    
                    
print(collect)