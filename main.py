#coding=utf-8
from moviepy.editor import VideoFileClip
from svm_pipeline import *
#import matplotlib.pyplot as plt
import os

def pipeline_svm(img):

    output = unmanned_aerial_vehicle_detection_svm(img)
    return output

def get_filenames(rootdir):
    data=[]
    path_list=os.listdir(rootdir)
    path_list.sort(key=lambda x:int(x[:-4]))
    for filename in path_list:
        data.append(path.join(rootdir,filename))
    return data


if __name__ == "__main__":

    demo = 1  # 1:image (SVM), 2: video (SVM pipeline)

    if demo == 1:
        filename = 'D:\PycharmProjects/Unmanned_aerial_vehicle/unmanned_aerial_vehicle_img/346.png'
        #filename = 'D:\PycharmProjects/Unmanned_aerial_vehicle\examples/175.png'
        #filename='D:\PycharmProjects/vehicle-detection-master\examples/test1.jpg'
        image = mpimg.imread(filename)

        #SVM pipeline
        draw_img = pipeline_svm(image)
        fig = plt.figure()
        plt.imshow(draw_img)
        #cv2.imwrite("prediction.png",draw_img)
        plt.title('svm pipeline', fontsize=30)
        plt.show()

    elif demo == 2:
        # SVM pipeline

        video_output = 'unmanned_aerial_vehicle_video/airplane_svm8.mp4'
        clip1 = VideoFileClip( "unmanned_aerial_vehicle_video/airplane.mp4" ).subclip(0,89)
        clip = clip1.fl_image( pipeline_svm )
        clip.write_videofile( video_output, audio=False )

    else:
        datadir="D:\PycharmProjects/Unmanned_aerial_vehicle/unmanned_aerial_vehicle_img"
        img_list=get_filenames(datadir)
        for img in img_list[2200:2205]:
            dir,file=path.split(img)
            image = mpimg.imread( img )
            # SVM pipeline
            draw_img = pipeline_svm( image )
            fig = plt.figure()
            plt.imshow( draw_img )
            plt.title( '%s'%(file), fontsize=10 )
            plt.show()