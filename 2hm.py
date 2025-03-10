import random

def get_numbers_ticket(min_num, max_num, quantity):
    if not (1 <= min_num <= max_num <= 1000) or not (min_num <= quantity <= max_num):
     return []
 
    numbers = random.sample(range(min_num, max_num + 1), quantity)
    return sorted(numbers)

lottery_numbers = get_numbers_ticket(1, 1000, 10)
print("Ваші лотерейні числа:", lottery_numbers)