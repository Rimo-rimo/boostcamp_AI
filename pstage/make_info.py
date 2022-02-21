import os
import pandas as pd
import copy

train_images = (list(os.listdir("train/images")))
result = copy.deepcopy(train_images)

for i in train_images:
    if i[0] == ".":
        result.remove(i)
infos = []
for path in result:
    path = path.split("_")
    gender = path[1]
    age = path[-1]
    info = {"gender" : gender, "age" : age}
    infos.append(info)
train_df = pd.DataFrame(infos)
train_df.to_csv("info.csv")
