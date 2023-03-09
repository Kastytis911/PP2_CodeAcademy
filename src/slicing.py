import numpy as np
from PIL import Image


def vertical_slicing(img_array):

    # Split into slices
    number_of_slices = np.split(img_array, 20, axis=1)

    image1_slices = number_of_slices[1::2]

    image1_array = np.concatenate(image1_slices, axis=1)

    image2_slices = np.delete(number_of_slices, np.s_[1::2], axis=0)

    image2_array = np.concatenate(image2_slices, axis=1)

    # Concatenate two images arrays
    combined_array = np.concatenate((image1_array, image2_array), axis=1)

    return combined_array


def horizontal_slicing(img_array):

    # Split into slices
    number_of_slices = np.split(img_array, 20, axis=0)

    image3_slices = number_of_slices[1::2]

    image3_array = np.concatenate(image3_slices, axis=0)

    image4_slices = np.delete(number_of_slices, np.s_[1::2], axis=0)

    image4_array = np.concatenate(image4_slices, axis=0)

    # Concatenate two images arrays
    combined_array = np.concatenate((image3_array, image4_array), axis=1)

    combined_image = Image.fromarray(combined_array)

    return combined_image
