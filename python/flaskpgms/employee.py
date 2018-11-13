class employee:
    def __init__(self,a,b,c,d):
         self.name=a
         self.code=b
         self.age=c
         self.salary=d

    def printresult(self):

        print("name="+str(self.name))
        print("code="+str(self.code))     
        print("age="+str(self.age))   
        print("salary="+str(self.salary)) 

p=employee("anusha",22,22,30000)
q=employee("anu",221,22,30000)
r=employee("sha",222,22,30000)
s=employee("an",223,22,30000)
t=employee("a",22422,30000)

p.printresult()
q.printresult()
r.printresult()
s.printresult()
t.printresult()
             













