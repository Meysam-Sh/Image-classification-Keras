# imports
from skimage import data
import tensorflow as tf
import numpy as np
import cv2
from matplotlib import pyplot as plt
from scipy.ndimage import convolve


# selecting a sample image form dataset 
img = Image.open('Sample_dog.jpg')
plt.imshow(img)
plt.axis('off') 
plt.title('Original Image') 
plt.show()

img = Image.open('Sample_dog.jpg')
img = tf.image.rgb_to_grayscale(img)
img = tf.Session().run(img)
img = img.reshape([340,453])

img = np.expand_dims(img, -1)
img = np.expand_dims(img, 0) 

# filters applied on the image 
ver_filter = np.array([[-2., -1. ,  0.  ,  1. ,  2.],
                   [-2. , -1. ,  0.  ,  1. ,  2. ],
                   [-2. , -1.  ,  0.  ,  1.  ,  2. ],
                   [-2. , -1. ,  0.  ,  1. , 2. ],
                   [-2., -1. ,  0.  ,  1. ,  2.]])

hor_filtr = np.array([[-0.25, -0.4 , -0.5 , -0.4 , -0.25],
                   [-0.2 , -0.5 , -1.  , -0.5 , -0.2 ],
                   [ 0.  ,  0.  ,  0.  ,  0.  ,  0.  ],
                   [ 0.2 ,  0.5 ,  1.  ,  0.5 ,  0.2 ],
                   [ 0.25,  0.4 ,  0.5 ,  0.4 ,  0.25]])

Gauss_filter = np.array([[1  ,  4  ,  7  ,  4  ,  1],
                      [4  ,  16  ,  26  ,  16  ,  4],
                      [7  ,  26  ,  41  ,  26  ,  7],
                      [4  ,  16  ,  26  ,  16  ,  4],
                      [1  ,  4  ,  7  ,  4  ,  1]])

filters = np.concatenate([[ver_filter], [hor_filtr],[Gauss_filter]])  
filters = np.expand_dims(filters, -1)  
filters = filters.transpose(1, 2, 3, 0) 

# Convolve image
ans = tf.nn.conv2d((img / 255.0).astype('float32'),
                   filters,
                   strides=[1, 1, 1, 1],
                   padding='SAME')

with tf.Session() as sess:
    ans_np = sess.run(ans) 

filtered1 = ans_np[0, ..., 0]
filtered2 = ans_np[0, ..., 1]
filtered3 = ans_np[0, ..., 2]

# plotting the image afer appliyng each filter 
plt.matshow(filtered1)
plt.axis('off') 
plt.title('ver_filter') 
plt.show()


plt.matshow(filtered2)
plt.axis('off') 
plt.title('hor_filter') 
plt.show() 


plt.matshow(filtered3)
plt.axis('off') 
plt.title('Guss_filter') 
plt.show()
