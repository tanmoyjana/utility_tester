class ImprovingStatistics():
    def howManyGames(self, played, won):
        x = (won*100/played)
        y = played*(x+1)/100
        return y