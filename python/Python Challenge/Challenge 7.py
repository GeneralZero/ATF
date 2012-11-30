#http://www.pythonchallenge.com/
#Challenge 7
import re
from PIL import Image
def decrypt_image(image_file, text_file):
	if not os.path.exists(image_file): raise IOError('File does not exist: %s' % image_file)
	img = Image.open(image_file)
	with open(text_file, 'w') as txt:
		txt.write(img.tostring())
img = Image.open('..\Downloads\oxygen.png')
for lines in img.tostring():
	print lines
