import numpy as np # linear algebra
# import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os
import torch
import torchvision
import torch.nn as nn # All neural network modules, nn.Linear, nn.Conv2d, BatchNorm, Loss functions
import torchvision.datasets as datasets # Has standard datasets we can import in a nice way
import torchvision.transforms as transforms # Transformations we can perform on our dataset
import torch.nn.functional as F # All functions that don't have any parameters
from torch.utils.data import DataLoader, Dataset # Gives easier dataset managment and creates mini batches
from torchvision.datasets import ImageFolder
import torch.optim as optim # For all Optimization algorithms, SGD, Adam, etc.
from PIL import Image

from torchvision import models
# load pretrain model and modify...

device = torch.device("cpu") # use gpu or cpu

class CatDogModel():
    def __init__(self):
        criterion = nn.CrossEntropyLoss()
        self.model = models.resnet50(pretrained=True)
        for param in self.model.parameters():
            param.requires_grad = False

        num_ftrs = self.model.fc.in_features
        self.model.fc = nn.Linear(num_ftrs, 2)
        optimizer = optim.Adam(self.model.parameters(), lr=0.01)
        print("----> Loading checkpoint")
        checkpoint = torch.load("./checpoint_epoch_4.pt",  map_location=torch.device('cpu')) # Try to load last checkpoint
        self.model.load_state_dict(checkpoint["model_state_dict"]) 
        # print(checkpoint["model_state_dict"])
        optimizer.load_state_dict(checkpoint["optimizer_state_dict"])
        # return model
    def __call__(self, filepath):
        print(filepath)
        img_array = Image.open(filepath).convert("RGB")
        data_transforms=transforms.Compose([
            transforms.Resize((224, 224)), 
            transforms.ToTensor(), 
            transforms.Normalize([0.5]*3, [0.5]*3)
        ])
        img = data_transforms(img_array).unsqueeze(dim=0) # Returns a new tensor with a dimension of size one inserted at the specified position.
        load = DataLoader(img)
        
        for x in load:
            x=x.to(device)
            pred = self.model(x)
            _, preds = torch.max(pred, 1)
            print(f"class : {preds}")
            if preds[0] == 1: print(f"predicted ----> Dog")
            else: print(f"predicted ----> Cat")