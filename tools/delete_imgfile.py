#coding=utf-8

import os

datadir="D:\PycharmProjects/Unmanned_aerial_vehicle/positve_sample_old"
deletedir="D:\PycharmProjects/Unmanned_aerial_vehicle/unmanned_aerial_vehicle_img"
def getfilename(datadir):
    filelist=[]
    for root,dir,filenames in os.walk(datadir):
        for filename in  filenames:
            filename=filename[4:]
            filelist.append(filename)
    return filelist

def deletefile(deletedir,filelist):
    for filename in filelist:
        file=os.path.join( deletedir, filename)
        if os.path.exists(file):
            os.remove(file)


if __name__=="__main__":
    filelist=getfilename(datadir)
    deletefile(deletedir,filelist)