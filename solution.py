""" This module returns all the possible solutions to the 8 Queen Problem"""

from itertools import permutations

# all possible solution
all= permutations(range(8))

# function to check if the given list is corrrect in \ diagon

def diag1(lst):
    # iterate through all the queens in the list
    for q in range(8):
        Q = lst[q]

        for j in range(q+1,8):
            print("column:",j , "row:",lst[j],"Queen",Q)
            if lst[j] ==(Q+j):
                return False
    return True

        

        