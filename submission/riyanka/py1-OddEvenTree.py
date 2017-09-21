from itertools import combinations as ic
import random
import itertools
class OddEvenTree():
    def getTree(self,x):
        c=[]
        y = ic(range(0,len(x)),2)
        for i in y:
            if (x[i[0]][i[1]]==x[i[1]][i[0]]) and (x[i[0]][i[0]]=='E') :
                for i in range(0, len(x)-1):
                    y = i
                    z = i+1
                    c.append((y,z))       

            elif (x[i[0]][i[1]]!=x[i[1]][i[0]]) or (x[i[0]][i[0]]!='E'):
                return [-1]

        m = random.sample(list(set(c)), len(x)-1)
        n = itertools.chain.from_iterable(m)
        return list(n)
        
