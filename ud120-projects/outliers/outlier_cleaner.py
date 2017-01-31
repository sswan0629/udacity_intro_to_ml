#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    import numpy as np
    cleaned_data = []

    ### your code goes here
    total = len(predictions)
    
    errors = np.array([[abs(predictions[i][0] - net_worths[i][0]) ] for i in range(total)])
    
    
    sorted_errors = sorted(errors)
    cleaned = sorted_errors[:int(total*0.9)]# sort errors
    for i in range(total):
        if errors[i] in cleaned and len(cleaned) > 0: 
            cleaned_data.append((ages[i][0], net_worths[i][0], errors[i][0]))
            cleaned.remove(errors[i])
    return cleaned_data

