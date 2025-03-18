import os
filename = "cats_file.txt" #створив файл та дав йому ім'я

#перевірка, чи файл вже існує
if not os.path.exists(filename):  
    with open(filename, "w", encoding="utf-8") as file:  #("w") - відкриття файлу в режимі запису,"write"
        file.write("60b90c1c13067a15887e1ae1,Tayson,3\n")
        file.write("60b90c2413067a15887e1ae2,Vika,1\n")
        file.write("60b90c2e13067a15887e1ae3,Barsik,2\n")
        file.write("60b90c3b13067a15887e1ae4,Simon,12\n")
        file.write("60b90c4613067a15887e1ae5,Tessi,5\n")

def get_cats_info(path):

    cats_list = []  #пустий список для інформації про киць

    try:
        #("r") - відкриття файлу в режимі читання
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(",")  #видаляє зайві пробіли та розділяє рядок за комами
                if len(parts) == 3:  #перевірка, чи є всі три частини (id, ім'я, вік)
                    cat_info = {
                        "id": parts[0],   #унікальний ідентифікатор киці
                        "name": parts[1], #ім'я киці
                        "age": parts[2]   #вік киці
                    }
                    cats_list.append(cat_info)  #додаю словник до списку

        return cats_list

    #виведе помилку в разі якщо файл не знайдено
    except FileNotFoundError:
        print("Помилка: Файл не знайдено.")
        return []

    #виведе помилку в разі якщо некоректні дані
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        return []

cats_info = get_cats_info(filename)

print(cats_info)
