# შექმენით Student კლასი
# კლასს უნდა გააჩნდეს შემდეგი ატრიბუტები:
# status, ნაგულისხმევად უნდა იყოს True
# pay რომელიც იქნება 1000

# არსებული კლასის ინსტანსს უნდა გააჩნდეს შემდეგი ატრიბუტები:
# first_name(ტექსტური), last_name(ტექსტური), age(ინტეჯერი), grades(სია, რომელშიც რამდენიმე ქულა იქნება)

# დაუმატეთ შემდეგი მეთოდები:
# get_full_name - რომელიც დააბრუნებს სახელს(first_name) და გვარს(last_name) ერთად, სფეისით დაშორებულს
# get_discount - თუ ინსტანსის ასაკი იქნება 18 წელზე ნაკლები, გადასახადი(pay) შემცირდეს 20%-ით
# calculate_average - დააბრუნებს საშუალო ქულას grades სიაზე დაყრდნობით
# get_status - თუ საშუალო ქულა(calculate_average) მეტი იქნება 90-ზე, დააბრუნებს "Excellent", თუ 90-სა და 70-ს შორის არის,
# დააბრუნებს "Good", თუ 70-სა და 50-ს შორის დააბრუნებს "Average", ხოლო 50ზე ნაკლები თუა, დააბრუნებს "Poor" და status
# ატრიბუტიც უნდა შეიცვალოს და გახდეს False





class Student:
    status = True
    pay = 1000
  
    def __init__(self, first_name, last_name, age, grades):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.grades = grades

    def get_full_name(self) :
        return f"{self.first_name} {self.last_name}"  
    
    def get_discount(self):
        if self.age < 18:
            self.pay = self.pay * 0.8
        return self.pay
    
    def calculate_average (self):
        if len(self.grades) == 0:
            return 0
        return sum (self.grades) / len(self.grades)
    
    def get_status(self):
        avg = self.calculate_average()

        if avg > 90:
            return "Exellent"
        elif 70 < avg <= 90:
            return "good"
        elif 50 < avg <= 70:
            return "Average"
        else :
            self.status = False
            return "poor"

student1 = Student()
print(student1.get_full_name())
print(student1.get_discount())
print(student1.calculate_average())        
print(student1.get_status())
print(student1.status)