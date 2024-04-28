""" # from init function 
        super().__init__()
        # self.layer0 = nn.Linear(in_feat, in_feat) # just a linear layer to specify number of inputs  
        self.layer1 = nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, padding=1, stride = 1)
        self.layer2 = nn.MaxPool2d(kernel_size=2, stride=2)
        self.layer3 = nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, padding=1, stride = 1)
        self.layer4 = nn.MaxPool2d(kernel_size=2, stride=2)
        self.layer5 = nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3, padding=1, stride = 1 )
        self.layer6 = nn.MaxPool2d(kernel_size=2, stride=2)
        self.layer7 = nn.Flatten()
        self.layer8 = nn.Linear(60675328, 256)
        self.layer9 = nn.Linear(256, out_feat)
        """



# layers in init 
self.layer1 = nn.Conv2d(in_channels=3, out_channels=16, kernel_size=3, padding=0, stride=1)
self.layer2 = nn.MaxPool2d(kernel_size=2, stride=2)
self.layer3 = nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3, padding=1, stride=1)
self.layer4 = nn.MaxPool2d(kernel_size=2, stride=2)
self.layer5 = nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, padding=0, stride=1)
self.layer6 = nn.MaxPool2d(kernel_size=2, stride=2)
self.layer7 = nn.Flatten()
self.layer8 = nn.Linear(4096, 128)  # Calculate the input size based on the output size of layer6
self.layer9 = nn.Linear(128, out_feat)
#corresponding forward method 
x = nn.functional.relu(self.layer1(x))
x = self.layer2(x)
x = nn.functional.relu(self.layer3(x))
x = self.layer4(x)
x = nn.functional.relu(self.layer5(x))
x = self.layer6(x)
x = self.layer7(x)
x = nn.functional.relu(self.layer8(x))
x = self.layer9(x)


