num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number:"))

result = num * num2

if result > 0:
    print("the result is positive.")
else result < 0:
    print("the result is negative.")
else:
    print("the result is zero.")

print(f"the result of multiplying {num1}and {num2} is: {result}")
