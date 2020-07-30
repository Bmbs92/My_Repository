import utils #import the module utils where the class Airtransport was created, hint: do not forget to save the module utils first

#Create an object of the class Airtransport
airplane=utils.Airtransport('airplane','800 km/hr','air','commercial')

airplane.location() #execute the method form the class Airtransport
airplane.description() #execute the method from the father class Transport
airplane.passengers(80) #execute the method and add the parameter

from utils import Airtransport #only import from utils the class Airtransport

#Create an object of the class Airtransport
helicopter=Airtransport('helicopter','400 km/hr','air','commercial')
helicopter.passengers(6) #execute the method and add the parameter