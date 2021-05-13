# from image.sudokuMain import sudoku_main
import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
from numpy.core.shape_base import stack
from tensorflow.keras.models import load_model
from .sudoku_main import *
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
# from image.sudokuMain import *

def handle_uploaded_file(f):
    with open('static_my_project/input.jpg', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)



def image_processor(selected_option):
    img1 = cv2.imread('static_my_project/input.jpg')
    if selected_option == "1":
        img2 = binarize(img1)
    elif selected_option == "2":
        img2 = invert(img1)
    elif selected_option == "3":
        img2 = hist_eq(img1)
    elif selected_option == "4":
        img2 = sudoku_main(img1)
    else:
        return False
    cv2.imwrite('static_my_project/output.jpg', img2)
    return True


def binarize(img):
    print("hi2", type(img))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    bin_img = np.where(img>128, 255, 0)
    return bin_img

def invert(img):
	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	inv_img = (255-img)
	return inv_img

def hist_eq(img):
    data = img.copy().flatten()
    hist, bins = np.histogram(data, 256, density=True)
    cdf = hist.cumsum()
    cdf = 255*cdf/cdf[-1]
    img_eq = np.interp(data, bins[:-1], cdf)
    return img_eq.reshape(img.shape)

#***************** Utilities of Sudoku Solver ****************************#

# def preProcess(img):
#     #imgGray is grayscale image of img
#     imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
#     #adding Gaussian blur
#     imgBlur = cv2.GaussianBlur(imgGray, (5,5), 1)
#     #applying adaptive filter
#     imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, 1, 1, 11, 2)
#     return imgThreshold

# #Finding the biggest contour and declaring it as sudoku puzzle
# def biggestContour(contours):
#     biggest = np.array([])
#     max_area = 0
#     for i in contours:
#         area = cv2.contourArea(i)
#         if area > 50:
#             peri = cv2.arcLength(i, True)
#             approx = cv2.approxPolyDP(i, 0.02*peri, True)
#             if area > max_area and len(approx) == 4:
#                 biggest = approx
#                 max_area = area
#     return biggest, max_area

# #re order points for warp perspective
# def reorder(myPoints):
#     myPoints = myPoints.reshape((4,2))
#     myPointsNew = np.zeros((4,1,2), dtype = np.int32)
#     add = myPoints.sum(1)
#     myPointsNew[0] = myPoints[np.argmin(add)]
#     myPointsNew[3] = myPoints[np.argmax(add)]
#     diff = np.diff(myPoints, axis = 1)
#     myPointsNew[1] = myPoints[np.argmin(diff)]
#     myPointsNew[2] = myPoints[np.argmax(diff)]
#     return myPointsNew

# #splitting the image into 81 different images
# def splitBoxes(img):
#     rows = np.vsplit(img, 9)
#     boxes = []
#     for r in rows:
#         cols = np.hsplit(r,9)
#         for box in cols:
#             boxes.append(box)
#     return boxes


# #Step4
# def getPredection(boxes,model):
#     result = []
#     for image in boxes:
#         ## PREPARE IMAGE
#         img = np.asarray(image)
#         img = img[4:img.shape[0] - 4, 4:img.shape[1] -4]
#         img = cv2.resize(img, (28, 28))
#         img = img / 255
#         img = img.reshape(1, 28, 28, 1)
#         ## GET PREDICTION
#         predictions = model.predict(img)
#         classIndex = model.predict_classes(img)
#         probabilityValue = np.amax(predictions)
#         ## SAVE TO RESULT
#         if probabilityValue > 0.8:
#             result.append(classIndex[0])
#         else:
#             result.append(0)
#     return result

# def displayNumbers(img,numbers,color = (0,255,0)):
#     secW = int(img.shape[1]/9)
#     secH = int(img.shape[0]/9)
#     for x in range (0,9):
#         for y in range (0,9):
#             if numbers[(y*9)+x] != 0 :
#                  cv2.putText(img, str(numbers[(y*9)+x]),
#                                (x*secW+int(secW/2)-10, int((y+0.8)*secH)), cv2.FONT_HERSHEY_COMPLEX_SMALL,
#                             2, color, 2, cv2.LINE_AA)
#     return img

# def intializePredectionModel():
#     model = load_model('/home/animesh-kumar/Desktop/semester6/img-processing/project/src/image/myModel.h5')
#     return model