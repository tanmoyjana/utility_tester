import math
class Abacus():
    def add(self , original , val):
        ab = []
        count = []
        org = list(original) #converting the tuple to a list
        n =( len(org) - 1 )
        p = 0
        num = 0
        result = 0
        j =( len(org) - 1 )
        t = 0
        out=[]
        for i in org :
            del ab[:] #emptying the list on each iteration
            ab.append ( i.split('---') ) #splitting a string when'---' is found
            count.append ( len ( list ( ab[ 0 ][ 1 ] ) ) ) #converting the value of the abacus to an integer
        while n >= 0 :
            num += int ( count [ n ] * (math.pow ( 10 , p ) ) ) 
            n = n-1
            p = p+1
        result = num + val
        while j >= 0:
            ret = [ 'o' , 'o' , 'o' , 'o' , 'o' , 'o' , 'o' , 'o' , 'o' , 'o' ]
            t = int ( result / ( math.pow (10 , j ) ) )
            result = int ( result % ( math.pow ( 10 , j ) ) )
            ret[ 9-t ] = '---' #implimenting the result on the abacus
            string = ''.join(ret) #joining the elements of the list
            out.append ( string )
            j = j-1
        return tuple(out)
