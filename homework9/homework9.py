
import tensorflow as tf
from tensorflow import keras
import tensorflow.lite as tflite
from io import BytesIO
from urllib import request
from PIL import Image
import numpy as np



#_____load and save model_______
model = keras.models.load_model('hw_model.h5')
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()
with open('clothing-model.tflite', 'wb') as f_out:
    f_out.write(tflite_model)


#_____input and output indexes_____
interpreter = tflite.Interpreter(model_path='clothing-model.tflite')
interpreter.allocate_tensors()
input_index = interpreter.get_input_details()[0]['index']
output_index = interpreter.get_output_details()[0]['index']



#____prepare image______
def download_image(url):
    with request.urlopen(url) as resp:
        buffer = resp.read()
    stream = BytesIO(buffer)
    img = Image.open(stream)
    return img
def prepare_image(img, target_size):
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img = img.resize(target_size, Image.NEAREST)
    return img
def prepare_input(x):
  return x * (1. /255)




#_____predict_____
url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Smaug_par_David_Demaret.jpg/1280px-Smaug_par_David_Demaret.jpg'

def predict(url):
    img = download_image(url)
    img = prepare_image(img, target_size=(150, 150))
    x = np.array(img, dtype='float32')
    X = np.array([x])
    X = prepare_input(X)

    interpreter.set_tensor(input_index, X)
    interpreter.invoke()
    preds = interpreter.get_tensor(output_index)
    return float(preds[0,0])



