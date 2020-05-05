""" This module returns all the possible solutions to the 8 Queen Problem"""

from itertools import permutations
from pprint import pprint as pp
import time
# all possible solution
class EightQ:
    def __init__(self):
        self.all= permutations(range(8))
        self.sol = []

# function to check if the given list is corrrect in \ diagon

    def __diag1(self,lst):

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

    def __diag2(self,lst):

        for q in range(8):
            Q = lst[q]
            count = 0

            for j in range((q-1),-1,-1):
                count+=1
                #print("column:",j , "row:",lst[j],"Queen",Q)  # for checking the solution
                if lst[j] == Q+count:
                    return False
        return True
    
    def result(self):
        for lst in self.all:
            if self.__diag2(lst) and self.__diag1(lst):
                self.sol.append(lst)
        return self.sol


def main():
    ans = EightQ()
    pp(ans.result())


if __name__ == '__main__':
    main()