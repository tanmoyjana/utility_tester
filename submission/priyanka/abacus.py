import math
class Abacus:
    def add(self,original,val):
        n = []
        s = []
        for num in original:
            n.append(num.split("---"))
        for i in n:
            s.append(len(i[1]))
        q = len(original)-1
        p = 0
        l = 0
        while q >= 0 :
           l += int(s[q]*(math.pow(10,p)))
           p = p + 1
           q = q - 1
        f = l + val
        t= len(original)-1
        k = 0
        result = []
        while t >= 0:
            b = ['0','0','0','0','0','0','0','0','0','0']
            k = int(f/(math.pow(10,t)))
            f = int(f%(math.pow(10,t)))
            b[9-k] = '---'
            r = ''.join(b)
            result.append(r)
            t = t - 1
        return tuple(result)
            
           
        
        
            
