
import io
from PIL import Image
import logging
import Colorer
import numpy as np

logging.basicConfig(level=logging.DEBUG)
# Open image using the pillow package
img = Image.open("./images/nature-night-reflection_320x320.jpg")
img_rgb = img.convert('RGB')
img_rgb = np.asarray(img)
# img = Image.open("./images/Punk1094.png")
pix_val = list(img.getdata())
# img.tobytes("hex", "rgb")
# img.tobytes("xbm", "rgb")
logging.info(len(pix_val))
print(img_rgb)
# # initialiaze io to_bytes converter
# img_byte_arr = io.BytesIO()
# # define quality of saved array
# img.save(img_byte_arr, format='PNG', subsampling=0, quality=100)
# # converts image array to bytesarray
# img_byte_arr = img_byte_arr.getvalue()
# print(img_byte_arr)

# with open("./images/Punk1094.png", "rb") as image:
#   f = image.read()
#   b = bytearray(f)
#   print(b[0])