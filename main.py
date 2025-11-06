# დავალება 1
a = int (input("ჩაწერეთ პირველი კათეტის სიგრძე"))
b = int (input("ჩაწერეთ მეორე კათეტის სიგრძე"))

#ჰიპოტენუზის სიგრძე 
hypotenuse = (a**2 + b**2) ** 0.5
print(hypotenuse)

# სამკუთხედის ფართობი
area = (a * b) / 2
print (area)

# დავალება 2

total_seconds = int(input("ჩაწერეთ წამების რაოდენობა"))
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds / 60

print(f"{total_seconds} , {hours} , {minutes} , {seconds}")