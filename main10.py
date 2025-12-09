# 1. გამოიყენეთ lambda ფუნქცია sorted() ფუნქციაში, იმისათვის რომ დაასორტიროს მოცემული ლისტი:
#    [(1, 3), (4, 2), (2, 5)] - მასში არსებული ელემენტების მეორე ელემენტის მიხედვით
# numbers = [(1, 3), (4, 2), (2, 5)]
# sorted_list = sorted(numbers, key=lambda x: x[1])
# print(sorted_list)


# 2. დაწერეთ ფუნქცია, რომელსაც გადაეცემა სამი პარამეტრი. დააგენერირეთ ლისტი: 
# პირველი პარამეტრი გამოიყენება ლისტის სიგრძედ, რომელშიც იქნება შემთხვევითი რიცხვები მეორე 
# პარამეტრიდან მესამე პარამეტრამდე. ამავე ფუნქციაში მომხმარებელს შეაყვანინეთ ინდექსი და არსებული 
# ლისტიდან ამ ინდექსის მიხედვით დააბრუნეთ ელემენტი. დაიჭირეთ ერორები: 1. თუ ინდექსი არარსებობს დააბრუნეთ შესაბამისი პასუხი. 
# 2. თუ ინდექსი არარის რიცხვი - შესაბამისი პასუხი. 3. ზოგადი ერორიც შეგიძლიათ დაიჭიროთ.
# (ჩავთვალოთ რომ ამ კონკრეტულ ფუნქციას არგუმენტები გადაეცემა სწორად).

# import random
# def random_list(length, start, end):
#     lst = [random.randint(start, end) for _ in range(length)]
#     print (lst)
#     try:
#         index = int(input("Enter index: "))
#         print("this index element is: ", lst[index])
#     except IndexError:
#         print("Error: index not avalaible in this list.")   
#     except ValueError:
#         print("Error: index must be a number.")
#     except Exception as e:
#         print("general error: ", e)    

    


# 3. მოცემულია პროდუქტების ლისტი:
# from functools import reduce
# products = [
#     {"name": "Laptop", "price": 1200},
#     {"name": "Mouse", "price": 15},
#     {"name": "Keyboard", "price": 25},
#     {"name": "Monitor", "price": 150},
#     {"name": "Power", "price": 100},
#     {"name": "Pad", "price": 10},
# ]
# cheap_products = list(filter(lambda p: p["price"] < 100, products))
# print("100 ლარზე ნაკლები: ", cheap_products)

# products_info = list(map(lambda p: (p["name"], p["price"]),products))
# print("სახელი და ფასი: ", products_info)

# sorted_products = sorted(products, key=lambda p: p["price"])
# print(" დალაგებულია ფასების მიხედვით: ", sorted_products)

# total_price = reduce(lambda acc, p: acc + p["price"], products, 0)
# print("ფასების ჯამი: ", total_price)


# filter() ფუნქციის გამოყენებით გაფილტრეთ და გამოიტანეთ პროდუქტები, რომლის ფასი ნაკლებია 100-ზე;
# map() ფუნქციის გამოყენებით გამოიტანეთ ყველა პროდუქტის სახელი და ფასი
# sorted() ფუნქციის გამოყენებით დაასორტირეთ პროდუქტების სია ფასის მიხედვით
# reduce() ფუნქციის გამოყენებით გამოიტანეთ ყველა პროდუქტის ფასების ჯამი






# 4. დაწერეთ რეკურსიული ფუნქცია, რომელსაც პარამეტრად გადაეცემა რიცხვი და დააბრუნებს 1-დან ამ რიცხვის ჩათვლით ყველა რიცხვის ჯამს
# def recursive_sum(n):
#     if n == 1:
#         return 1
#     else:
#         return n + recursive_sum (n-1)
# print(recursive_sum())