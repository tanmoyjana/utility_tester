class Abacus():
    def add(self, original, val):
        l1 = []
        l2 = []
        for i in original:
            a = i.split("---")
            b = a[1].count("o")
            l1.append(b)
            s1 = ''.join(str(e) for e in l1)
        original = int(s1) + val
        newlist = list(str(original))
        for k in newlist:
            thread = (9 - int(k))*"o"+"---"+int(k)*"o"
            l2.append(thread)
        return tuple(l2)
