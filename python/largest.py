
num1=int(input("enter a number1"))
num2=int(input("enter a number2"))
num3=int(input("enter a number3"))

if(num1>num2 and num1>num3):
    print("largest is num1",num1)
elif(num2>num1 and num2>num3):
     print("largest is num2",num2)
elif(num3>num1 and num3>num2):
    print("largest is num3",num3)
else:
    print("error")

