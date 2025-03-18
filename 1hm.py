import os 

filename = "salary_file.txt"  #cтворив файл та дав йому ім'я

#перевірка, чи файл вже існує
if not os.path.exists(filename):  
    with open(filename, "w", encoding="utf-8") as file:  #("w") - відкриття файлу в режимі запису,"write"
        file.write("Alex Korp,3000\n")  
        file.write("Nikita Borisenko,2000\n")  
        file.write("Sitarama Raju,1000\n")  

def total_salary(path):
    try:
        #("r") - відкриття файлу в режимі читання
        with open(path, "r", encoding="utf-8") as file:
            #тут розділення за комою та перетворення зп на число
            salaries = [int(line.strip().split(",")[1]) for line in file if line.strip()]
        
        total = sum(salaries)
        
        #обчислення середьної зп,якщо список не порожній, інакше середнє = 0
        average = total / len(salaries) if salaries else 0
        
        return total, average

    #виведе помилку в разі якщо файл не знайдено
    except FileNotFoundError:
        print("Помилка: Файл не знайдено.")  
        return 0, 0  
    #виведе помилку в разі якщо дані не в коректному форматі
    except (ValueError, IndexError):
        print("Помилка: Некоректний формат даних у файлі.")  
        return 0, 0  
total, average = total_salary(filename)

print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

