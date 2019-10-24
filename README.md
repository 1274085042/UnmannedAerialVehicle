# Unmanned Aerial Vehicle Detection  
## A demo of UAV(Unmanned Aerial Vehicle) Detection System  
[**Video UAV Detection**](https://github.com/1274085042/Unmanned_aerial_vehicle/blob/master/unmanned_aerial_vehicle_video/result.mp4)  
[![gif_demo][demo_gif]](https://github.com/1274085042/Unmanned_aerial_vehicle/blob/master/unmanned_aerial_vehicle_video/result.mp4)
_ _ _
## Code & Files  
### 1. My project includes the following files

* [main.py](main.py) is the main code for demos
* [svm_pipeline.py](svm_pipeline.py) is the UAV detection pipeline with SVM
* [visualization.py](visualizations.py) is the function for adding visalization  
### 2. Environment  
* OpenCV3, Python3.5
* OS: Win10
### 3. How to run the code  
 If you want to run the demo, you can simply run:
```sh
python main.py
```  
## Linear SVM Approach  
`svm_pipeline.py` contains the code for the svm pipeline.   

**Steps:**  
* Perform a Histogram of Oriented Gradients (HOG) feature extraction on a labeled training set of images and train a classifier Linear SVM classifier.
* A color transform is applied to the image and append binned color features, as well as histograms of color, to HOG feature vector. 
* Normalize features. 
* Implement a sliding-window technique and use SVM classifier to search for UAV in images.
* Run pipeline on a video stream and create a heat map of recurring detections frame by frame to reject outliers.



[//]: # (Image References)
[demo_gif]: ./unmanned_aerial_vehicle_video/result.gif
