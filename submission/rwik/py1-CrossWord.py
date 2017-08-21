class CrossWord():
    def countWords(self,board,size):
        N = len(board)
        num = 0
        for i in range(0,N):
            x = board[i].split("X")
            B = len(x)
            for j in range(0,B):
                p = x[j].count(".")
                if (p == size and size>= 2):
                    num += 1
        return num
            
