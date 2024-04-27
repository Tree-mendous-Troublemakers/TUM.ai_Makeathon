from libtiff import TIFF # an alternative 


#im = Image.open('test.tif')
#im.show()



tif = TIFF.open('test.tif') # open tiff file in read mode
# read an image in the current TIFF directory as a numpy array
image = tif.read_image()

# read all images in a TIFF file:
for image in tif.iter_images(): 
    print("Hi")
    pass

tif = TIFF.open('test.tif', mode='w')
tif.write_image(image)




def get_data():
    pass

def preprocess(data): 
    # resizing or normalization 
    pass



def get_clear_data():
    pass