class ChristmasTreeDecoration:
     def solve(self,col,x,y):
        b = 0
        for i in range(0,len(x)):
            if (col[x[i]-1] != col[y[i]-1]):  #matching colours of stars
                b += 1
        final =  len(col)-1-b
        if final > 0:
           print final
        else:
           return 0

                                        
                
                
