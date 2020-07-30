#create a class
class Transport:
    def __init__(self,name,land,speed): #add atributions to the class
        self.name=name
        self.land=land
        self.speed=speed
    
    def description(self): #create a method for the class transport
        print('The {} goes at {} on {}.'.format(self.name,self.speed,self.land))


#create objects from the class Transport
car=Transport('car','ground','160 km/hr') #save the object in a variable call "car"
bike=Transport('bike','ground','20 km/hr')

#execute the method for each object created
car.description()
bike.description()
