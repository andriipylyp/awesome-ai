import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
import pickle
DATADIR = "PetImages"
CATEGORIES = ["Dog", "Cat"]
IMG_SIZE = 50

# training_data = []

# def create_training_data():
#     for category in CATEGORIES:
#         path = os.path.join(DATADIR, category)
#         class_num = CATEGORIES.index(category)
#         for img in os.listdir(path):
#             try:
#                 img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
#                 new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
#                 training_data.append([new_array, class_num])
#             except Exception as e:
#                 pass

# create_training_data()

# import random

# random.shuffle(training_data)

# X = []
# y = []

# for features, label in training_data:
#     X.append(features)
#     y.append(label)

# X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 1)



# pickle_out = open("X.pickle", "wb")
# pickle.dump(X, pickle_out)
# pickle_out.close()
# pickle_out = open("y.pickle", "wb")
# pickle.dump(y, pickle_out)
# pickle_out.close()

pickle_in = open("X.pickle", "rb")
X = pickle.load(pickle_in)
pickle_in.close()
pickle_in = open("y.pickle", "rb")
y = pickle.load(pickle_in)
pickle_in.close()

# print(y)


import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
# tf.executing_eagerly()

X = X/255.0

# model = Sequential([
#     Conv2D(16, 3, padding='same', activation='relu', input_shape=(IMG_SIZE, IMG_SIZE ,1)),
#     MaxPooling2D(),
#     Conv2D(32, 3, padding='same', activation='relu'),
#     MaxPooling2D(),
#     Conv2D(64, 3, padding='same', activation='relu'),
#     MaxPooling2D(),
#     Flatten(),
#     Dense(512, activation='relu'),
#     Dense(1, activation='sigmoid')
# ])

# model.compile(loss='binary_crossentropy',
#                 optimizer='adam',
#                 metrics=['accuracy'])
# model.fit(X,y,batch_size = 32,epochs = 3, validation_split=0.1)

# model.save('my_model.h5')
model = tf.keras.models.load_model('my_model.h5')
# model.eva
img_array2 = cv2.imread("Chinook-On-White-03.jpg", cv2.IMREAD_GRAYSCALE)
new_array2 = cv2.resize(img_array2, (IMG_SIZE, IMG_SIZE))


img_array1 = cv2.imread("Arthur,_the_cat.jpg", cv2.IMREAD_GRAYSCALE)
new_array1 = cv2.resize(img_array1, (IMG_SIZE, IMG_SIZE))
data = []
data.append(new_array1)
data.append(new_array2)
# plt.imshow(new_array2)
# plt.show()
data = np.array(data).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
data = data / 255.0
# plt.show()
# testing_data = [new_array, 1]
# print(model.predict_classes(new_array1))
# print(model.predict_classes(new_array2))
# test_loss, test_acc = model.evaluate(X,  y, verbose=2)


# print('\nTest accuracy:', test_acc)
predictions = model.predict(data)
# print(len(new_array2), len(new_array2[0]))
print(predictions)
print(np.around(predictions[0]), np.around(predictions[1]))


