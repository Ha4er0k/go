import os  
from pathlib import Path  
from colorama import init, Fore, Style  

def print_directory_tree(directory, indent=""):
    try:
        #тут отримую список всіх файлів і папок у вказаній директорії,та сортую їх так щоб спочатку йшли папки а потім файли
        entries = sorted(Path(directory).iterdir(), key=lambda e: (not e.is_dir(), e.name.lower()))

        for entry in entries:
            if entry.is_dir():  #якщо це папка
                print(f"{indent}{Fore.BLUE}📂 {entry.name}{Style.RESET_ALL}")  #вивід синім кольором
                print_directory_tree(entry, indent + " ┃ ")  #виулик рекурсії для вмісту папки
            else:  #якщо це файл
                print(f"{indent}{Fore.GREEN}📜 {entry.name}{Style.RESET_ALL}")  #вивід зеленим кольором
    except PermissionError:
        #якщо немає доступу до директорії, вивід повідомлення буде червоним кольором
        print(f"{indent}{Fore.RED}Доступ заборонено: {directory}{Style.RESET_ALL}")

def main():
    init(autoreset=True) 

    directory = Path(r"C:/шлях/до/вашої/директорії") # замість /шлях/до/вашої/директорії треба вписати шлях до своєї директорії
    
    #перевірка,чи існує така директорія
    if not directory.exists():
        print(f"{Fore.RED}Помилка: Вказана директорія не існує!{Style.RESET_ALL}")
        return
    
    #перевірка,чи це дійсно директорія,а не файл
    if not directory.is_dir():
        print(f"{Fore.RED}Помилка: Вказаний шлях не є директорією!{Style.RESET_ALL}")
        return 

    #вивід назви директорії жовтим кольором
    print(f"{Fore.YELLOW}📦 {directory.resolve().name}{Style.RESET_ALL}")

    print_directory_tree(directory)

if __name__ == "__main__":
    main()
