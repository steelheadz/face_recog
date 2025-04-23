import face_recognition
import numpy
from PIL import Image
from PIL.ImageDraw import ImageDraw

filepath = r'D:\Personal\Identification Photo\0254230335.jpg'

img_arr = face_recognition.load_image_file(filepath)
face_recognition.face_landmarks(img_arr)