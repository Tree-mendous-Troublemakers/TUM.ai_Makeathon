# train model, setting everything up on its own 

import torch
import torch.nn as nn 
import torch.nn.functional as F
import numpy as np




class MyModel(nn.Module):
    # input layer: x 
    # n hidden layer : y 
    # output: 1
    

    def __init__(self):#, in_features= 192 , out_features = 1): #12288 input features? 3*64*64 
        super(MyModel, self).__init__()
        # Define the layers of the neural network
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=48, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(in_channels=48, out_channels=96, kernel_size=3, padding=1)
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
        self.fc1 = nn.Linear(96 * 48 * 16, 128)  # Calculated based on input size after pooling
        self.fc2 = nn.Linear(128, 1)  # Output layer with one node

    def forward(self, x):
        # Define the forward pass
        x = self.pool(torch.relu(self.conv1(x)))
        x = self.pool(torch.relu(self.conv2(x)))
        x = torch.flatten(x, 1)  # Flatten the feature maps
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x


    

    def init_params(m):
        if type(m)==nn.Linear or type(m)==nn.Conv2d:
            m.weight.data=torch.randn(m.weight.size())*.01#Random weight initialisation
            m.bias.data=torch.zeros(m.bias.size())


#model = Model()

# Input to the model
x = torch.randn([1, 3, 64, 64]) # dimensions of the input 

#torch_out = model(x) # output of the model when given input x 
#print(torch_out)



