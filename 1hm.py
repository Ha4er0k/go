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
            raise ValueError("The phone number must contain exactly 10 digits.")
        super().__init__(value)

class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY.")
    
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
        raise ValueError("Phone not found.")
    
    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None
    
    def add_birthday(self, birthday):
        if not isinstance(birthday, Birthday):
            raise ValueError("Invalid birthday format.")
        self.birthday = birthday
    
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {self.birthday if self.birthday else 'Not set'}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
    
    def find(self, name):
        return self.data.get(name, None)
    
    def delete(self, name):
        if name in self.data:
            del self.data[name]
    
    def get_upcoming_birthdays(self):
        today = datetime.today()
        upcoming_birthdays = []

        for record in self.data.values():
            if record.birthday:

                birthday_this_year = record.birthday.value.replace(year=today.year)
                
                if birthday_this_year < today:
                    birthday_this_year = birthday_this_year.replace(year=today.year + 1)
                
                days_diff = (birthday_this_year - today).days

                if 0 < days_diff <= 7:
                    upcoming_birthdays.append((record.name.value, birthday_this_year.strftime("%d.%m.%Y")))
        
        return upcoming_birthdays

if __name__ == "__main__":
    book = AddressBook()
    
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    john_record.add_birthday(Birthday("10.04.1990"))
    book.add_record(john_record)
    
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    jane_record.add_birthday(Birthday("05.04.1985"))
    book.add_record(jane_record)
    
    for name, record in book.data.items():
        print(record)
    
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")
    print(john)
    
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")
    
    print("\nUpcoming birthdays:")
    upcoming = book.get_upcoming_birthdays()
    for name, birthday in upcoming:
        print(f"Upcoming birthday: {name} on {birthday}")

       
