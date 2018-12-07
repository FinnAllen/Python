# author: Finnian Allen
# 12/06/2018
# This is a simple insertion sort program that
# takes in a list and sorts it least to greatest

import numpy as np

list = [9, 5, 7, 2, 8] # initialize our example list

n = len(list) # set n to the size of our list

unsorted = 1 # initialize unsorted to 1

while unsorted < n: # base while loop that will go tthrough the code until the last index has been reached
    nextItem = list[unsorted] # set our next item variable to list at the location of unsorted
    loc = unsorted; # set loc to unsorted to keep our index in question

    while ((loc > 0) and (list[loc - 1] > nextItem)):
        list[loc] = list[loc - 1]
        loc -= 1 # decrament loc
    unsorted += 1 # incrament unsorted
    list[loc] = nextItem; # set the list at the index to the next item

print(list) # print our list in order
