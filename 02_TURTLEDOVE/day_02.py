import pandas as pd

df = pd.read_csv("02_TURTLEDOVE/d02_input.txt", header=None, delimiter=',')
data = df.to_numpy()
id_sum = 0

for id_pair in data[0]:
    [first_id, last_id] = id_pair.split('-')
    id = first_id
    while int(id) <= int(last_id):
        added = False
        for n in range(1, len(id)):
            if len(id)%n == 0 and not added:
                allowed = all([id[0:n] == id[x:x+n] for x in range(0,len(id),n)])
                if allowed:
                    id_sum += int(id)
                    added = True
        id = str(int(id)+1)
        
print(id_sum)