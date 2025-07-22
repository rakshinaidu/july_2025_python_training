# print("Rakshitha")
# a=input("Enter the number from 0-10:")
# print(a)

# if ( int (a)<10):
#     print("She is a child")
# else:
#     print("not a child")

# print("Enter the number:") 
# for i in range(int (a)+1) :
#      print(i)  

# a=("one","two","three")
# i=int(input("ENTER THE INDEX OF THE ELEMENET:"))
# if(i<len(a)-1):
#     print(a[i])
# else:
#     print("limit exceeded")    

# user_input=input("Enter text:")  
# with open("user_input.txt","w") as file:
#     file.write("user_input")
# print("input saved to file")    

from datetime import datetime
current_datetime=datetime.now()
filename=str(current_datetime).replace(":","-")
with open(filename+".txt","w") as file:
    file.write("user_input")
print("input saved to file")    
