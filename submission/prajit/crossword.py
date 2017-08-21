class CrossWord():
    def countWords(self,board,size):
        num=0
        for k in board:
            j=k.split('X')
            for i in j:
                if i.count(".")==int(size):
                    num=num+1
        return num
