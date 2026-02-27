#for loop
for i in range (1,20):
    if i ==13 :
        break
    else:        print(i)
    

#while loop
CALCULATOR = 1
while CALCULATOR == 1:
    print("Calculator is running.")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /): ")
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero is not allowed.")
            continue
    else:
        print("Invalid operation.")
        continue
    print("Result:", result)
    cont = input("Do you want to perform another calculation? (yes/no): ")
    if cont.lower() != "yes":
        CALCULATOR = 0
        print("Calculator is closing.")
    
#NOT WHILE LOOP
NUM=int(input("Enter a number: (press 0 if you want to exit)"))
while not NUM == 0:
    print("The number is positive.")
    NUM=int(input("Enter a number: (press 0 if you want to exit)"))
print("Exiting the program.")
        

    