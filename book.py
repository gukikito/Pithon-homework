
# Book კლასი

class Book:
    def __init__(self, title, author, year):
        
        self._title = title
        self._author = author
        self._year = year

    # Getter მეთოდები 
    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def year(self):
        return self._year

    # ობიექტის ფორმატირება
    def __str__(self):
        return f"{self.title} - {self.author} ({self.year})"


# BookManager კლასი
class BookManager:
    def __init__(self):
        # სია წიგნების შესანახად
        self._books = []

    # წიგნის დამატება
    def add_book(self, book: Book):
        for existing in self._books:
            if (existing.title.lower() == book.title.lower() and
                existing.author.lower() == book.author.lower() and
                existing.year == book.year):

                print("ასეთი წიგნი უკვე დამატებულია!")
                return 
        self._books.append(book)
        print("წიგნი წარმატებით დაემატა!")

    # ყველა წიგნის დაბრუნება 
    def get_all_books(self):
        return self._books

    # წიგნის ძებნა სათაურის მიხედვით
    def find_by_title(self, title: str):
        title = title.lower()
        # search – თუ სიტყვა შედის სათაურში
        return [book for book in self._books if title in book.title.lower()]


# UserInterface კლასი
class UserInterface:
    def __init__(self, manager: BookManager):
    
        self.manager = manager

    # ტექსტის ვალიდაცია 
    def input_text(self, message):
        while True:
            value = input(message).strip()
            if value == "":
                print("გთხოვთ შეიყვანოთ ტექსტი!")
            else:
                return value

    # წლის ვალიდაცია – მხოლოდ დადებითი მთელი რიცხვი
    def input_year(self, message):
        while True:
            year = input(message).strip()

            # შემოწმება არის თუ არა მხოლოდ ციფრები
            if not year.isdigit():
                print("გთხოვთ შეიყვანოთ მხოლოდ რიცხვი!")
                continue

            year = int(year)

            # უარყოფითი წლის აკრძალვა
            if year < 0:
                print("წელი არ შეიძლება იყოს უარყოფითი!")
            else:
                return year

    # მენიუს არჩევანი – მხოლოდ დასაშვები ვარიანტები
    def input_menu(self, message, options):
        while True:
            choice = input(message).strip()
            if choice in options:
                return choice
            print("⚠ არასწორი არჩევანი, სცადეთ თავიდან.")

    

    # წიგნის დამატება
    def add_book_ui(self):
        print("\n=== ახალი წიგნის დამატება ===")

        # ვალიდირებული შეყვანა
        title = self.input_text("სათაური: ")
        author = self.input_text("ავტორი: ")
        year = self.input_year("გამოცემის წელი: ")

        # Book ობიექტის შექმნა
        new_book = Book(title, author, year)

        # BookManager-ში დამატება
        self.manager.add_book(new_book)

    # ყველა წიგნის ჩვენება
    def show_books_ui(self):
        print("\n=== წიგნების სია ===")
        books = self.manager.get_all_books()

        if not books:
            print("წიგნები არ არის დამატებული.")
            return

        # enumerate – ნომრების ჯგუფში წმენდა
        for i, book in enumerate(books, start=1):
            print(f"{i}. {book}")

    # წიგნის ძებნა სათაურის მიხედვით
    def search_book_ui(self):
        print("\n=== წიგნის ძებნა ===")
        keyword = self.input_text("სათაური: ")

        results = self.manager.find_by_title(keyword)

        if not results:
            print("წიგნი ვერ მოიძებნა.")
        else:
            print("ნაპოვნია წიგნები:")
            for book in results:
                print(book)

    

    def run(self):
        while True:
            print("\n წიგნების მართვის სისტემა ")
            print("1. წიგნის დამატება")
            print("2. წიგნების ნახვა")
            print("3. წიგნის ძებნა")
            print("4. გასვლა")

        
            choice = self.input_menu("აირჩიე ოპცია: ", ["1", "2", "3", "4"])

            
            if choice == "1":
                self.add_book_ui()
            elif choice == "2":
                self.show_books_ui()
            elif choice == "3":
                self.search_book_ui()
            elif choice == "4":
                print("პროგრამა დასრულდა.")
                break




def main():

    manager = BookManager()
    ui = UserInterface(manager)
    ui.run()

if __name__ == "__main__":
    main()