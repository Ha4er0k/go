def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Give me name please."
        except KeyError:
            return "Contact not found."
        except Exception as e:
            return f"An error occurred: {e}"
    return inner


def parse_input(user_input):
    cmd, *args = user_input.split() 
    cmd = cmd.strip().lower()  
    return cmd, *args


@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        raise ValueError
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        raise ValueError
    name, phone = args
    if name in contacts:
        contacts[name] = phone  
        return "Contact updated."
    else:
        raise KeyError

@input_error
def show_phone(args, contacts):
    if len(args) != 1:
        raise ValueError
    name = args[0]
    return contacts.get(name, "Contact not found.")

@input_error
def show_all(contacts):
    if not contacts:
        raise IndexError
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

def main():
    contacts = {}  
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break  

        elif command == "hello":
            print("Hello, how can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            print(show_all(contacts))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
#hello - Виводить привітальне повідомлення.
#add [name] [phone] - Додає новий контакт з вказаним ім'ям та номером телефону.
#change [name] [new phone] - Змінює номер телефону існуючого контакту за вказаним ім'ям.
#phone [name] - Виводить номер телефону контакту, який відповідає вказаному імені.
#all - Виводить список усіх контактів у системі, разом з їх іменами та номерами телефонів.
#help - Показує список доступних команд і їх пояснення.
#close або exit - Завершує роботу програми та виводить повідомлення про завершення розмови.