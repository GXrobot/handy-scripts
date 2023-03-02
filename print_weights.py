# python3
# Print Model Weights to File

import torch
import sys
import numpy as np
import tqdm

np.set_printoptions(precision=7)
np.set_printoptions(suppress=True)  # no scientific Notation
#np.set_printoptions(threshold=sys.maxsize) # no truncation

original_stdout = sys.stdout

path = "swin_tiny_patch4_window7_224.pth"

model = torch.load(path)

#print("model_dir: ", model.__dir__())

with open(path + '_weights', 'w') as f:
    sys.stdout = f
    
    for key, value in model.items():
        print(key)
        for k, v in tqdm.tqdm(value.items()):
            print(k, v.size())
            val = v.detach().cpu().numpy()
            print(val)
    sys.stdout = original_stdout 
