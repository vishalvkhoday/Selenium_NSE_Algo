'''
Created on Jun 6, 2018

@author: khoday
'''


def Get_prime(int_val):
    for i in range(2,int_val):
        if (int_val % i)==0:
            return False
        
    return True

def Max_prime(max_num):
    list_of_prime =[]
    for num in range(2,max_num):
        if Get_prime(num):
            list_of_prime.append(num)
    return list_of_prime
       

while True:
    
    try:
        int_prime = int(input('Enter value get prime value series: '))
        break
    except:
        print ("Entered value is not number")
list_of_prime = Max_prime(int_prime)

for prime in list_of_prime:
    print prime
    
    
def Sum_all(*args):
    sum1 =0
    for x in args:
        sum1 +=x
    return sum1

print Sum_all(1,2,3,4,5,6,7,8,9)