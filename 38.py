import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.multiclass import OneVsRestClassifier
import cv2

data = load_digits()

imgs = data.images
plt.figure(figsize=(20,10))
columns = 5
for i in range(5):
    plt.subplot(5 / columns + 1, columns, i + 1)
    plt.imshow(imgs[i],cmap=plt.cm.gray_r)
	
X = data.data
y = data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)


svm = SVC()
svm.fit(X_train,y_train)

plt.figure(figsize=(20,10))
op = svm.predict(X[0:10])
columns = 5
for i in range(5):
    splt = plt.subplot(5 / columns + 1, columns, i + 1)
    splt.set_title(op[i])
    plt.imshow(imgs[i],cmap=plt.cm.gray_r,)
	
	