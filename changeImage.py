#convert images size and type

import os, sys
from PIL import Image

#Setting the locale images
user = os.getenv('USER') # To get the username from environment variable
image_directory = '/home/{}/supplier-data/images/'.format(user)

for image_name in os.listdir(image_directory):
    if image_name.endswith(".tiff"):
        image_path = image_directory + image_name
        path = os.path.splitext(image_path)[0]
        im = Image.open(image_path)
        new_path = '{}.jpeg'.format(path)
        im.convert('RGB').resize((600, 400)).save(new_path, "JPEG")
