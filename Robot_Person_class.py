'''
Created on Aug 7, 2018

@author: khoday
'''

class Robot:
#     Name = None
#     LastN = None
#     Height = 0
    
    def __init__(self,Name="",LastN="",Height=0):
        self.Name =Name
        self.LastN=LastN
        self.Height=Height
        
    def introduct(self): #,Name,LastN,Height
        print("Hello I am {} & my LastName  {} and height {}".format(self.Name,self.LastN,self.Height))
     
    
       
class Office:
#     location =None
#     department=None
#     pin=0
#     Personal=None
    
    def __init__(self,location="",department="",pin=0,): #Personal=""
        self.location=location
        self.department=department
        self.pin=pin
#         self.Personal
        
    def Work(self):
        print ("My currently location {} i am working in {} department at pincode {}".format(self.location,self.department,self.pin))
    
    def eligible(self,obj):
        if obj.Height > 20:
            return obj
        else:
            return "Not eligible"
    
R1 = Robot("Vishal","Khoday",56)
W1 = Office("EC","Testing",999)

print R1.introduct() #
print W1.Work()
W1.Personal =R1
print W1.Personal.introduct()
str_Person = W1.eligible(R1)
print W1.Personal.Name
 
if str_Person =="Not eligible":
    print str_Person
else:
    if len(str_Person.Name.strip()) ==0:
        print ( "Name cant be blank")
        raise NameError
    else:        
        print str_Person.LastN
        print str_Person.Height