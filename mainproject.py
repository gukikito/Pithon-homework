# ფუნქცია, რომელიც იღებს რიცხვს მომხმარებლისგან
def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Please enter a valid number!")


# ფუნქცია, რომელიც ირჩევს ოპერატორს (+, -, *, /)
def get_operator():
    allowed = {"+", "-", "*", "/"} #ნებადართული ოპერატორები
    while True:
        op = input("Choose operator (+, -, *, /): ")
        if op in allowed:  # თუ ოპერატორი ნებადართულია აბრუნებს
            return op
        print(" Invalid operator! Please choose one of (+, -, *, /)")


print("Welcome! I am your Calculator")
name = input("Dear customer, what is your name?: ")
print(f"Hello {name}, let's calculate something together!\n")


num1 = float(input("Enter first number: "))
op = get_operator()
num2 = float(input("Enter second number: "))

print()   


if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    if num2 == 0:
        print(" You can’t divide by 0!")  #ნულზე გაყოფისგან დაცვა
        result = None
    else:
        result = num1 / num2

if result is not None:
    print(f"Result: {result: .4f}") #შედეგის ჩვენება 4 ციფრის სიზუსტით

print("\nThank you for using the Calculator!")