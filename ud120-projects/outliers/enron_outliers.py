#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot as plt
sys.path.append("../tools/")
plt.switch_backend("Qt5Agg")

from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "rb") )
features = ["salary", "bonus"]

## Find the outlier
for name in data_dict.keys(): 
    if float(data_dict[name]['salary']) > 2600000:
        print(name, data_dict[name])
    if float(data_dict[name]['salary']) > 1000000:
        print(name, " salary ", data_dict[name]["salary"], " bonus ",data_dict[name]["bonus"])
    if float(data_dict[name]['bonus']) > 6000000:
        print(name, " salary ", data_dict[name]["salary"], " bonus ",data_dict[name]["bonus"])

data_dict.pop("TOTAL", 0)
data = featureFormat(data_dict, features)



### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    plt.scatter( salary, bonus )

plt.xlabel("salary")
plt.ylabel("bonus")
plt.show()


