from PIL import Image
import os,glob
from torchvision import transforms



def get_data(dataset): # add model here 
    print("Hi")
    if dataset == 1: 
        # the rainforest dataset 
        pass
        #TODO add the dataset path 
    elif dataset == 2: 
        # the other dataset 
        #TODO add the dataset path 
        pass 
    elif dataset == 3: 
        # the series dataset 
        folder_path = '/Users/julia/Desktop/Makeathon/TUM.ai_Makeathon/data/silver_layer'
        for folder in glob.glob(os.path.join(folder_path, '*')):
            for file in glob.glob(os.path.join(os.path.join(folder_path, folder),'*.tif')):
                im = Image.open(file)
                pil_to_tensor = transforms.ToTensor()(im).unsqueeze_(0)
                #output = model(pil_to_tensor) 
                print(pil_to_tensor.size())
    else: 
        raise ValueError # value is supposed to be between 1 and 3 

def preprocess(data): 
    # resizing or normalization 
    pass



def get_clear_data():
    pass

get_data(3)