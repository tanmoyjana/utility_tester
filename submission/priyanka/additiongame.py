class AdditionGame:
    def getMaximumPoints(self,A,B,C,N):
        sum = 0
        for i in range(0,N):
            num = max(A,B,C)
            if (num == A) and (A > 0):
                       A = A - 1
            elif (num == B) and (B > 0):
                       B = B - 1
            elif (num == C) and (C > 0):
                       C = C - 1
            sum = sum + num
        return sum
                
