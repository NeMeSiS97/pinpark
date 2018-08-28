#ScaleDown.py

import cv2

def scale800x600(imgOriginalScene):

    height = imgOriginalScene.shape[0]
    width = imgOriginalScene.shape[1]

    if width > 800:
      if height > 600:     
         width = 800
         height = 600
      
    img = cv2.resize(imgOriginalScene, (width, height)) 
    #cv2.imwrite("Resized.png",img)
    
    return img

#end function
