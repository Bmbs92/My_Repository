#create a class
class Transport:
    def __init__(self,name,space,speed): #add atributions to the class
        self.name=name
        self.space=space
        self.speed=speed
    
    def description(self): #create a method for the class transport
        print('The {} goes at {} on {}.'.format(self.name,self.speed,self.space))
    
#Create a second class
class Airtransport(Transport): #By adding "Transport", the class Airtransport inherit the methods from the father class
    def __init__(self,name,speed,space,tipo):
        super().__init__(name,space,speed) #with the function super() the child class inherits the father's attributes
        self.tipo=tipo #you can still add more attributes to the child
    
    def location(self):
        print('Mostly, {}s are the airport.'.format(self.name))
    
    def passengers(self,number): #add a parameter "number"
        print('The {} {}, can take {} passengers.'.format(self.tipo,self.name,number))
    
#Create an object of the class Airtransport
airplane=Airtransport('airplane','800 km/hr','air','commercial')

airplane.location() #execute the method form the class Airtransport
airplane.description() #execute the method from the father class Transport
airplane.passengers(80) #execute the method and add the parameter


