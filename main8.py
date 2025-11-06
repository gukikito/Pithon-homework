# 1. დაწერეთ ფუნქცია, რომელიც პარამეტრად მიიღებს მომხმარებლის მიერ შეყვანილ ტექსტს და ამ ტექსტში დათვლის რამდენი სიმბოლო იყო მაღალ რეგისტრში
#    შეყვანილი და ასევე ამ ტექსტს გადააქცევს uppercase-ად ანუ მაღალ რეგისტრში დააბრუნებს, მაგალითად, მომხმარებელმა თუ შეიყვანა ტექსტი
#    Hello woRld, ფუნქციამ უნდა დააბრუნოს რომ 2 დიდი ამ ტექსტში და ეს ტექსტი აქციოს HELLO WORLD-ად.


def count_upprcase_and_convert(text ):
    count = sum(1 for i in text if i.isupper())
    upper_text = text.upper()
    return count, upper_text

text = input("Enter text: ")
count, upper = count_upprcase_and_convert(text)
print (f"{count}capital letter")
print(f"{upper}")

# 2. დაწერეთ ფუნქცია, რომელიც პარამეტრად მიიღებს ე.წ. camel case ცვლადებს და დააბრუნებს snake case სახით, ანუ თუ გადავცემთ ცვლადს
#    firstName დააბრუნებს first_name, name დააბრუნებს ისევ name, preferredFirstName დააბრუნებს preferred_first_name, lastName დააბრუნებს
#    last_name და ასე შემდეგ.

def camel_to_snake(name) :
    result = ""
    for i in name: 
        if i.isupper() :
            result += "_" + i.lower()
        else:
            result += i
    return result 


print(camel_to_snake("firstName"))
print(camel_to_snake("preferredFirstName"))
print(camel_to_snake("lastName"))
print(camel_to_snake("name"))