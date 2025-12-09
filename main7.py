# 1. მოცემულია სია:

# (სახელი, გვარი, ასაკი)

persons = [
    ('Kelly', 'Simpson', 26),
    ('Erika', 'Stephens', 24),
    ('Cheryl', 'Dunn', 30),
    ('Amy', 'Larsen', 49),
    ('Christine', 'Gordon', 23),
    ('Monica', 'Huff', 38),
    ('David', 'Nixon', 36),
    ('Cindy', 'Escobar', 41),
    ('Cindy', 'White', 33), 
    ('Joel', 'Hall', 43),
    ('Steven', 'Winters', 28),
    ('Alex', 'Cole', 68),
    ('Alex', 'Smith', 32),
    ('Brittany', 'Thompson', 18),
    ('Ernest', 'Young', 43),
    ('Traci', 'Wells', 38),
    ('Andrew', 'Flores', 61),
    ('Christopher', 'Lewis', 29),
    ('Kevin', 'Willis', 57),
    ('Kayla', 'Lucas', 28),
    ('Michelle', 'Rush', 43),
    ('Thomas', 'Mason', 37)
]

# დაწერეთ უსასრულო ციკლი, რომელშიც მომხმარებელს ჰკითხავთ სახელს, თუ სახელი იქნება მოცემულ სიაში, შემდეგ ჰკითხეთ გვარი და გვარიც თუ იქნება,
# დაბეჭდეთ მისი ასაკი, ხოლო თუ არ იქნება სახელი დაბეჭდეთ რომ არ არის მოცემული სახელი, შესაბამისად გვარი აღარ ჰკითხოთ, ანალოგიურად
# მოიქეცით გვარის კითხვის შემთხვევაშიც. ციკლი უნდა გაჩერდეს იმ შემთხვევაში თუ მომხმარებელი შემოიყვანს სიტყვას "stop".

# 2. დაწერეთ პროგრამა, რომელიც მომხმარებელს შემოაყვანინებს ჯერ პირველ და მერე მეორე სიტყვას.
#    იპოვეთ ამ სიტყვებში საერთო სიმბოლოები, განსხვავებული სიმბოლოები, და გაერთიანებული სიმბოლოები(ანუ ორივეში ერთად რომელიცაა ყველა ერთად)
#    დაბეჭდეთ ყველა ზემოთჩამოთვლილი(გამოიყენეთ set)

while True:
    name = input("enter a name: ").lower()

    if name == "stop" :
        break

    found_persons = []

    for person in persons:
        if name == person[0].lower():
            found_persons.append(person)

    if found_persons:
        last_name = input("enter a last name: ").lower()

        for person in found_persons:
            if last_name == person[1].lower():
                print(f"{person[0]} {person[1]} is {person[2]} years old.")
                break

        else:
            print("no last namde found")
    else:
        print("No name found")