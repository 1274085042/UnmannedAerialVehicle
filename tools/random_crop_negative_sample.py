#coding=utf-8
# I am not responsible of this code.
# They made me write it, against my will.
# 下面的代码，我不负责。因为是他们逼我写的，违背了我的意愿。

import cv2
import random
import os

#datadir="D:\PycharmProjects/Unmanned_aerial_vehicle/no_umannde_aerial_vehicle"
datadir="D:\PycharmProjects/Unmanned_aerial_vehicle/no_unmanned_aerial_vehicle_img"
def get_filename(datadir):
    data=[]
    for root,dir,filename in os.walk(datadir):
        for name in filename:
            _,ending=os.path.splitext(name)
            if ending !='.jpeg' and ending !='.jpg' and ending !='.png':
                continue
            else:
                data.append(os.path.join(root,name))
    return data
# 读取图片
data=get_filename(datadir)


for img_path in data:
    img = cv2.imread(img_path )

    # h、w为想要截取的图片大小
    h = 64
    w = 64

    count = 0
    while 1:
        # 随机产生x,y   此为像素内范围产生
        y = random.randint( 0, img.shape[0] )
        x = random.randint( 0, img.shape[1] )
        # 随机截图
        if y+h>img.shape[0]:
            continue
        elif x+w>img.shape[1]:
            continue
        else:
            count += 1
            cropImg = img[(y):(y + h), (x):(x + w)]
            filepath,filename=os.path.split(img_path)
            name,extension=os.path.splitext(filename)
            cv2.imwrite( 'D:\PycharmProjects/Unmanned_aerial_vehicle/negative_sample/neg_%s_%s.png'%(name,str(count)), cropImg )

        if count == 50:
            break
