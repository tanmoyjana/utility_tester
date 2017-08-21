class AccountBalance():
    def processTransactions( self , startingBalance , transactions ):
        t = list( transactions ) #converting the tuple to a list
        s = []
        credit = 0
        debit = 0
        result = 0
        for i in t:
            s = i.split(' ') #splitting the string when ' ' is found
            if s[0] == 'C' :
                credit = credit + int( s[1] )
            elif s[0] == 'D':
                debit = debit + int( s[1] )
        result = startingBalance + credit - debit
        return result
