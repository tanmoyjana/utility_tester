class ChristmasTreeDecoration():
    def solve( self , col , x , y) :
        stars = []
        i = 0
        p = 0
        m = 0
        n = 0
        count = 0
        while i < len( col ):
            stars.append( col[ i ] )
            i = i + 1
        while p < len( x ) :
            m = int( x[ p ] ) - 1
            n = int( y[ p ] ) - 1
            if stars[ m ] != stars[ n ] :  #taking the number of beautiful connections in count
                count = count + 1
            p = p + 1
        if ( len( col ) - count - 1 ) >= 0 :
            return ( len( col ) - count - 1 )  #returns the number of ugly connections
        else:
            return 0
