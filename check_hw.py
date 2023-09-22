import os
from PIL import Image
from tqdm import tqdm

# images path
folder_path = 'images'

# get all images
for filename in tqdm(os.listdir(folder_path)):
    # get full path of image
    file_path = os.path.join(folder_path, filename)
    
    # open image
    image = Image.open(file_path)
    
    # get the height&width of image
    width, height = image.size
    if width != 1920 or height != 1080:
        print(filename)
