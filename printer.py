from solution import EightQ
from pprint import pprint as pp


class Printer:

    def __init__(self):
        E = EightQ()
        self.answer =E.result() 
        self._ppr = []
        self.ppr =[]

    def __call__(self):
        sols = self.q__printer()
        for i in sols:
            pp(i)
            print("\n\n")

    def __toDict(self, lst):
        _dict = {}
        
        for i in range(len(lst)):
            _dict[lst[i]] = i
        
        return _dict

    
    def __hash(self,num):
        
        line = (num) * " * " + " Q " + (8-num-1) * " * "
        return line

    def q__printer(self):
        for i in self.answer:
            self._ppr.append(self.__toDict(i))
            
        
        for solution in range(len(self._ppr)):
            self.ppr.append([])

            for row in self._ppr[solution]:
                
                self.ppr[solution].append(self.__hash(row))
        return self.ppr

        


chess = Printer()

print(chess())






