from django.db import models

import h5py
from keras.models import load_model
import cv2
import numpy as np
# from .models import File

def output_result():
	model = load_model('media/full_retina_model.h5')

	# model.compile(loss='binary_crossentropy',
	#               optimizer='rmsprop',
	#               metrics=['accuracy'])

	img = cv2.imread('media/test.jpg')

	# img = cv2.resize(img,(320,240))
	# img = np.reshape(img,[1,320,240,3])

	classes = model.predict_classes(img)

	print (classes)
	return classes

class File(models.Model):
	file = models.FileField(blank=False, null=False)
	name = models.CharField(max_length=20, default='filename')
	timestamp = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.file.name


class Result(models.Model):
	def __init__(self, result_details=output_result()):
		self.result_details = result_details

result = Result(result_details=result_details)