import primefac
class NonCoprimeGraph():
    def distance(self, n, s, t):
        if s == t:
            return 0
        elif (len(list(primefac.primefac(s))) == 1) and (len(list(primefac.primefac(t))) == 1) :
            return -1
        else:
            if primefac.gcd(s,t) > 1 :
                return 1
            else:
                length = len(set(primefac.primefac(s))) + len(set(primefac.primefac(t)))
                return length

