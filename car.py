class car():
    def __init__(self):
        print "Car is idle"
    
    
    def Drive(self):
        print "Car is driving now!!!"
        
        
    def startEngin(self):
        print "Engine started!!!"
        
    def turnOff(self):
        print "Turn off the engine !!!"
 
    
 
newcar = car()

newcar.Drive()
print "\n"

newcar.startEngin()
print "\n"

newcar.turnOff()

print isinstance(newcar,car)

print car()