class AccountBalance():
    def processTransaction(self, startingBalance, transactions):
        a = 0
        b = 0
        for t in transactions:
            if(t.split(" ")[0] == "C"):
                a = a+(int(t.split(" ")[1]))
            else:
                b = b+(int(t.split(" ")[1]))
        return startingBalance+a-b
class AdditionGame():
    def getMaximumPoints(self, A, B, C, N):    
        totalpoints = 0
        for i in range(0, N):
            x = max(A, B, C)
            if (x >= 1):
                totalpoints = totalpoints+x
                if (x == A):
                    A = A-1
                elif (x == B):
                    B = B-1
                else:
                    C = C-1
                i = i+1
            else:
                x = max(A, B, C)
        return totalpoints
class ATaleOfThreeCities():
    def connect(self, ax, ay, bx, by, cx, cy):
        import math
        n1 = len(ax)
        n2 = len(bx)
        n3 = len(cx)
        dis = lambda x1, x2, y1, y2: math.sqrt((x1-y1)**2+(x2-y2)**2)
        dis1 = dis(ax[0], ay[0], bx[0], by[0])
        for i in range(0, n1):
            for j in range(0, n2):
                if(dis1 > dis(ax[i],ay[i],bx[j],by[j])):
                    dis1 = dis(ax[i],ay[i],bx[j],by[j])
        dis2 = dis(ax[0], ay[0], cx[0], cy[0])
        for i in range(0, n1):
            for j in range(0, n3):
                if(dis2 > dis(ax[i], ay[i], cx[j], cy[j])):
                    dis2 = dis(ax[i], ay[i], cx[j], cy[j])
        dis3 = dis(bx[0], by[0], cx[0], cy[0])
        for i in range(0, n2):
            for j in range(0, n2):
                if(dis3 > dis(bx[0], by[0], cx[0], cy[0])):
                    dis3 = dis(bx[0], by[0], cx[0], cy[0])
        return (dis1+dis2+dis3)-max(dis1, dis2, dis3)
class IntoTheMatrix():
    def takePills(self,turns,N):
        pass
            


            
