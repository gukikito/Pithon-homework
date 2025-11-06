# 1. დაწერეთ პროგრამა, რომელიც მომხმარებელს შემოაყვანინებს წინადადებას, პირველ სიტყვას და მეორე სიტყვას და 
# შემოყვანილ წინადადებაში პირველ სიტყვას ჩაანაცვლებს მეორე სიტყვით
sentence = input("შეიყვანეთ წინადადება: ")
word1 = input("შეიყვანეთ  პირველი სიტყვა:" )
word2 = input("შეიყვანეთ  მეორე სიტყვა:" )
new_sentence = sentence.replace(word1, word2)
print (new_sentence)

# 2. დაწერეთ პროგრამა, რომელიც მომხმარებლის მიერ შემოყვანილ წინადადებაში 
# იპოვის ყველაზე გრძელ სიტყვას და დაბეჭდავს მას. არ გამოიყენოთ max() ფუნქცია!
# sentence = input("შეიყვანეთ წინადადება: ")
words = sentence.split()
longest_word = ""
longest_length = 0
for word in words:
    if len(word) > longest_length:
        longest_length = len(word)
        longest_word = word
print("ყველაზე გრძელი სიტყვაა: ", longest_word)        

