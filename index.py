# Take 3 numbers from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
# create a function with 3 parameters
def maxOfNum(num1,num2,num3):
    # checking which number is bigger
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
    
# save function in a variable
maximum = maxOfNum(num1,num2,num3) 
# show the bigger number to user 
print("   Max Number Is",maximum)      
    