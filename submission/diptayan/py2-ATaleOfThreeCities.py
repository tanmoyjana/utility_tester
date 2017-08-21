import math
class ATaleOfThreeCities():
    def connect( self , ax , ay , bx , by , cx , cy ):
        count_a_b = []
        count_a_c = []
        count_b_c = []
        result = []
        i = 0
        k = 0
        m = 0
        out = 0
        ax = list( ax )  #converting each tuple to a list
        ay = list( ay )
        bx = list( bx )
        by = list( by )
        cx = list( cx )
        cy = list( cy )

        while i < len( ax ):
            j = 0
            while j < len( bx ):
                res = math.sqrt( ( math.pow( ( ax[i] - bx[j] ) , 2 ) ) + ( math.pow( ( ay[i] - by[j] ) , 2 ) ) ) #counting the distance between two points
                count_a_b.append( res )
                j = j + 1
            i = i + 1
        result.append( min( count_a_b ) )  #taking the minimum distance in count
        while k < len( ax ):
            l = 0
            while l < len( cx ):
                res = math.sqrt( ( math.pow( ( ax[k] - cx[l] ) , 2 ) ) + ( math.pow( ( ay[k] - cy[l] ) , 2 ) ) )    #counting the distance between two points
                count_a_c.append( res )
                l = l+1
            k = k + 1
        result.append( min( count_a_c ) )    #taking the minimum distance in count
        while m < len( bx ):
            n = 0
            while n < len( cx ):
                res = math.sqrt( ( math.pow( ( bx[m] - cx[n] ) , 2 ) ) + ( math.pow( ( by[m] - cy[n] ) , 2 ) ) )    #counting the distance between two points
                count_b_c.append( res )
                n = n + 1
            m = m + 1
        result.append( min( count_b_c ) )   #taking the minimum distance in count
        for i in result :
            out = out + i
        out = out - max( result )    #excluding the maximum distance
        return out
        
