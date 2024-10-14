# My-projects
This repository contains my small python projects.

## 1 - [Detecting coins using OpenCV](https://github.com/ms0525/My-projects/blob/main/Deteccting%20Coins%20using%20OpenCV/Detecting_coins.ipynb)

This guide explains how to detect coins or other circular objects in an image using OpenCV. The detection process leverages image processing techniques such as color conversion, blurring, and circle detection using the Hough Transform. Each step in this process is outlined below, along with explanations for the reasoning behind them.

### 1. Read the image 
TThe first step is reading the image using OpenCV's `cv2.imread()` method. When OpenCV reads an image, it stores it in BGR (Blue, Green, Red) format by default. However, many image processing tasks, including visualization, work best in RGB (Red, Green, Blue) format.
- The image is read into a NumPy array in the BGR format, which is the standard format for OpenCV.
- To standardize the processing across different environments (e.g., for display in libraries like Matplotlib), we convert the image to RGB format.

Since many applications and display libraries, such as Matplotlib, assume the image is in RGB format, we need to convert the image. This also makes the image more intuitive to work with, as RGB is the standard for most image operations. Convert the BGR image to RGB using `cv2.cvtColor(img, cv2.COLOR_BGR2RGB)`.

### 2. Convert it into grey-scale image ()
For many image processing algorithms, working with a grayscale image simplifies the computations. In grayscale, the image has only intensity information (i.e., shades of gray), making it easier to identify objects based on contrast differences.
- The RGB image is converted to grayscale to reduce the complexity of the image data.
- Grayscale simplifies the process of detecting edges and shapes, which is critical for tasks like circle detection.
Convert the RGB image to grey scale using `cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)`.

### 3. Blur the image
To reduce noise in the image, apply a median blur using `cv2.medianBlur(gray, 5)`. This step helps smooth the image, making it easier to detect shapes without interference from small details or irregularities.
- Blurring helps reduce noise and minor distortions that could interfere with accurate shape detection.
- A median blur is used because it is particularly effective in removing noise while preserving edges, which is important for detecting distinct boundaries like those of coins.

### 4. Finds Circles
We use the Hough Circle Transform `cv2.HoughCircles()` to detect circular shapes in the image. This algorithm identifies circles based on the geometric properties of the objects. 
- The Hough Circle Transform identifies circles in the image by analyzing edge points and their geometric distribution.
- Key parameters:
  - dp controls the resolution of the accumulator array. A value of 1.2 means the resolution is slightly reduced, which balances accuracy and computation speed.
  - minDist sets the minimum distance between detected circles to avoid multiple detections of the same coin.
  - param1 and param2 control edge detection sensitivity. param1 is the higher threshold for edge detection, and param2 is the threshold for detecting a circle based on its geometric shape.
  - minRadius and maxRadius restrict the size of the circles detected, helping to filter out objects that are not likely to be coins.

### 5. Draw Circles
Once the circles are detected, the next step is to visualize the results by drawing the circles on the original image.
Draw the circles using `cv2.circle(cimg, (circles[0][i][0], circles[0][i][1]), circles[0][i][2], (0,255,0),2)` method.
- Iterate through the detected circles and draws each one on the image using `cv2.circle()`.
- The color (0, 255, 0) specifies a green circle with a thickness of 2.

The coin detection process outlined above uses a combination of image processing techniques to identify circular objects in an image. Converting the image to grayscale and applying a median blur reduces noise, while the Hough Circle Transform accurately detects circular shapes. The detected circles are then drawn on the original image for visualization. These steps can be easily adapted to detect other circular objects or optimized based on specific image conditions.

## 2 - [Image Loading and Processing](https://github.com/ms0525/My-projects/blob/main/Image%20Loading%20and%20Processing/notebook.ipynb)

In this project I practiced image processing using PIL. I did the following operations.
1. Opening images with PIL
2. Image manipulation with PIL (resizing, cropping, rotating, flipping, converting to greyscale (or other color modes)
3. Exploring and understanding images as arrays of data and it's color channels

## 3 - [Netflix Data Analysis](https://github.com/ms0525/My-projects/blob/main/Netflix%20Data%20Analiysis/notebook.ipynb)
## 4 - [SI_TI Python Script](https://github.com/ms0525/My-projects/blob/main/SI_TI%20Python%20Script/plot_graph.py)
A python script to get spatial information and temporal information average values of multiple video files in a folder. It saves .txt file in log folder and saves a seperate .json file containing all the average values of the video files in the folder. 
