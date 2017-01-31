#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import math
from pandas.core.common import isnull
enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))
print(list(list(enron_data.values())[0].keys()))
print(enron_data.keys())
print(len(enron_data))
print(len(list(enron_data.values())[0]))
print("poi: ",sum([d['poi'] for d in enron_data.values()]))
pj = enron_data["Prentice James".upper()]
print(pj['exercised_stock_options'] + pj['restricted_stock'])
wc = enron_data["Colwell Wesley".upper()]
print(wc['from_this_person_to_poi']) 
money=["total_payments"]
poi = ["Skilling Jeffrey k".upper(),"LAY KENNETH L".upper(), "FASTOW ANDREW S"]
for p in poi:
    print(p, " ", enron_data[p]) 
    print(p, " ", sum([enron_data[p][m] for m in money])) 
print("Not NaN ", sum([enron_data[p]["total_payments"]  != "NaN" for p in enron_data.keys() if enron_data[p]["poi"]]))
print(18/146-1)