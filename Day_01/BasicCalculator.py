# We are trying to create a basic calculator:- 

print("Welcome to My Calculator !")
print("Please Choose The Operation You Like To Perform:-")
print("1. Addition " \
"2. Subtraction " \
"3. Multiplication " \
"4. Division " \
"5. Exponent " \
"6. Remainder ")

user_choice = int(input("Enter Your Choice: "))

if(user_choice == 1):
    print("You have chosen Addition")
    num1 = int(input("Enter The First Number: "))
    num2 = int(input("Enter The Second Number: "))
    print(f"Your Sum is: {num1 + num2}")
    print("Thanks For Using The Calculator")

elif(user_choice == 2):
    print("You have chosen Subtraction")
    num1 = int(input("Enter The First Number: "))
    num2 = int(input("Enter The Second Number: "))
    print(f"Your Difference is: {num1 - num2}")
    print("Thanks For Using The Calculator")

elif(user_choice == 3):
    print("You have chosen Multiplication")
    num1 = int(input("Enter The First Number: "))
    num2 = int(input("Enter The Second Number: "))
    print(f"Your Product is: {num1 * num2}")
    print("Thanks For Using The Calculator")

elif(user_choice == 4):
    print("You have chosen Division")
    num1 = int(input("Enter The First Number: "))
    num2 = int(input("Enter The Second Number: "))
    print(f"Your Division is: {num1 / num2}")
    print("Thanks For Using The Calculator")

elif(user_choice == 5):
    print("You have chosen Exponent")
    num1 = int(input("Enter The First Number: "))
    num2 = int(input("Enter The Second Number: "))
    print(f"Your Exponent is: {num1 ** num2}")
    print("Thanks For Using The Calculator")

elif(user_choice == 6):
    print("You have chosen Remainder")
    num1 = int(input("Enter The First Number: "))
    num2 = int(input("Enter The Second Number: "))
    print(f"Your Remainder is: {num1 % num2}")
    print("Thanks For Using The Calculator")

else:
    print("Invalid Input Please Try Again.....")