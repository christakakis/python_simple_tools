#Christakakis Panagiotis

#distributions.txt is used for testing the function
#Generated randomly and each line will corresponds
#to a discrete probability distribution

def min_KL_distributions(filename):

    """
    This function computes the KL divergence 
    between various discrete distributions finds
    the minimum and its index. 
    Receives as input a string (a file name).
    """

    #Libraries used
    import re
    import numpy as np
    from scipy.special import rel_entr

    #Reading the lines throughout the .txt file
    #passing by any special characters and save
    #floats into a list
    with open(filename, "r") as f:
        distributions = [
            list(map(float, re.findall(r"-?\d+(\.\d+)?", line)))
            for line in f.readlines()    
        ]
    
    #Iterate through the distributions list twice
    #and if i≠j append the row index with min KL
    #to the first loop index position
    index_list = []
    for i in range(len(distributions)):
        min_kl = 1000
        index = -1
        for j in range(len(distributions)):
            if i != j:
                dist_diverg = sum(rel_entr(distributions[i], distributions[j]))
                if dist_diverg < min_kl:
                    min_kl = dist_diverg
                    index = j
        index_list.append(index)
    
    return(index_list, min_kl, index)
    
min_KL_distributions("distributions.txt")