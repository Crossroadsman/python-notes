# imports for Pillow still use PIL as the import name
from PIL import Image


# Pillow lazy-loads the file so this operation is fast
image_file = Image.open("img/IMG_1.jpg")

# These details can be obtained just by looking at the file header so these
# operations are fast and not filesize dependent
print(image_file.format)  # JPEG
print(image_file.size)  # (3003, 3003) x then y
print(image_file.mode)  # RGB

# Creates a temporary file and loads it in the default image editor
image_file.show()

# rotate(d) rotates the file counter-clockwise by the specified amount in
# degrees
# optional args:
# - resample : (default=Image.NEAREST) the resampling filter to use
# - expand : (default=False) expand the image box to contain the whole image
#            after rotation. Otherwise crops the image to preserve the original
#            image dimensions.
rotate_image = Image.open("img/IMG_2.jpg")
rotated = rotate_image.rotate(45)
rotated.show()
rotated_expand = rotate_image.rotate(45, 
                                     resample=Image.BICUBIC,
                                     expand=True)
rotated_expand.show()

# Mode conversion
# ===============
# the following are some of the most common modes:
# 1 : 1-bit pixels
# L : 8-bit black and white
# P : 8-bit using a palette
# RGB : 24-bit
# RGBA : 32-bit (24-bit plus 8-bit transparency mask)
# CMYK
# YCbCr
# LAB
# HSV
bw = image_file.convert(mode='1')
bw.show()

bw = image_file.convert(mode='L')
bw.show()

# Resizing
# ========
# parameters:
# - size : 2-tuple ints width, height in px for output
# - resample (optional) : the filter to use. Default is nearest-neighbour
#   - PIL.Image.NEAREST (default) : nearest-neighbour. Worst quality, best
#                                   performance
#   - PIL.Image.BICUBIC : Bicupic filter. Best quality filter available for
#                         geometry transforms other than resize/thumbnail
#   - PIL.Image.LANCZOS : Lanczos filter. Best quality, worst performance
# - box (optional) : 4-tuple describing the co-ordinates of the image to resize
small = image_file.resize((256, 256))
small.show()
large = image_file.resize((4000,1000))
large.show()

small_input = Image.open("img/IMG_3.jpg")
downsized = small_input.resize((256,256), Image.LANCZOS)
downsized.show()
x_multiplier = 8
y_multiplier = 8
up_bad = downsized.resize(
    (downsized.width * x_multiplier, downsized.height * y_multiplier),
    Image.NEAREST
)
up_bad.show()
up_good = downsized.resize(
    (downsized.width * x_multiplier, downsized.height * y_multiplier),
    Image.LANCZOS
)
up_good.show()

# Thumbnail
# like resize except modifies in-place rather than returning a new instance
# note that the size arguments describe the maximum value in that direction,
# preserving aspect ratio
small_input_copy = small_input.copy()
small_input_copy.thumbnail((256, 256))
small_input_copy.show()

# Crop
# the box is in the form (x0, y0, x1, y1)
box = (500, 1100, 900, 1700)   # look for jQuery widget that gets a box
cropping_image = Image.open("img/IMG_4.jpg")
cropping_image.show()
cropped_image = cropping_image.crop(box)
cropped_image.show()

re_up_multiplier = 3
cropped_image.resize(
    (cropped_image.width*re_up_multiplier, cropped_image.height*re_up_multiplier),
    Image.LANCZOS
).show()

# Saving
to_save_file = Image.open("img/IMG_5.jpg")
box = (1250, 800, 3850, 2020)
transformed = to_save_file.crop(box)
scale_factor = 1800/1220
transformed = transformed.resize(
    (int(transformed.width * scale_factor), int(transformed.height * scale_factor)),
    Image.LANCZOS
)
transformed.save("img/transformed.jpg")


# See also the fourth video in the Treehouse Image Manipulation with Python
# workshop for examples of using ImageEnhance (brightness, desaturation etc)
# and ImageFilter (sharpen, gaussian blur, etc)
# https://teamtreehouse.com/library/enhance-and-filter
