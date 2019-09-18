#coding=utf-8
# I am not responsible of this code.
# They made me write it, against my will.
# 下面的代码，我不负责。因为是他们逼我写的，违背了我的意愿。

import cv2
import  os
from glob import glob

datadir="D:\PycharmProjects/Unmanned_aerial_vehicle/postitive_sample_ori/positive_sample_old1"
for fn in glob(os.path.join(datadir, '*.png')):
    img = cv2.imread(fn)
    res=cv2.resize(img,(64,64),interpolation=cv2.INTER_AREA)
    root,filename=os.path.split(fn)
    name,extension=os.path.splitext(filename)
    cv2.imwrite('D:\PycharmProjects/Unmanned_aerial_vehicle/training_data/positive_sample_1/%s.png'%(name),res)

print ('all done!')

