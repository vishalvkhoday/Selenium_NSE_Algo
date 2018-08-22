#!usr/bin/python

import os
import sys


class Animal:
    __name = None
    __height = 0
    __weight = 0
    __sound = 0
    
    
    def __init__(self,name,height,weight,sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound
    
    def set_name (self,name):
        self.__name =name
        
    def get_name(self):
        return self.__name
        
    def set_height(self,height):
        self.__height = height
        
    def get_height(self):
        return self.__height
    
    def set_weight(self,weight):
        self.__weight = weight
        
    def get_weight(self):
        return self.__weight
    
    def set_sound (self,sound):
        self.__sound = sound
        
    def get_sound (self):
        return self.__sound
    def getType(self):
        print ("Animal")
        
    def to_str(self):
        print "{} is  {} cm tall weights {} and sound {}".format(self.__name,self.__height,self.__weight,self.__sound)
        
        
cat = Animal('Wisker',33,4,'Meow')

print cat.to_str()

class Dog(Animal):
    __owner = ""
    
    def __init__(self,name,height,weight,sound,owner):
        self.__owner = owner        
        super(Dog,self).__init__(name, height, weight, sound)
        
    def set_owner(self,owner):
        self.__owner = owner
        
    def get_owner(self):
        return self.__owner
    
    def getType(self):
        print("Dog")
        
    def to_str(self):
        print "{} is  {} cm tall weights {} and sound {} & Owner is {}".format(self.__name,
                                                                               self.__height,
                                                                               self.__weight,
                                                                               self.__sound,
                                                                               self.__owner)
        
          
    def multiple_sound(self,how_many =None):
        if how_many is None :
            print(self.get_sound())
            
        else:
            print(self.get_sound()* how_many)
spot = Dog("Spot",33,10,"bark","Vishal")
print (spot.to_str())
            
super_Villain = {"Cement" : "Ambuja Cements","IT" : "Mindtree","Cement" : "Shree Cement","IT" : "Infosys","IT": "TCS",
                 "Textile": "ABFRL","Textile":"Alok Industry","Steel" :"Tata Steel"
                 }
print super_Villain.get("IT")
print (super_Villain.values())
print super_Villain.keys()
new_tup = list(super_Villain.keys())
print max(new_tup)
print min(new_tup)




