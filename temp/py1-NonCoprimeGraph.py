class NonCoprimeGraph():
     def distance(self,n, s, t):
        cs = 2
        ct = 2
        count_s = []
        count_t = []
        mult = 0
        res = []
        if n > t and n > s and 1 <= n <= 1000000000 :
            if s == t :
                return 0
            else :
                while cs <= s :
                    if s % cs == 0:
                        count_s.append( cs )  #taking the factors of s into a list
                    cs = cs + 1
                while ct <= t:
                    if t % ct == 0 :
                        count_t.append( ct )    #taking the factors of t into a list
                    ct = ct + 1
                for i in count_s :
                    for j in count_t :
                        if i == j :
                            return 1
                            
                        else :
                            mult = i * j
                            if mult <= n :
                                res.append( mult )
                
                if len( res ) == 0 :
                    return -1
                elif len( res ) > 0 :
                    return 2
                    
                
                
