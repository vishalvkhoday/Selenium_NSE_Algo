'''
Created on Jun 18, 2018

@author: khoday
'''

class Square:
    
    def __init__(self,height=0,width=0):
        self.height =height
        self.width=width
        
    @property
    def height(self):
        print ("Reteriving data pls wait...")
        return self.__height
    
    @height.setter
    def height(self,value):
        
        if value.isdigit():
            self.__height = value
            
        else:
            print("Enter value in number")
            
    @property
    def width(self):
        print ("Reterving value from user ...")
        return self.__width
    
    @width.setter
    def width(self,value):
        if value.isdigit():
            self.__width = value
    
    def getArea(self):
        
        return int (self.__height) * int(self.__width)
    
def main():
    aSquare = Square
    height = input("Enter height : ")
    width = input("Enter width : ")
    
    aSquare.height = height
    aSquare.width = width
    
    print("Height : ", aSquare.height)
    print("Widht : ", aSquare.width)
    
    print ("Area = ",aSquare.getArea())
        

main()