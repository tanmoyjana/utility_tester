class AccountBalance():
    def processTransactions(self,startingBalance,transactions):
        for k in transactions:
            j= k.split(" ")
            if j[0]== "C":
                startingBalance= int(startingBalance) + int(j[1])
            elif j[0]== "D":
                startingBalance= int(startingBalance) - int(j[1])
        return startingBalance
