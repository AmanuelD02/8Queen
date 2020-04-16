""" This module returns all the possible solutions to the 8 Queen Problem"""

from itertools import permutations
from pprint import pprint as pp
import time
# all possible solution

a = time.time()
all= permutations(range(8))

# function to check if the given list is corrrect in \ diagon

def diag1(lst):
    # iterate through all the queens in the list
    for q in range(8):
        Q = lst[q]
        count =0
        for j in range(q+1,8):
            count+=1
            #print("column:",j , "row:",lst[j],"Queen",Q)  # for checking the solution
            if lst[j] ==(Q+count):
                return False
    
    return True



def diag2(lst):
    for q in range(8):
        Q = lst[q]
        count = 0
        for j in range((q-1),-1,-1):
            count+=1
            #print("column:",j , "row:",lst[j],"Queen",Q)  # for checking the solution
            if lst[j] == Q+count:
                return False
    return True

sol=[]
for lst in all:
  
    if diag2(lst) and diag1(lst):
        sol.append(lst)


pp(sol)
print(len(sol))
print("Time Taken:",time.time()-a)


       