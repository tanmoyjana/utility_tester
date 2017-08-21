class MealPlan() :
    def countDistinct( self , morningMeal , noonMeal , eveningMeal ,  nightMeal ) :
        plan = []
        sort_meal = []
        output = []
        for i in morningMeal :
            for j in noonMeal :
                for k in eveningMeal :
                    for l in nightMeal :
                        meal = [ i , j , k , l ]   #creating the combinations of mealplan
                        sort_meal = sorted( meal , key = int )  #sorting them acc. to their integer value
                        plan.append( sort_meal )
        for x in plan :
            if x not in output :
                output.append( x )   #appending only unique plans
        return len( output )
