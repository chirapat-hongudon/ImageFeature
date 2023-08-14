import cv2
import numpy as np

# Load the image as grayscale
img_gray = cv2.imread('Cars Dataset\\train\\Hyundai Creta\\106.jpg', cv2.IMREAD_GRAYSCALE)

# Resize the image
img_new = cv2.resize(img_gray, (128, 128), interpolation=cv2.INTER_AREA)

# Define HOG parameters
win_size = (128, 128)
cell_size = (8, 8)
block_size = (16, 16)
block_stride = (8, 8)
num_bins = 9

# Create a HOG descriptor
hog = cv2.HOGDescriptor(win_size, block_size, block_stride, cell_size, num_bins)

# Compute the HOG Descriptor for the grayscale image
hog_descriptor = hog.compute(img_new)

print('HOG Descriptor:', hog_descriptor)
