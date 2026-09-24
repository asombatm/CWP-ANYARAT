number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

result = 0
i = 0

while i < abs(number2):
    result += abs(number1)
    i += 1

if (number1 < 0 and number2 > 0) or (number1 > 0 and number2 < 0):
    result = -result

print(number1, "x", number2, "=", result)