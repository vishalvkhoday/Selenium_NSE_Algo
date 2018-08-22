class NameError(Exception):
    def __init__(self,*args,**kwargs):
        Exception.__init__(self,*args,**kwargs)
    
try:
    name = input('Enter name: ')
    if any(char.isdigit() for char in name):
        print str(name)
        raise NameError
    else:
        print ('Good name')
except:
    print('Name cant have numbers')

    