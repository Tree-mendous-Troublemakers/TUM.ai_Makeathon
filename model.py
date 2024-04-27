# train model, setting everything up on its own 

import torch
import torch.nn as nn 
import torch.nn.functional as F
import numpy as np




class Model(nn.Module):
    # input layer: x 
    # n hidden layer : y 
    # output: 1
    

    def __init__(self, in_feat=3, hidden = , out_feat=1):
        super().__init__()
        self.layer1 = nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, padding=1, stride = 1)
        self.layer2 = nn.MaxPool2d(kernel_size=2, stride=2)
        self.layer3 = nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, padding=1, stride = 1)
        self.layer4 = nn.MaxPool2d(kernel_size=2, stride=2)
        self.layer5 = nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3, padding=1, stride = 1 )
        self.layer6 = nn.MaxPool2d(kernel_size=2, stride=2)
        self.layer7 = nn.Flatten()
        self.layer8 = nn.Linear(60675328, 256)
        self.layer9 = nn.Linear(256, 1)


        self.apply(init_params) # does that work??

    def forward(self, x): # x is the data received and it describes what is done with it 
        #x = F.Relu6(self.fc1(x))
        #x = self.layer1(x) # erstmal ohne Aktivierungsfnkt 
        # x = self.layer2(x)
        x = nn.functional.relu(self.layer1(x))
        x = self.layer2(x)
        x = nn.functional.relu(self.layer3(x))
        x = self.layer4(x)
        x = nn.functional.relu(self.layer5(x))
        x = self.layer6(x)
        x = self.layer7(x)
        x = nn.functional.relu(self.layer8(x))
        x = nn.functional.logsigmoid(self.layer9(x))

        return x
    
    
        

    def weights_setting(self):

        # do it randomly 

    def init_params(m):
        if type(m)==nn.Linear or type(m)==nn.Conv2d:
            m.weight.data=torch.randn(m.weight.size())*.01#Random weight initialisation
            m.bias.data=torch.zeros(m.bias.size())




            
        
    


model = Model()
        

#print("Model's state_dict:")
for param_tensor in model.state_dict():
    pass
    #print(param_tensor, "\t", model.state_dict()[param_tensor].size(), "\t", model.state_dict()[param_tensor])





# Input to the model
x = torch.randn(1,3)
x[0,0] = 2
x[0,1] = 5.5

torch_out = model(x) # output of the model when given input x 

print(torch_out)



