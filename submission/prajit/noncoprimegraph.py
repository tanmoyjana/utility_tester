class NonCoprimeGraph():
    def distance(self,n,s,t):
        if s==t:
            return 0
        factor1=[]
        factor2=[]
        factor3=[]
        for i in range(2,s):
            if s%i==0:
                factor1.append(i)
        for j in range(2,t):
            if t%j==0:
                factor2.append(j)
        c=0
        for a in factor1:
            for b in factor2:
                if a==b:
                    return 1
                else:
                    c= a*b
                    if c<=n:
                        factor3.append(c)
        if len(factor3)==0:
            return -1
        elif len(factor3)>0:
            return 2
