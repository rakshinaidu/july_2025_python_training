# class Person:
#     def __init__(self,name):
#         self.name=name

#     def print_name(self):
#         print(self.name)

# person=Person("SARA")
# person.print_name()        

#ENCAPSULATION

class Person:
    def __init__(self,name):
        self.name= name

    def setName(self,name):
        self.name= name

    def getName(self):
        return self.name


person=Person("SARA")
person.setName("SEENU")

r=person.getName()
print(r)

