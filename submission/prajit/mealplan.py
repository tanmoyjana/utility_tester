class MealPlan():
    def countDistinct(self,morningMeal,noonMeal,eveningMeal,nightMeal):
        list1= []
        i=0
        j=0
        k=0
        l=0
        for i in morningMeal:
            for j in noonMeal:
                for k in eveningMeal:
                    for l in nightMeal:
                        list1.append([i,j,k,l])
        list2=[]
        for a in list1:
            a=sorted(a)
            list2.append(a)
        list3=[]
        for b in list2:
            if b not in list3:
                list3.append(b)
        list2=list3
        return len(list3)
