#from preprocess_data.py import get_clear_data
from model import *
from BlobUtils import BlobHandler
import random, os 
from PIL import Image
import os,glob
from torchvision import transforms
import torchvision.datasets as datasets
import cv2


# hyperparameters 
number_epochs = 1
batch_size = 16 


#data = get_clear_data()
#blob_handler = BlobHandler()
#blob_handler.download_blob_folder(target_path="data/bronze_layer") # dataset in cloud is wrong


def get_len(folder_num): 
    folder_path = 'data/bronze_layer'
    if os.path.exists(os.path.join(folder_path, str(folder_num))):
        folder_to_extract = os.path.join(folder_path, str(folder_num))
        return len(os.listdir(os.path.join(folder_path, str(folder_num))))
    else:
        print("Folder not found in get_len. ", folder_num)

def get_ith_file(number, path):
    tmp = 0
    files = glob.glob(os.path.join(path,'*'))
    for file in files:
        if tmp == number: 
            return file 
        else: 
            tmp = tmp + 1 
    
    print("That's an error. ")

# everything together 
def __main__(model, epochs = number_epochs): 
    for epoch in range(number_epochs): 
        loss = 0
        training_data = get_elements()
        for element in training_data: 
            label = element[0]
            print(element[1].size())
            pred = model(element[1])
            loss = loss + (label-pred)
        #prediction = model(training_data) # forward pass (prediction seems to be a vector)

        loss = (prediction - labels).sum() # do we just take the difference, taking it in each step 
        loss.backward() # backward pass

        optim = torch.optim.SGD(model.parameters(), lr=1e-2, momentum=0.9)
        optim.step() # update all weights 



def get_elements(batch_size = batch_size):
    training_data = []
    folder_path = 'data/bronze_layer'
    length = [get_len(folder) for folder in range(0,10) ]
    #print("Length: ", length)
    for tuple in range(batch_size): 
        # len(glob.glob('*')) # alternativ 
        label = random.randint(0, 9) # which label is it? 

        if os.path.exists(os.path.join(folder_path, str(label))):
            folder_to_extract = os.path.join(folder_path, str(label))
            #print("Folder found:", folder_to_extract) 
            example = random.randint(0, length[label])
            file = get_ith_file(example, folder_to_extract)
            try: 
                #im = Image.open(file) not using image anymore 
                # im = cv2.imread('test.tif', cv2.IMREAD_UNCHANGED) für tif dateien 
                im = Image.open(file)
                pil_to_tensor = transforms.ToTensor()(im).unsqueeze_(0)
                training_data.append((label, pil_to_tensor))
            except Exception: 
                print("Problem. ")
                tuple = tuple - 1 
            
        else:
            print("Folder not found.")
    
    return training_data



my_model = MyModel()
__main__(my_model)
#print(data)

PATH = 'my_model.pth' # oder Endung .pt 
# torch.save(net.state_dict(), PATH)


# Save
#torch.save(my_model, PATH)








