# Unmanned Aerial Vehicle Detection  
## A demo of UAV(Unmanned Aerial Vehicle) Detection System  
[**Video UAV Detection**](https://github.com/1274085042/Unmanned_aerial_vehicle/blob/master/unmanned_aerial_vehicle_video/result.mp4)  
![gif_demo][demo_gif]
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
### Extract Histogram of Oriented Gradients (HOG) from training images
The code for this step is contained in the function named `extract_features` and codes from line 95 to 146 in `svm_pipeline.py`. 
 If the SVM classifier exist, load it directly. 
 
 Otherwise, I started by reading in all the `UAV` and `non-UAV` images.Here is an example of one of each of the `UAV` and `non-UAV` classes:  
 ![][picture1]  
 I then explored different color spaces and different `skimage.hog()` parameters (`orientations`, `pixels_per_cell`, and `cells_per_block`).  I grabbed random images from each of the two classes and displayed them to get a feel for what the `skimage.hog()` output looks like.
  
 To optimize the HoG extraction, I **extract the HoG feature for the entire image only once**. Then the entire HoG image
is saved for further processing. (see line 327 to 329 in  `svm_pipeline.py`)
### Final choices of HOG parameters, Spatial Features and Histogram of Color
I tried various combinations of parameters and choose the final combination as follows 
(see line 25-34 in `svm_pipeline.py`):
* `YCrCb` color space
* orient = 9  # HOG orientations
* pix_per_cell = 8 # HOG pixels per cell
* cell_per_block = 2 # HOG cells per block, which can handel e.g. shadows
* hog_channel = "ALL" # Can be 0, 1, 2, or "ALL"
* spatial_size = (32, 32) # Spatial binning dimensions
* hist_bins = 32    # Number of histogram bins
* spatial_feat = True # Spatial features on or off
* hist_feat = True # Histogram features on or off
* hog_feat = True # HOG features on or off

All the features are **normalized** by line 569 to 571 in `svm_pipeline.py`, which is a critical step. Otherwise, classifier 
may have some bias toward to the features with higher weights.
### How to train a classifier
I randomly select 20% of images for testing and others for training, and a linear SVM is used as classifier.  
### Sliding Window Search
For this SVM-based approach, I use three scales of the search window (96x96 288x288 and 640x640, see line 50).

For every window, the SVM classifier is used to predict whether it contains a UAV nor not. If yes, save this window (see 
line 371 to 376 in `svm_pipeline.py`). In the end, a list of windows contains detected UAVs are obtianed.  
### Create a heat map of detected UAVs
After obtained a list of windows which may contain UAVs, a function named `generate_heatmap` (in line 492 in 
`svm_pipeline.py`) is used to generate a heatmap. Then a threshold is used to filter out the false positives.  
### Image vs Video implementation
**For image**, we could directly use the result from the filtered heatmap to create a bounding box of the detected 
UAV. 

**For video**, we could further utilize neighbouring frames to filter out the false positives, as well as to smooth 
the position of bounding box. 
* Accumulate the heatmap for N previous frame.  
* Apply weights to N previous frames: smaller weights for older frames.
* I then apply threshold and use `scipy.ndimage.measurements.label()` to identify individual blobs in the heatmap.  
* I then assume each blob corresponded to a UAV and constructe bounding boxes to cover the area of each blob detected.  
  
## Discussion  
**Obviously, our method does not meet the requirement of real-time due to the fact of sliding window approach is time consuming!** We could use image downsampling, multi-threads, or GPU processing to improve the speed. But, there are probably a lot engineering work need to be done to make it running real-time. 
  
[//]: # (Image References)
[demo_gif]: ./unmanned_aerial_vehicle_video/result.gif
[picture1]: ./examples/picture1.png
