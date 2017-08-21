class CrossWord():
    def countWords(self,board,size):
        a=list(board)
        i=0
        b=[]
        count=[]
        result=0
        for p in a:
            b.append(list(p))
        for ll in b:
            d=0
            total=0
            for pp in ll:
                total= total + 1
                if pp=='.':
                    d=d+1
                    if total==len(ll):
                        count.append(d)
                    else:
                        continue
                elif pp=='x':
                    count.append(d)
                    d=0
        for t in count:
            if size == t:
                result=result+1
            else:
                continue
        return result
