import random
number = random.randint(1, 100)
lives = 5
while lives > 0:
    choose = int(input("აირჩიე რიცხვი:"))
    if choose == number:
        print("სწორია!")
        break
    elif choose < number:
        print ("ჩემი რიცხვი უფრო მაღალია:)")
    else:
        print("ჩემი რიცხვი უფრო დაბალია:")

    lives -= 1
    print("დაგრჩა {lives} სიცოცხლე.")
    lives == 0
    print ("ამოგეწურა სიცოცხლეები")
    print ("საიდუმლო რიცხვი იყო: {number}")   