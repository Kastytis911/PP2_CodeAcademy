from src import slicing as sl
from src import get_image as img
from src import save_sliced_image as save

# Getting image from img directory
get_img = img.image_from_directory()

# Slice image in vertical slices
img_vertical_sliced = sl.vertical_slicing(get_img)

# Slice image in horizontal slices
img_horizontal_sliced = sl.horizontal_slicing(img_vertical_sliced)

# After all slicing, save image in '\img\Shredded_images' directory
save.save_image(img_horizontal_sliced)


