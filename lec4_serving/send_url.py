import json
import base64
from PIL import Image
import numpy as np
import io
import matplotlib.pyplot as plt
import tensorflow as tf



# Image to binary
img_path = "/Users/seongjungkim/PycharmProjects/network_study/lec4_serving/sample.png"
f = open(img_path, mode='rb')
image = f.read()
b_image = base64.encodebytes(image).decode("utf-8")
data = {'image': b_image}
j_image = json.dumps(data)


# binary to Image
raw_image = base64.b64decode(b_image)
img = Image.open(io.BytesIO(raw_image))

#
data = json.dumps({"signature_name": "serving_default", "instances": b_image})
print('Data: {} ... {}'.format(data[:50], data[len(data)-52:]))


