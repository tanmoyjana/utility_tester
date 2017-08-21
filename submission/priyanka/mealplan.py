class MealPlan():
    def countDistinct(self,morningMeal,noonMeal,eveningMeal,nightMeal):
     meal = []
     if (morningMeal == noonMeal == eveningMeal == nightMeal):
        return 1
     else:
        for i in morningMeal:
            for j in noonMeal:
                for k in eveningMeal:
                    for l in nightMeal:
                        plan = [i,j,k,l]
                        meal.append(plan)
        s = []
        for n in meal:
            s.append(sorted(n))  #sorting the meal list
        p = []
        for x in s:              #appending the same mealplans in another list 
            if x in p:
                continue
            else:
               p.append(x)
        return len(p)            #no of unique plans are taken                       
                            
                        
                        
