import numpy as np
from PIL import Image


def image_from_directory():

    # Loading image as a NumPy array
    img_array = np.array(Image.open(".\img\dog.jpg"))

    return img_array
