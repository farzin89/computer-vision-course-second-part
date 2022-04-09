import numpy as np
from numpy import genfromtxt


data = genfromtxt('bank_note_data.txt',delimiter=',')

labels = data[:,4]

features = data[:,0:4]
#print(features)

X = features
y = labels

# split data into train and test data

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.33,random_state=42)

   # print(X_train)
   #print(len(X_train))
   #print(len(X))
   #print(len(X_test))

   #print(y_train)
   #print(len(y_train))
   #print(len(y))
   #print(len(y_test))

from sklearn.preprocessing import MinMaxScaler

scaler_object = MinMaxScaler()
scaler_object.fit(X_train)
scaled_X_train = scaler_object.transform(X_train)
scaled_X_test = scaler_object.transform(X_test)

#print(scaled_X_train.max())

from keras.models import Sequential
from keras.layers import Dense

model = Sequential()

model.add(Dense(4,input_dim=4,activation='relu'))
model.add(Dense(8,activation='relu'))
model.add(Dense(1,activation='sigmoid'))

model.compile(loss = 'binary_crossentropy',optimizer='adam',metrics=['accuracy'])
model.fit(scaled_X_train,y_train,epochs=50,verbose=2)
