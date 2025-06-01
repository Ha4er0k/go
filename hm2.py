from collections import deque

def is_palindrome(input_str):
    #Попередня обробка рядка: видалення пробілів, приведення до нижнього регістру
    cleaned_str = ''.join(char.lower() for char in input_str if char.isalnum())

    #Створення двосторонньої черги
    char_deque = deque(cleaned_str)

    #Порівняння символів з обох кінців
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False  #Не паліндром
    return True  #Паліндром

#Приклади використання
test_strings = [
    "A man a plan a canal Panama",
    "racecar",
    "No lemon, no melon",
    "hello",
    "Was it a car or a cat I saw"
]

for s in test_strings:
    result = is_palindrome(s)
    print(f"'{s}' → {'паліндром' if result else 'не паліндром'}")
