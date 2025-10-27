class Bank:#case sensitive , indentation
    def __init__(self,name,balance,pin):
        self.__name=name #when you create attribute with self. then that attribute will be considered as public attribute
        self._balance=balance#using class method we can access it
        self.pin=pin        
    def printdata(self):
            print(self.__name)  
    def __print_data(self):#private method
         print(self.__name) 
         print(self.balance) 
         print(self.pin)         
    def method1(self):
         self.__print_data()    #when you create object of a class then that class can also acess attribute 
obj1=Bank("KRUPALI",10000,"abc")
obj1.method()
#obj1.printdata()
#print(obj1.name)#__ by giving "double underscore" attribute will become private
#name cannot access by the object now 
#Derived class cannot access 
#protected the varible or attribute only derived class or class object or method can access
#how to create _ only one 
obj1.__print_data()# private method cannot be accessed by this object of the class
#to access that create one method to acess that 