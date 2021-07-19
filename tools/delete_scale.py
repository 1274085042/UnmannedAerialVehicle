#coding=utf-8

import os
import cv2

def getfilename(rootdir):
    datalist=[]
    fileslist=os.listdir(rootdir)
    for file in fileslist:
        datalist.append(os.path.join(rootdir,file))
    return datalist

def deletefile_scale(datadir,scale):
    datalist=getfilename(datadir)
    for img in datalist:
        image=cv2.imread(img)
        if image.shape[0]<scale:
            os.remove(img)

if __name__=="__main__":
    datadir="D:\PycharmProjects/Unmanned_aerial_vehicle/postitive_sample_ori/positive_sample_old1"
    deletefile_scale( datadir, 50 )