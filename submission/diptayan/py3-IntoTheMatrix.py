class IntoTheMatrix (): 

    def takePills(self ,turns , N)  :
        friend = 0
        total = 1
        while N > total:
            friend = friend + 1
            total = total * (turns + 1 )
        return friend
