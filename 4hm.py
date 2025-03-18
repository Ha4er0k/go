def parse_input(user_input):
    cmd, *args = user_input.split() #команда розбиває введений рядок на слова
    cmd = cmd.strip().lower()  #команда видаляє зайві пробіли і переводимо команду в нижній регістр
    return cmd, *args 

#функція для додавання контакту
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

#функція для зміни номера телефону існуючого контакту
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone  #оновлює номер
        return "Contact updated."
    else:
        return "Contact not found."

#функція для отримання номера телефону за ім'ям
def show_phone(args, contacts):
    name = args[0]
    return contacts.get(name, "Contact not found.")  

#функція для виведення всіх контактів
def show_all(contacts):
    if contacts:
        return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())  #команда формує список контактів
    return "No contacts found."

def main():
    contacts = {}  #порожній словник для контактів
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break  #вихід з циклу при командах "close" або "exit"

        elif command == "hello":
            print("Hello,how can I help you?")

        elif command == "add" and len(args) == 2:
            print(add_contact(args, contacts))  

        elif command == "change" and len(args) == 2:
            print(change_contact(args, contacts)) 

        elif command == "phone" and len(args) == 1:
            print(show_phone(args, contacts))

        elif command == "all":
            print(show_all(contacts))

        else:
            print("Invalid command.")  #якщо невідома команда

if __name__ == "__main__":
    main()

    
#команди для бота:
#hello = виводить привітання.
#add [name] [phone] = додає контакт.
#change [name] [new phone] = змінює номер контакту.
#phone [name] = виводить номер телефону.
#all = показує всі контакти.
#close/exit = завершує роботу