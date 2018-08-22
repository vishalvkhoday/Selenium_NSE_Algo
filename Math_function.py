'''
Created on Jun 6, 2018

@author: khoday
'''

import math

Sample_string = "This is the sample text to print"
print math.ceil(4.3)
print math.floor(4.4)
print math.fabs(-4.4)
print math.factorial(4)
print math.fmod(5,4)
print math.trunc(4.2)
print 20/4
a =3.0
b=2
print (type(a))
print (type(b))
print (type('2'))

try :
    print int('t')
except:
    print ('Not an number')
    
for char in Sample_string:
    print char
    
for i in range(0,len(Sample_string)-1,2):
    print (Sample_string[i]+Sample_string[i+1])

print chr(65)
print ord('A')


msg = raw_input("Enter message ")


tem_msg = ""
tem_cod = ""
for j in msg:
    
    tem_msg +=str(j)
    tem_cod += str(ord(j))
    
print tem_msg
print tem_cod


age = int(input('Enter age : '))

if (age == 5):
    print ("Go to kinder garder")
elif (age >= 6) and (age <=17):
    print ("Goes to {} grades".format(age-5))

else:
    print("Goto College")