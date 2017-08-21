import itertools
class MealPlan():
    def countDistinct(self,morningMeal,noonMeal,eveningMeal, nightMeal):
        y =[list(morningMeal),list(noonMeal),list(eveningMeal),list(nightMeal)]
        z = [sorted(p) for p in itertools.product(*y)]
        
        return len(set(map(tuple,z)))

