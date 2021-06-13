# selecting sample images and flip them horizontally 
im1 = plt.imread('ml/dog.744.jpg')
plt.imshow(im1)
plt.axis('off')
plt.show()

rim1= np.fliplr(plt.imread('ml/dog.744.jpg'))
plt.imshow(rim1)
plt.axis('off')
plt.show()

im2 = plt.imread('ml/cat.3277.jpg')
plt.imshow(im2)
plt.axis('off')
plt.show()

rim2 = np.fliplr(plt.imread('ml/cat.3277.jpg'))
plt.imshow(rim2)
plt.axis('off')
plt.show()
