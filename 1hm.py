import pickle
from collections import UserDict
from datetime import datetime, timedelta

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if not (value.isdigit() and len(value) == 10):
            raise ValueError("Phone number must contain exactly 10 digits.")
        super().__init__(value)

class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
    
    def __str__(self):
        return self.value.strftime("%d.%m.%Y")

class Record:
    def __init__(self, name):
        self.name = Name(name)  
        self.phones = []
        self.birthday = None
    
    def add_phone(self, phone):
        self.phones.append(Phone(phone))
    
    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]
    
    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                self.phones.remove(p)
                self.phones.append(Phone(new_phone))
                return
        raise ValueError("Phone number not found.")
    
    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None
    
    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)
    
    def __str__(self):
        birthday_str = f", birthday: {self.birthday}" if self.birthday else ""
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}{birthday_str}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
    
    def find(self, name):
        return self.data.get(name, None)
    
    def delete(self, name):
        if name in self.data:
            del self.data[name]
    
    def get_upcoming_birthdays(self):
        today = datetime.today().date()
        upcoming_birthdays = []
        
        for record in self.data.values():
            if record.birthday:
                birthday_date = record.birthday.value.date()
                birthday_this_year = birthday_date.replace(year=today.year)
                if birthday_this_year < today:
                    birthday_this_year = birthday_this_year.replace(year=today.year + 1)
                
                days_until_birthday = (birthday_this_year - today).days
                if 0 <= days_until_birthday < 7:
                    upcoming_birthdays.append((record.name.value, birthday_this_year.strftime("%d.%m.%Y")))
        
        return upcoming_birthdays
    
    def show_all_contacts(self):
        if not self.data:
            return "No contacts available."
        return "\n".join(str(record) for record in self.data.values())

# Серіалізація: Збереження даних у файл
def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

# Десеріалізація: Завантаження даних з файлу
def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()  # Повертаємо нову книгу, якщо файл не знайдено

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, IndexError) as e:
            return str(e)
    return wrapper

@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message

@input_error
def add_birthday(args, book):
    name, bday = args
    record = book.find(name)
    if record:
        record.add_birthday(bday)
        return f"Birthday added to {name}."
    return "Contact not found."

@input_error
def show_birthday(args, book):
    name = args[0]
    record = book.find(name)
    if record and record.birthday:
        return f"{name}'s birthday is {record.birthday}"
    elif record:
        return f"No birthday set for {name}."
    return "Contact not found."

@input_error
def birthdays(args, book):
    results = book.get_upcoming_birthdays()
    if not results:
        return "No upcoming birthdays."
    return "\n".join([f"{name}: {date}" for name, date in results])

def parse_input(user_input):
    parts = user_input.strip().split()
    return parts[0], parts[1:]

def main():
    # Завантажуємо дані з файлу
    book = load_data()

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            # Зберігаємо дані перед виходом
            save_data(book)
            break

        elif command == "hello":
            print("Hello, how can I help you?")

        elif command == "add":
            print(add_contact(args, book))

        elif command == "change":
            name, old_phone, new_phone = args
            record = book.find(name)
            if record:
                try:
                    record.edit_phone(old_phone, new_phone)
                    print("Phone updated.")
                except ValueError as e:
                    print(str(e))
            else:
                print("Contact not found.")

        elif command == "phone":
            name = args[0]
            record = book.find(name)
            if record:
                print(", ".join([p.value for p in record.phones]))
            else:
                print("Contact not found.")

        elif command == "all":
            print(book.show_all_contacts())  

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(birthdays(args, book))

        elif command == "show-contacts":  
            print(book.show_all_contacts())

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
