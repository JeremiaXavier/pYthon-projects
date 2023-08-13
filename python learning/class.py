#class MySampleClass:

    #def get_name(self, name):
      #  self.name = name                # self is used as this pointer in case of cpp


    #def print_name(self):
     #   print("hello "+self.name)




#x = MySampleClass()
#y= MySampleClass()

name = "jeremia"
#x.get_name(name)
#x.print_name()

#y.get_name("jino")

#y.print_name()

name = "dilshad"
age = 21


class ForConstructor:
    year = 2023
    #Above is class variable

    def __init__(self, name, age, place):  #Constructor
        self.name = name
        self.age = age    #self.variable name is the datamember of class
        self.place = place

    def get_details(self):
        print("Name: "+self.name)
        print("Age: "+str(self.age)) #we can only concatenate string not intger variables so we need to convert into string
        print("Place: "+self.place)
        print("Year: "+str(ForConstructor.year))

    def add_age(self):
        self.age = self.age+1

    def relocate(self,place):
        self.place = place

    @classmethod                # This is an annotation for creating class method or similar to static function
    def add_year(cls):
        cls.year=cls.year+1
        print("Class method")
        print(cls.year)






x = ForConstructor("jeremia",21,"vannappuram")


x.get_details()
x.add_age()
print("After a year age increases by 1")

x.get_details()
x.relocate("calicut")
print("----------------------------------------------------")
x.get_details()
ForConstructor.year=ForConstructor.year+1

ForConstructor.add_year()

