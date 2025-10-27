#Constructor All classes hae a funtion called _init_(), which is always executed when the class is being initiated
#creating class
class Student:
    def init(self, fullname):
     self.name=fullname
s1=Student()
print(s1.name)