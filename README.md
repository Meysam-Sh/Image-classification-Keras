In this project, a classifier is built for classifying between dogs and cats using the dataset available on Kaggle. The dataset consists of 25k training images and 12.5k test images. At first vertical, horizontal, and Gaussian filters are applied to the images to detect the edges of the images and to make the images blur. After that, a Convolutional Neural Network is implemented using the Keras framework for the classification task.

----------------------------
**Original image along with the vertical, horizontal, and Gaussian filters applied to it:**

![BeforeFilter](https://user-images.githubusercontent.com/62679750/121814388-317dbb80-cc47-11eb-84d8-0f601c05dd09.png)
![HorizontalFilter](https://user-images.githubusercontent.com/62679750/121814481-b4067b00-cc47-11eb-9371-6c49db22ff4d.png)
![VerticalFilter](https://user-images.githubusercontent.com/62679750/121814517-e2845600-cc47-11eb-9fee-a34ea1482a6e.png)
![GussianFilter](https://user-images.githubusercontent.com/62679750/121814520-e44e1980-cc47-11eb-9763-142622690fce.png)

----------------------------
**Vertical flip of the image:**
![Dog](https://user-images.githubusercontent.com/62679750/121814702-c8974300-cc48-11eb-878b-921ab55568ec.png)
![dog-flipped](https://user-images.githubusercontent.com/62679750/121814704-ca610680-cc48-11eb-92b7-0fff607ca376.png)
        ![cat](https://user-images.githubusercontent.com/62679750/121814734-fd0aff00-cc48-11eb-9366-8947519c10b8.png)
        ![cat-flipped](https://user-images.githubusercontent.com/62679750/121814737-ff6d5900-cc48-11eb-9b79-5888a26e0f6c.png)
