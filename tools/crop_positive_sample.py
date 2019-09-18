#coding=utf-8
# I am not responsible of this code.
# They made me write it, against my will.
# 下面的代码，我不负责。因为是他们逼我写的，违背了我的意愿。
import numpy as np
import cv2
import os
from os import walk
from os import path

rootdir="D:/PycharmProjects/Unmanned_aerial_vehicle/unmanned_aerial_vehicle_img"

#rootdir="D:\PycharmProjects/Unmanned_aerial_vehicle/tools\img"
# def get_fileNames(rootdir):
#     data=[]
#     for root, dirs, files in walk(rootdir, topdown=True):
#         for name in files:
#             _, ending = path.splitext(name)
#             if ending != ".jpg" and ending != ".jepg" and ending != ".png":
#                 continue
#             else:
#                 data.append(path.join(root, name))
#     return data

def get_filenames(rootdir):
    data=[]
    path_list=os.listdir(rootdir)
    path_list.sort(key=lambda x:int(x[:-4]))
    for filename in path_list:
        data.append(path.join(rootdir,filename))
    return data
# 获取文件路径
data=get_filenames(rootdir)

rects=[]
for img_path in data:
    # Read image
    img=cv2.imread(img_path)
    filepath, filename = path.split( img_path )
    name, extension = path.splitext( filename )
    # 创建一个窗口
    cv2.namedWindow("image", flags= cv2.WINDOW_NORMAL | cv2.WINDOW_FREERATIO)
    cv2.imshow("image", img)
    # 是否显示网格
    showCrosshair = False
    # 如果为Ture的话 , 则鼠标的其实位置就作为了roi的中心
    # False: 从左上角到右下角选中区域
    fromCenter = False
    # Select ROI
    ch=cv2.waitKey( 0 )
    #如果按键为n，则跳过该张图片
    if ch==110:

        continue
    else:
        #用空格确认选择的矩形
        rect = cv2.selectROI("image", img, showCrosshair, fromCenter)
        if rect==(0,0,0,0):
            continue
        else:
            print("选中 %s 矩形区域"%(img_path))
            x, y, w, h = rect
            if h<w:
                # Crop image
                if y+h/2-w/2<0:
                    imCrop = img[0: 0+w, x:x + w, :]
                    rect=[x,0,x+w,w]
                elif y +h/2+w/2 >img.shape[0]:
                    imCrop = img[img.shape[0]-w:img.shape[0], x:x + w, :]
                    rect = [x, img.shape[0]-w, x + w, img.shape[0]]
                else:
                    imCrop = img[int(y+h/2-w/2): int(y +h/2+w/2 ), x:x + w,:]
                    rect = [x,int(y+h/2-w/2),x + w,int(y +h/2+w/2 )]
            else:
                if  x + w / 2 - h / 2  < 0:
                    imCrop = img[y: y + h, 0:h, :]
                    rect = [0,y,h,y+h]
                elif x + w/2+h/2 > img.shape[1]:
                    imCrop = img[y: y +h , img.shape[1]-h:img.shape[1],:]
                    rect = [img.shape[1]-h,y,y+h,img.shape[1]]
                else:
                    imCrop = img[y: y +h , int(x+w/2-h/2):int(x + w/2+h/2),:]
                    rect = [int(x+w/2-h/2),y,int(x + w/2+h/2),y+h]
            rects.append(rect)
            print("矩形坐标为：",rect)
            # Display cropped image

            cv2.namedWindow( "image_roi", flags=cv2.WINDOW_NORMAL | cv2.WINDOW_FREERATIO )
            cv2.imshow("image_roi", imCrop)
            # filepath,filename=path.split(img_path)
            # name,extension=path.splitext(filename)
            cv2.imwrite("D:\PycharmProjects/Unmanned_aerial_vehicle\positve_sample_old/pos_%s.png"%(name), imCrop)
            #cv2.waitKey(0)

xmin,ymin,xmax,ymax=rects[0]
for rect in rects:
    if xmin>rect[0]:
        xmin=rect[0]
    if ymin>rect[1]:
        ymin=rect[1]
    if xmax<rect[2]:
        xmax=rect[2]
    if ymax<rect[3]:
        ymax=rect[3]
print('ymin:',ymin,'\nymax:',ymax,'\nxmin:',xmin,'\nxmax:',xmax)