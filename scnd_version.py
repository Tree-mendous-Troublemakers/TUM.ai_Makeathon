import os
import glob
import random
from PIL import Image
import torch
from torchvision import transforms
from model import Model

# Hyperparameters
number_epochs = 3
batch_size = 16

# Define a function to get the length of a folder
def get_len(folder_num):
    folder_path = 'data/bronze_layer'
    if os.path.exists(os.path.join(folder_path, str(folder_num))):
        return len(os.listdir(os.path.join(folder_path, str(folder_num))))
    else:
        print("Folder not found in get_len:", folder_num)
        return 0

# Define a function to get the path of the i-th file in a folder
def get_ith_file(number, path):
    files = glob.glob(os.path.join(path, '*'))
    if number < len(files):
        return files[number]
    else:
        print("Index out of range in get_ith_file:", number)
        return None

# Define a function to load image data on-the-fly
def get_elements(batch_size=batch_size):
    training_data = []
    folder_path = 'data/bronze_layer'
    length = [get_len(folder) for folder in range(10)]
    for _ in range(batch_size):
        label = random.randint(0, 9)
        length_label = length[label]
        if length_label == 0:
            continue  # Skip if the folder is empty
        example = random.randint(0, length_label - 1)
        file = get_ith_file(example, os.path.join(folder_path, str(label)))
        if file is not None:
            try:
                im = Image.open(file)
                pil_to_tensor = transforms.ToTensor()(im).unsqueeze_(0)
                training_data.append((label, pil_to_tensor))
            except Exception as e:
                print("Error loading image:", e)
    return training_data

# Define the main training loop
def train_model(model):
    for epoch in range(number_epochs):
        training_data = get_elements()
        for data, labels in training_data:
            # Forward pass
            prediction = model(data)
            # Compute loss
            loss = (prediction - labels).sum()
            # Backward pass
            loss.backward()
            # Update weights
            optimizer = torch.optim.SGD(model.parameters(), lr=1e-2, momentum=0.9)
            optimizer.step()

# Main function
def main():
    model = Model()
    train_model(model)

if __name__ == "__main__":
    main()
