class MyParent: #base class
    #1.1 property
    bloodGroup='AB+'

    #1.2 constructor 

    #1.3 method

class MyChild(MyParent): # derived class
    #1.1 property

    #1.2 constructor

    #1.3 method    
    def getMyBloodGroup(self):
        print(f"My blood group is {self.bloodGroup}")

# create classs object 
#we always create object of child class
co = MyChild()
co.getMyBloodGroup()        