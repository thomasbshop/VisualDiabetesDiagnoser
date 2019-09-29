import os
from keras.models import load_model
from keras.preprocessing.image import load_img, img_to_array, array_to_img
import numpy as np
from .. import app

#load saved model file
basedir = app.config["BASEDIR"]
MODEL_FOLDER = os.path.join(basedir, 'ai_model/saved_models')
app.config['MODEL_FOLDER'] = MODEL_FOLDER
model_file_name = 'keras_model.h5'
model_path = os.path.join(app.config['MODEL_FOLDER'], model_file_name)
model = load_model(model_path)
model._make_predict_function()

def predict(image):
	# dimensions of our images
	img_width, img_height = 128, 128

	# load the image and convert the image size
	img = load_img(image, target_size=(img_width, img_height))

	# convert image to numpy array
	img_array = img_to_array(img)

	# add dimention to image attay
	img_array = np.expand_dims(img_array, axis=0)

	# do prediction
	classes = model.predict_classes(img_array)
	return classes



# dimensions of our images
# img_width, img_height = 128, 128

# load the image and convert the image size
# img = load_img('images/13_left.jpeg', target_size=(img_width, img_height))

# show the image
# img.show()

# convert image to numpy array
# img_array = img_to_array(img)


# # add dimention to image attay
# img_array = np.expand_dims(img_array, axis=0)

# # do prediction
# classes = model.predict_classes(img_array)

# # report details about the image
# print(type(img))
# print(img.format)
# print(img.mode)
# print(img.size)

# #Report detals abour array
# print(img_array.dtype)
# print(img_array.shape)

# # print result eg [1] 
# # This is the meaning of the results : 0 - No DR, 1 - Mild, 2 - Moderate, 3 - Severe, 4 - Proliferative DR
# print (classes)


