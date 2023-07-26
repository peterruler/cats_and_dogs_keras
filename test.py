import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import os
from os import listdir
import random
from tensorflow.keras.models import model_from_json

# Load train and test data
test_dir = './catdog/test'

image_size = (180, 180)

fig, axes = plt.subplots(2, 5, figsize=(20, 12), facecolor='w')

# load json and create model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)

# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")

for ax in axes.ravel():
    
    files = listdir(test_dir)
    i = random.choice(files)
        
    img_path = os.path.join(test_dir, '{}'.format(i))
    
    img = keras.utils.load_img(
    img_path, target_size=image_size)

    img_array = keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # Create batch axis



    predictions = loaded_model.predict(img_array)
    score = float(predictions[0])

    if 100 * score > 50 :
        label = 'dog'
    else :
        label = 'cat'
    ax.set_title(label)
    ax.imshow(img)
plt.axis('off')
plt.show()