class NonCoprimeGraph:
    def distance(self,n,s,t):
      m = []
      p = []
      if (n > s) and (n > t) and (1 < n < 1000000000):
       if (s == t):  #same number returns 0
        return 0
       else:
        for i in range(2,s):   #to find factors of s
            if s % i == 0:
                 m.append(i)
        for j in range(2,t):  #to find factors of t
            if t % j == 0:
                p.append(j)
        for j in m:
            for k in p:
                if (j == k):   #if common factor they are not coprime return 1>shortest path by one edge 
                    return 1
        z1 = []
        for x in m:
            for y in p:     #if no common factor  then factor multiplication 
                z = x * y
                if (z < n):  # if factor product exceeds n discard
                   z1.append(z)
        if (len(z1) == 0):    #if no such factor product exist return -1 
                    return -1
        else:                 #else return 2 the shortest distance as they are coprime
                    return  2
