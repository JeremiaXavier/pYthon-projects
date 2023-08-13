class BaseClass:
    def __init__(self):
        print("Base constructor invoked")

    def read(self,name,age,admno):
        self.name = name
        self.age = age
        self.admission_no = admno




class Sports(BaseClass):
    def __init__(self):
        print("derived Constructor invoked")
    def read_score(self,score):
        self.score = score

    def print(self):
        print("Name: " + self.name)
        print("Age: " + str(self.age))
        print("admissiom no: " + str(self.admission_no))
        print("Sports Score: "+str(self.score))


jeremia = Sports()

jeremia.read("jeremia",19,2427)
jeremia.read_score(234)
jeremia.print()

