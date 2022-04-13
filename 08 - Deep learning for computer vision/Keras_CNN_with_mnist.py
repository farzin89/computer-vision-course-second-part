import numpy as np
from tensorflow.keras.datasets import mnist
import matplotlib.pyplot as plt

(x_train,y_train),(x_test,y_test) = mnist.load_data()

#print(x_test.shape)

single_image = x_train[0]
plt.imshow(single_image,cmap='gray')


from keras.utils.np_utils import to_categorical
y_cat_test  = to_categorical(y_test,10)
y_cat_train = to_categorical(y_train,10)
print(y_cat_train[0])

single_image.max()

x_train = x_train/x_train.max() # /255
x_test = x_test/x_test.max() # /255

scaled_image = x_train[0]
scaled_image

plt.imshow(scaled_image,cmap='gray_r')

x_train.shape

x_train = x_train.reshape(60000,28,28,1)
x_train.shape

x_test = x_test.reshape(10000,28,28,1)
x_test.shape

from keras.models import Sequential
from keras.layers import Dense,Conv2D,MaxPool2D,Flatten

model = Sequential()

# Convolutional layer
model.add(Conv2D(filters=32,kernel_size=(4,4),input_shape=(28,28,1),activation='relu'))
# pooling layer
model.add(MaxPool2D(pool_size=(2,2)))
# 2d--> 1d
model.add(Flatten())
# Dense layer
model.add(Dense(128,activation='relu'))

model.add(Dense(10,activation='softmax'))

model.compile(loss = 'categorical_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])
model.summary()

model.fit(x_train,y_cat_train,epochs=2)

model.metrics_names

model.evaluate(x_test,y_cat_test)

from sklearn.metrics import classification_report

predictions = model.predict_classes(x_test)