import itertools 
class OddEvenTree():
    def getTree(self, y):
        x = list(itertools.combinations(range(0,len(y)),2))
        c = []
        for v in x:
            if y[v[0]][v[1]] == y[v[1]][v[0]]: 
                c.append(v)
        return list(itertools.chain.from_iterable(c))
