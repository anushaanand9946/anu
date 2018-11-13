class Students:
    def __init__(self,x,y):
        self.name=x
        self.rollno=y
    def printdata(self):
        print("name ="+ str(self.name))
        print("name ="+ str(self.rollno))

    ##rollno=2

    def age(self,myage):
        print("age ",myage)

s=Students("anusha",22)
x=int(input("enter age"))

#print(s.name)
#print(s.rollno)
s.printdata()
s.age(x)