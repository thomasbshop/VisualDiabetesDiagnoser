# from rest_framework.parsers import FileUploadParser
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import FileSerializer


# def output_result():
# 	model = load_model('retina/full_retina_model.h5')

# 	# model.compile(loss='binary_crossentropy',
# 	#               optimizer='rmsprop',
# 	#               metrics=['accuracy'])

# 	img = cv2.imread('media/test.jpg')

# 	# img = cv2.resize(img,(320,240))
# 	# img = np.reshape(img,[1,320,240,3])

# 	classes = model.predict_classes(img)

# 	print (classes)
# 	return classes


class FileUploadView(APIView):
    # parser_class = (FileUploadParser,)
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):

      file_serializer = FileSerializer(data=request.data)
      result_serializer = FileSerializer(data=request.data)

      if file_serializer.is_valid():
          file_serializer.save()
          return Response(result_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# def output_model():
# 	with h5py.File('random.hdf5', 'r') as f:
# 		data = f['default']

