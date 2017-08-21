class CrossWord:
    def countWords(self,board,size):
        final = 0
        for element in board:
             el = element.split('X')
             for chr in el:
                  if chr.count('.')== size:
                    final = final +1
        return final

