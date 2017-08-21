class AdditionGame ():
    def getMaximumPoints ( self , A , B , C , N ):
        result = 0
        while N > 0 : 
            if ( A + B + C ) > 0 : 
                if max ( A , B , C ) == A :
                    result = result + A
                    A = A - 1
                elif max( A , B , C ) == B :
                    result = result + B
                    B = B - 1
                elif max( A , B , C ) == C :
                    result = result + C
                    C = C - 1
            N = N - 1
        return result
