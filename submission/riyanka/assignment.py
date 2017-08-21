class CrossWord():
    def countWords(self,board, size):
        
        c=0
        for BOARD in board :
            x=BOARD.split("X")
        
            for element in x:
                y=element.count(".")
                if(y==size and size>=2):
                    c=c+1

        return c

    
class Abacus():
    def add(self,original, val):
        l=[]
        for w in original:
            l.append(9-w.index('---'))
            k=[]
            for i in str(int(''.join(map(str,l)))+val):
                s=int(i)
                x="---"
                value="o"*(9-s)+x+"o"*s
                k.append(value)
        return tuple(k)




class WordFind():
    def findWords(self, grid, wordList):
        pass

class EventOrder():
    def getCount(self, longEvents, instantEvents):
        pass
