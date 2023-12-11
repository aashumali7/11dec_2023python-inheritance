#1. Class defination
class Car:
    #1.1 Property = variable
    name="Harrier"
    brand="TATA"
    model="2024"  #variable
    color="black"
    #1.2 Constructor


    #1.3 Method /Function 
    def getMyBrand(self): #camelCase
        #self is internal class object
        print(f'Brand name is {self.name}')
        print(f'Brand is {self.brand}')
        print(f'Model year is {self.model}')
        print(f'Model color is {self.color}')

#2. create class object
#classObject = ClassName()
#co is external class object
co = Car()

#call the method with classObject
co.getMyBrand()