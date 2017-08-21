import math
class ATaleOfThreeCities():
    def connect(self,ax,ay,bx,by,cx,cy):
        list1= []
        list2= []
        list3= []
        i=0
        while i<len(ax):
            j=0
            while j<len(bx):
                AB= ((bx[j]-ax[i])*(bx[j]-ax[i])+(by[j]-ay[i])*(by[j]-ay[i]))
                list1.append(AB)
                j=j+1
            i=i+1
        k=0
        while k<len(bx):
            l=0
            while l<len(cx):
                BC= ((cx[l]-bx[k])*(cx[l]-bx[k])+(cy[l]-by[k])*(cy[l]-by[k]))
                list2.append(BC)
                l=l+1
            k=k+1
        m=0
        while m<len(cx):
            n=0
            while n<len(ax):
                AC= ((cx[m]-ax[n])*(cx[m]-ax[n])+(cy[m]-ay[n])*(cy[m]-ay[n]))
                list3.append(AC)
                n=n+1
            m=m+1
        distAB= math.sqrt(min(list1))
        distBC= math.sqrt(min(list2))
        distAC= math.sqrt(min(list3))
        y1= distAB + distBC
        y2= distBC + distAC
        y3= distAB + distAC
        return min(y1,y2,y3)
