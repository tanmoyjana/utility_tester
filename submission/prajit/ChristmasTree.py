class ChristmasTreeDecoration():
    def solve(self,col,x,y):
        N= len(col)-1
        list1=[]
        list2=[]
        for a in x:
            list1.append(col[a-1])

        for b in y:
            list2.append(col[b-1])

        z=[]
        i=0
        while i<len(list1):
            if list1[i]!= list2[i]:
                z.append('yes')
            i=i+1

        M= len(z)
        if M>=N:
            return 0
        elif M<N:
            return N-M
