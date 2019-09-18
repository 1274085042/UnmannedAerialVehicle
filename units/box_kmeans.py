#coding=utf-8
# I am not responsible of this code.
# They made me write it, against my will.
# 下面的代码，我不负责。因为是他们逼我写的，违背了我的意愿。

import numpy as np
import matplotlib.pyplot as plt
import os
import cv2

def getfilename(rootdir):
    datalist=[]
    fileslist=os.listdir(rootdir)
    for file in fileslist:
        datalist.append(os.path.join(rootdir,file))
    return datalist

datalist=getfilename("D:\PycharmProjects/Unmanned_aerial_vehicle/postitive_sample_ori/positive_sample_old1")
X = []
for data in datalist:
    img=cv2.imread(data)
    [w,h]=img.shape[0:2]

    X.append([w,h])
X=np.array(X)
#print(X)
# X=np.random.rand(100,2)
# print(X[0])
plt.scatter(X[:,0],X[:,1],s=50)
plt.show()

from sklearn.cluster import KMeans

#請KMeans分成三類
clf = KMeans(n_clusters=3)

#開始訓練！
clf.fit(X)

#這樣就可以取得預測結果了！
clf.labels_
print(clf.cluster_centers_)
#最後畫出來看看
#真的分成三類！太神奇了………無意義的資料也能分～
plt.scatter(X[:,0],X[:,1], c=clf.labels_)
plt.show()
#KMeans的使用時機就在於～你根本不知道測試的資料有什麼特性的時候
#就是用他的時候了，我稱KMeans為盲劍客 XD