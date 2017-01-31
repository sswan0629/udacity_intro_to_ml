#!/usr/bin/python 

""" 
    Skeleton code for k-means clustering mini-project.
"""




import pickle
import numpy
import matplotlib.pyplot as plt
import sys
from networkx.algorithms.distance_measures import center
sys.path.append("../tools/")
plt.switch_backend("Qt5Agg")
from feature_format import featureFormat, targetFeatureSplit




def Draw(pred, features, poi, mark_poi=False, name="image.png", f1_name="feature 1", f2_name="feature 2", centers=None):
    """ some plotting code designed to help you visualize your clusters """

    ### plot each cluster with a different color--add more colors for
    ### drawing more than five clusters
    print("centers: ", centers)
    colors = ["b", "c", "k", "m", "g"]
    for ii, pp in enumerate(pred):
        print("ii: ", ii, " pp: ", pp, " pred[", ii, "]: ", pred[ii])
        plt.scatter(features[ii][0], features[ii][1], color = colors[pred[ii]])
        if len(centers)>0: 
            
            plt.plot(centers[pred[ii]][0], centers[pred[ii]][1], 'o', markerfacecolor=colors[-pred[ii]],
                markeredgecolor='k', markersize=6)

    

    ### if you like, place red stars over points that are POIs (just for funsies)
    if mark_poi:
        for ii, pp in enumerate(pred):
            if poi[ii]:
                plt.scatter(features[ii][0], features[ii][1], color="r", marker="*")
    plt.xlabel(f1_name)
    plt.ylabel(f2_name)
    plt.savefig(name)
    plt.show()



### load in the dict of dicts containing all the data on each person in the dataset
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "rb") )
### there's an outlier--remove it! 
data_dict.pop("TOTAL", 0)

print("Min: ", min([float(data_dict[name]["salary"]) for name in data_dict if float(data_dict[name]["salary"]) > 0]))
print("Max: ", max([float(data_dict[name]["salary"]) for name in data_dict if float(data_dict[name]["salary"]) > 0]))

### the input features we want to use 
### can be any key in the person-level dictionary (salary, director_fees, etc.) 
poi  = "poi"
feature_1 = "salary"
feature_2 = "exercised_stock_options"
# feature_3 = "total_payments"
# features_list = [poi, feature_1, feature_2, feature_3]

from sklearn.preprocessing import MinMaxScaler
import numpy as np
salaries = np.array([float(data_dict[name]["salary"]) for name in data_dict if float(data_dict[name]["salary"]) > 0]) 
stocks = np.array([float(data_dict[name]["from_messages"]) for name in data_dict if float(data_dict[name]["from_messages"]) > 0])

print(max(stocks), min(stocks))
scaler= MinMaxScaler()
scaler.fit_transform(salaries)
print(scaler.transform(np.array([200000.])))
scaler= MinMaxScaler()
scaler.fit_transform(stocks)
print(scaler.transform(np.array([1000000.]))) 
                                




features_list = [poi, feature_1, feature_2]

data = featureFormat(data_dict, features_list )
poi, finance_features = targetFeatureSplit( data )


### in the "clustering with 3 features" part of the mini-project,
### you'll want to change this line to 
### for f1, f2, _ in finance_features:
### (as it's currently written, the line below assumes 2 features)
# for f1, f2, _ in finance_features:
for f1, f2 in finance_features:
    plt.scatter( f1, f2)
plt.show()

### cluster here; create predictions of the cluster labels
### for the data and store them to a list called pred

# from sklearn.cluster import KMeans
# k_means = KMeans(n_clusters=2)
# pred = k_means.fit_predict(finance_features)






### rename the "name" parameter when you change the number of features
### so that the figure gets saved to a different file
try:
    Draw(pred, finance_features, poi, mark_poi=False, name="clusters.pdf", f1_name=feature_1, f2_name=feature_2, centers = k_means.cluster_centers_)
except NameError:
    print("no predictions object named pred found, no clusters to plot")
