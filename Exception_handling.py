'''
Created on Jun 5, 2018

@author: khoday
'''


while True :
    try:
        Int_Number = int(input("Enter an number : "))
        if Int_Number == 7:
            print ("You guessed it")
            break
        else:
            print ("Wrong number guessed!!!")
        
    except:
        print(" You did not enter a number")
        

