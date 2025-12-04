import pandas as pd

df = pd.read_csv("02_TURTLEDOVE/d02_input.txt", header=None, delimiter=',')
data = df.to_numpy()
id_sum = 0

for id_pair in data[0]:
    [first_id, last_id] = id_pair.split('-')
    range = [*range(int(first_id),int(last_id)+1)]
    for id in range:
        if len(str(id))%2 == 0 and int(str(id)[0:len(str(id))//2]) == int(str(id)[(len(str(id))//2):len(str(id))]):
                id_sum += id
                
print(str(id_sum))