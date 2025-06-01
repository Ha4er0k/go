import queue
import time
import random

#Створення черги заявок
request_queue = queue.Queue()

#Лічильник для унікального номера заявки
request_id_counter = 1

def generate_request():
    global request_id_counter
    #Генерація нової заявки
    request = f"Заявка #{request_id_counter}"
    request_id_counter += 1
    #Додавання до черги
    request_queue.put(request)
    print(f"[+] Створено: {request}")

def process_request():
    if not request_queue.empty():
        #Видалення з черги
        request = request_queue.get()
        print(f"[✔] Обробляється: {request}")
        time.sleep(random.uniform(0.5, 1.5))  #Імітація часу обробки
        print(f"[✓] Завершено: {request}")
    else:
        print("[!] Черга порожня. Немає заявок для обробки.")

def main():
    print("Симуляція сервісного центру. Натисніть Ctrl+C для завершення.")
    try:
        while True:
            #З випадковою імовірністю генеруємо нову заявку
            if random.random() < 0.7:  #70% ймовірність створення заявки
                generate_request()
            process_request()
            time.sleep(1)  #Затримка між ітераціями головного циклу
    except KeyboardInterrupt:
        print("\n[!] Завершення програми.")

if __name__ == "__main__":
    main()
   
   