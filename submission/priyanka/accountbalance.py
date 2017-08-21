class AccountBalance:
    def processTransactions(self, startingBalance, transactions):
        l = list(transactions)
        c = 0
        d = 0
        f = 0
        n = []
        for i in l:
            n.append(i.split(' '))
        for j in n:
            if (j[0]=='C'):
                c = c + int(j[1])
            elif (j[0]=='D'):
                d = d +int(j[1])
            
        f = startingBalance + c  - d   
        return f
