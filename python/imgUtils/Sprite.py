import Image

def image_split(image_file, splits):
	size_x =  image_file.size[0]/splits[0]
	size_y = image_file.size[1]/splits[1]
	
	for x in xrange(0, splits[0]):
		for y in xrange(0, splits[1]):
			box = (size_x*x, size_y*y, size_x*(x+1), size_y*(y+1))
			temp_img = image_file.crop(box)
			temp_img.save("f0[%d][%d]." %(y ,x)+image_file.format, image_file.format) 
			
		
def image_crop(image_file):
	#print image_file.size[0]/splits[0]
	#print image_file.size[1]/splits[1]
	
	blank_lines = [0]*(image_file.size[1]+image_file.size[0])
	#blank_lines[12] =+ 5 
	
	print blank_lines
	
	for x in xrange(0, image_file.size[0]):
		for y in xrange(0, image_file.size[1]):
			blank_lines[x] =+ image_file.getpixel((x,y))[3] 
			blank_lines[image_file.size[0]+y] =+ image_file.getpixel((x,y))[3] 
			#print x, image_file.size[0]+y,  image_file.getpixel((x,y))[3] 
			
	#print blank_lines, '\n\n\n'
	blank_lines =[x for x in xrange(0,image_file.size[1]+image_file.size[0]) if blank_lines[x]==0]
	#blank_lines =[x-image_file.size[0] for x in xrange(0,len(blank_lines)) if blank_lines[x]>=image_file.size[0]]
	
	print blank_lines ,image_file.size[0]
	
#image_split(Image.open("f0.png"), [9,8])

image_crop(Image.open("f0[0][0].png"))