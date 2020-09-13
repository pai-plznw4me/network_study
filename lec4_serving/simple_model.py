import tensorflow as tf
from tensorflow.keras.layers import Input
from tensorflow.keras.models import Model
import base64
import numpy as np

f = open('sample.png', 'rb')
image = f.read()
b_image = base64.encodebytes(image).decode('utf-8')
print(b_image[0])


input = Input(, dtype=tf.string)
contents = tf.io.read_file(input)
image = tf.image.decode_jpeg(contents, channels=1)

# image_b_64 = tf.io.decode_base64(input_b_64)
# # img = tf.image.decode_jpeg(image_b_64[0], channels=3)
# # img = tf.image.resize(img, (100, 100))

model = Model(input_b_64, image_b_64)
model.predict()
