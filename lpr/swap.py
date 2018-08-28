import shutil
import os

def move(img):

 path = "/home/user/yolo/darknet/crop/"
 moveto ="/home/user/yolo/darknet/fini/"
 #files=os.listdir("C:\\Users\\user\\Desktop\\Lisence Plate Recognition\\imagesplate\\")
 #files.sort()
 #for f in files:
 head,f=os.path.split(img)
 src=path+f
 dst= moveto+f
 shutil.move(src,dst)
