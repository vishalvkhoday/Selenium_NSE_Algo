'''
Created on Jun 12, 2018

@author: khoday
'''


#   
# Per_Dict = {"Fname":"Vishal","Lname":"Khoday","Address":"Mysore road byataraynpura"}
#   
# print Per_Dict
#   
# Per_Dict["Address"]="chamrajpet VVpuram"
#   
# for i,j in Per_Dict.items():
#     print (i,j)
#       
# print (Per_Dict.values())
# print (Per_Dict.keys())
#   
# print (Per_Dict["Address"].capitalize())
# print (Per_Dict.get("Fname","Nothere"))
#   
# Emp =[]
#   
# fname,lname = raw_input("Enter name ").split()
#   
# Emp.append({"fname" : fname,"lname":lname})


# 
# Cust_details =[]
# 
# while True:
#     Entries    = raw_input("Do you want to add new customer details: ")
#     
#     if Entries == "n":
#         break
#     else:
#         First_name,Last_name = raw_input("Enter Cust name: ").split()
# #         Last_name  = raw_input("Enter Cust Lname: ")
#         int_age    = raw_input("Enter age: ")
#         Cust_details.append({"fname" : First_name,"Lname":Last_name,"age" : int_age})
#         
# for cust in Cust_details:
#     print (cust["fname"],cust["Lname"],cust["age"])


def factorial (num):    
    if num <=1:
        return 1
        
    else:
        num = num*factorial(num -1)
        return num


def fib(n):
    if n == 0:
        return 0
    elif n==1:
        return 1
    else:
        res = fib(n-1)+ fib(n-2)
        print res
        return  res
    
print fib(6)

    
    
print (factorial(4))
    