# 1. დაწერეთ ფუნქცია, რომელიც პარამეტრად მიიღებს რიცხვს, თუ რამდენჯერ უნდა ჰკითხოს მომხმარებელს რიცხვი და საბოლოოდ დააჯამებს
#    ყველა შეყვანილ რიცხვს, თუ არგუმენტად არ გადაეცა არანაირი რიცხვი, მაშინ ფუნქციამ 5-ჯერ ჰკითხოს მომხმარებელს რიცხვის 
#    შეყვანა და დააჯამოს ეს 5 რიცხვი. დააბრუნეთ საბოლოო ჯამი

def sum_numbers(times=5) :
    total = 0
    for i in range(times) :
        num = float(input(f"Enter number: "))
        total += num
    return total    

result = sum_numbers()
print("SUM: ", result)




# 2. დაწერეთ ფუნქცია რომელიც მიიღებს არგუმენტების განუსაზღვრელ რაოდენობას მთელი რიცხვების სახით და დააბრუნებს
#    ორ ლისტს, ერთ ლისტში იქნება გადაცმული არგუმენტებიდან კენტი რიცხვები ხოლო მეორე ლისტში ლუწი რიცხვები

def split_even_odd(*args) :
    even = []
    odd = []
    for num in args :
        if num % 2 == 0:
            even.append(num)
        else: 
            odd.append(num)
    return even, odd       

even_list, odd_list = split_even_odd("*args: any")
print("even: ", even_list)
print("odd: ", odd_list)




# 3. დაწერეთ ფუნქცია, რომელსაც პარამეტრად გადაეცემა მომხმარებლის მიერ შეყვანილი წინადადება და ამ წინადადებაში დაითვლის სიტყვებს
#    და დიქტის სახით დააბრუნებს თუ რომელი სიტყვა რამდენჯერ არის, მაგ: "This is a test. This test is fun." --> დააბრუნებს დიქტის
#    შემდეგი სახით: {'this': 2, 'is': 2, 'a': 1, 'test': 2, 'fun': 1} უნდა იყოს case insensitive (ანუ დიდ და პატარა ასოებს არ უნდა
#    ჰქონდეს მნიშვნელობა!)

def word_count(sentence): 
    sentence = sentence.lower()
    for i in ".,!?;:" :
        sentence = sentence.replace(i, "")

    words = sentence.split()

    word_dict = {}
    for word in words: 
        word_dict[word] = word_dict.get(word, 0) +1
    return word_dict      
   
text = input("enter sentence: ")
result = word_count(text)
print(result)