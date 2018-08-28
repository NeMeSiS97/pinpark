import cv2
import os
import shutil
from PIL import Image
import glob
from pathlib import Path
import subprocess
#import pytesseract
def convert(num,size):
    dw = size[0]
    dh = size[1]
    num[1] = num[1]*dw
    num[3] = num[3]*dw
    num[2] = num[2]*dh
    num[4] = num[4]*dh
    x=num[1]-(num[3]/2)
    y=num[2]-(num[4]/2)
    w=num[3]
    h=num[4] 
    return (int(round(x)),int(round(y)),int(round(w)),int(round(h)))


txtfiles = []
count=1
cls_id=0
while(1):
    for file1 in glob.glob1(os.getcwd()+"/images/","*.png"):
        nameout=file1[:file1.find(".png")]
        i=0
        os.system("./darknet detect cfg/yolo-voc.2.0.cfg yolo-voc_2000.weights images/"+nameout+".png")
        my_file = Path(os.getcwd()+"/images/"+nameout+".txt")
        if my_file.exists():
            im=Image.open("images/"+nameout+".png")
            s=im.size
            a=[0.0,0.0,0.0,0.0,0.0]
            with open("images/"+nameout+'.txt','r') as f:
                for line in f:
                    for word in line.split():
                        a[i]=float(word) 
                        i=i+1  
            f.close()
            bb = convert(a,s)
            f=open('bbox/'+nameout+".txt","w")
            f.write(" ".join([str(int(round(a))) for a in bb]) + "\n")
            f.close()
            img=cv2.imread("images/"+nameout+".png")
            crop_img=img[bb[1]:bb[1]+bb[3], bb[0]:bb[0]+bb[2]]
	    cv2.imwrite("crop/"+nameout+".png", crop_img)
	    shutil.move(os.getcwd()+"/images/"+nameout+".png",os.getcwd()+"/finish/"+nameout+".png")
	    subprocess.Popen(['python','lpr/loop.py'])
	    
