print("Simple Calculator")

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    answer = num1 + num2

elif operator == "-":
    answer = num1 - num2

elif operator == "*":
    answer = num1 * num2

elif operator == "/":
    if num2 == 0:
        answer = "Cannot divide by zero"
    else:
        answer = num1 / num2

else:
    answer = "Invalid operator"

print("Answer:", answer)