#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
from sklearn.metrics.classification import accuracy_score
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn import svm


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

#########################################################

### Reduce the training data set
features_train=features_train[:int(len(features_train) / 100)]
labels_train=labels_train[:int(len(labels_train) / 100)]

c_values = [
#     10, 
#     100, 
#     1000, 
    10000]
for v in c_values: 
    clf = svm.SVC(kernel="rbf", C=v)
    t = time()
    clf.fit(features_train, labels_train)
    print("Training time: ", round(time()-t, 3), "s")
    
    t = time()
    pred = clf.predict(features_test) 
    print("Prediction time: ", round(time()-t, 3), "s")
    accu = accuracy_score(labels_test, pred)
    print("Accuracy: ", accu )
    
    print(sum(pred))
    

