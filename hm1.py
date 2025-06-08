import os
import shutil
import argparse

def copy_and_sort_files(src_dir, dest_dir="dist"):
    # Отримання абсолютного шляху до директорії призначення
    abs_dest_dir = os.path.abspath(dest_dir)

    # Рекурсивний обхід усіх підкаталогів та файлів у вихідній директорії
    for root, dirs, files in os.walk(src_dir):
        # Виключення директорії призначення з обходу, щоб не копіювати вміст самої себе
        dirs[:] = [d for d in dirs if os.path.abspath(os.path.join(root, d)) != abs_dest_dir]

        
        for file in files:
            file_path = os.path.join(root, file)

            #Пропускаємо файли, які вже знаходяться в директорії призначення (щоб уникнути зациклення)
            if abs_dest_dir in os.path.abspath(file_path):
                continue

            #Отримання розширення файлу
            ext = os.path.splitext(file)[1].lower().strip('.')
            if not ext:
                ext = 'no_extension' 

            #Створення піддиректорії в dest, яка відповідає розширенню
            target_dir = os.path.join(dest_dir, ext)
            os.makedirs(target_dir, exist_ok=True) 

            #Формування повного шляху до місця призначення
            target_file_path = os.path.join(target_dir, file)

            #Копіювання файлу та обробка можливих помилок
            try:
                shutil.copy2(file_path, target_file_path) 
                print(f"Копійовано: {file_path} → {target_file_path}")
            except Exception as e:
                print(f"Помилка копіювання файлу '{file_path}': {e}")

def main():
    #Налаштування парсера аргументів командного рядка
    parser = argparse.ArgumentParser(description="Рекурсивне копіювання та сортування файлів за розширеннями.")
    parser.add_argument("src", help="Шлях до вихідної директорії")
    parser.add_argument("dest", nargs='?', default="dist", help="Шлях до директорії призначення (за замовчуванням: dist)")
    args = parser.parse_args()

    #Перевірка наявності вихідної директорії
    if not os.path.isdir(args.src):
        print(f"Вихідна директорія '{args.src}' не існує або не є директорією.")
        return

    #Створення директорії призначення
    os.makedirs(args.dest, exist_ok=True)

    #Виконання копіювання та сортування
    copy_and_sort_files(args.src, args.dest)
    print("Завершено.")

if __name__ == "__main__":
    main()
