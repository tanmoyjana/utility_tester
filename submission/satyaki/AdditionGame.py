class AdditionGame:

    def getMaximumPoints(self, A, B, C, N):

        gain = 0

        for i in range(N):

            chosen_number = max(A, B, C)

            print "\nGained score = ",chosen_number
            gain = gain + chosen_number

            if ((A == chosen_number) and (A > 0)) :

                A -= 1
            
            elif ((B == chosen_number) and (B > 0)):

                B -= 1
            

            elif ((C == chosen_number) and (C > 0)):

                C -= 1
            
                          
        print "\nFinal score gained = ",gain

               
               

               

    
