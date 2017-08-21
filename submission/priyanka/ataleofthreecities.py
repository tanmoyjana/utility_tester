import math
class ATaleOfThreeCities:
    def connect(self, ax, ay, bx, by, cx, cy):
        ab1 = []
        ab2 = []
        for i in list(ax):
            for j in list(bx):
                ab1.append(int(math.pow(i-j,2)))
        s1 =  min(ab1)
        for a in list(ay):
            for b in list(by):
                ab2.append(int(math.pow(a-b,2)))
        s2 = min(ab2)
        s = math.sqrt(s1+s2) #min distance of a and b
        print s
        bc1 = []
        bc2 = []
        for g in list(bx):
            for h in list(cx):
                bc1.append(int(math.pow(g-h,2)))
        s3 = min(bc1)
        for l in list(by):
            for m in list(cy):
                bc2.append(int(math.pow(l-m,2)))
        s4 = min(bc2)
        r = math.sqrt(s3+s4)  #min distance of c and b
        print r
        ac1 = []
        ac2 = []
        for p in list(ax):
            for q in list(cx):
                ac1.append(int(math.pow(p-q,2)))
        s5 = min(ac1)
        for o in list(ay):
            for n in list(cy):
                ac2.append(int(math.pow(o-n,2)))
        s6 = min(ac2)
        z = math.sqrt(s5+s6)  #min distance of a and c
        print z
        sum1 = s + r
        sum2 = s + z
        sum3 = r + z
        sum = min(sum1,sum2,sum3)  #min distance 
        return sum
        
                
                        
                
         
                
