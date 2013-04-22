from SimpleCV import *
import sys

class CameraCapture():
		
	_key = True
	_width = 640
	_height = 480
	def __init__(self,index,width = 640, height = 480):
		self.width = width
		self.height = height
		self.cam = Camera(index,prop_set={"width":self.width,"height":self.height})
			
	def setKey(self):
		if(self._key):
			self._key = False
		else:
			self._key = True
		
	def getNewImage(self):
		img = self.cam.getImage()
		if(self._key):
			return img
		else:
			img = img - img.colorDistance(Color.RED) #RED SEGMENTATION
			return img
		

if(len(sys.argv) != 3):
	print "\n>>>>Used as : python multiple.py <cam_index1> <cam_index2>\n"
	sys.exit(0)
#set camera index values from command line arguement
index1 = int(sys.argv[1])
index2 = int(sys.argv[2])	
#Make two camera objects 
cam1 = CameraCapture(index1)
cam2 = CameraCapture(index2)
width = cam1.width+cam2.width
disp = Display((width,cam1.height),0,'SimpleCV tutorial')

print("\n >>>Right click on the Image to exit!")

while disp.isNotDone():
	img1 = cam1.getNewImage()
	img2 = cam2.getNewImage()
	img3 = img1.sideBySide(img2)
	
	dwn = disp.leftButtonDownPosition()
	if (dwn is not None and dwn[0] <640):
		cam1.setKey()
	elif (dwn is not None and dwn[0] >= 640):
		cam2.setKey()
		
	img3.drawText("Camera 1",100,400,fontsize=40,color=Color.BLUE)
	img3.drawText("Camera 2",840,400,fontsize=40,color=Color.GREEN)
	img3.save(disp)
	if disp.mouseRight:
		break
print("\n >>>Program Exitted")
