import cv2
import glob
import numpy as np

import Main
import ScaleDown
import DetectChars
import DetectPlates
import PossiblePlate
import swap

while(1):
  
  for img in glob.glob("/home/user/yolo/darknet/crop/*"):
    n= cv2.imread(img)
    yoyo=Main.main(n,img)
    swap.move(img)
    
 
    
