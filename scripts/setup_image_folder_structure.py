import os
import shutil
import numpy as np

train = os.path.join("..", "images", "train")
valid = os.path.join("..", "images", "valid")
test = os.path.join("..", "images", "test")

# transfer from train to test 80-20
train_dir = os.listdir(train)
for idx in train_dir:
    num_transfers = np.ceil(len(os.listdir(os.path.join(train, idx)))*0.2).astype("int")
    files_to_transfer = np.random.choice(os.listdir(os.path.join(train, idx)), num_transfers, replace=False)
    for file in files_to_transfer:
        shutil.move(os.path.join(train, idx, file), os.path.join(test, idx))

# transfer from train to valid 80-20
train_dir = os.listdir(train)
for idx in train_dir:
    num_transfers = np.ceil(len(os.listdir(os.path.join(train, idx)))*0.2).astype("int")
    files_to_transfer = np.random.choice(os.listdir(os.path.join(train, idx)), num_transfers, replace=False)
    for file in files_to_transfer:
        shutil.move(os.path.join(train, idx, file), os.path.join(valid, idx))

# revert folder image structure
# change source and dest(ination)
# revert = os.listdir(source)
# for idx in revert:
#     files = os.listdir(os.path.join(source, idx))
#     for file in files:
#         shutil.move(os.path.join(source, idx, file), os.path.join(dest, idx, file))
