# num=input("Enter a number:")
# try:
#     if not num.isnumeric():
#         raise ValueError("It is not valid number")

# except ValueError as e:
#     print(e)
action = input("Enter an operator:")
num1=input("Enter a number:")
num2=input("Enter a number:")
try:
    if action =="add":
        res=int(num1)+int(num2);
        print("Result",res)
    elif action=="sub":
        res=int(num1)-int(num2);
        print("Result",res)
    elif action=="mult":
        res=int(num1)*int(num2);
        print("Result",res)
    elif action=="div":
        res=int(num1)/int(num2);
        print("Result",res)
    else:
        raise ValueError("It is  not a valid operator")
    

except ValueError as e:
    print(e)    

