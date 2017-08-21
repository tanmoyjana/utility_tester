class AdditionGame():
    def getMaximumPoints(self,A,B,C,N):
        X = 0
        num = 0
        while num!= N:
            Y = max(A,B,C)
            if Y == A:
                X= X + A
                A=A-1
            elif Y == B:
                X = X + B
                B = B - 1
            elif Y == C:
                X = X + C
                C= C- 1
            num = num + 1
        return X
