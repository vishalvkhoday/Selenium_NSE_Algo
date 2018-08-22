'''
Created on Jun 8, 2018

@author: khoday
'''

import random
import math




one_to_ten = list(range(10))

for i in one_to_ten:
    print i
    
rand_list =["String",333,"come soon","outting","String"]

comb_list = rand_list + one_to_ten

first3 = comb_list[0:3]

for i in first3:
    print ("{} : {}".format(first3.index(i),i))
    
print ("String" in first3)

print ("Count ",first3.count("String"))

x=0
#rand_name =""
j=0
Name_list = []
for j in(range(150)):
    rand_name=""         
    for x in range(8):        
        alpha_list ="abcdefghijklmnopqrstuvwxyz"
        ran_alpha = random.randint(0,25)
        rand_name =rand_name + alpha_list[ran_alpha]
    print rand_name.capitalize()
    Name_list.append(rand_name.capitalize())
    
print ('*--*--' * 15)

for names in Name_list:    
    print str("{}   {}".format(Name_list.index(names)+1,names))
    


