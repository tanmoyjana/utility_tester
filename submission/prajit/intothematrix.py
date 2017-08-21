class IntoTheMatrix():
    def takePills(self,turns,N):
        F=0
        i=1
        while i<N:
            F= F+1
            i = i*(turns+1)
        return F
