import random

def get_numbers_ticket(min_num, max_num, quantity):
    if not (1 <= min_num <= max_num <= 1000) or not (min_num <= quantity <= (max_num - min_num + 1)):
        return []
    
    return random.sample(range(min_num, max_num + 1), quantity)  

lottery_numbers1 = get_numbers_ticket(1, 1000, 1000)
lottery_numbers2 = get_numbers_ticket(10, 12, 11)
lottery_numbers3 = get_numbers_ticket(1, 1000, 10)
print ("Ваші лотерейні номерки:",lottery_numbers1)
print ("Ваші лотерейні номерки:",lottery_numbers2)
print ("Ваші лотерейні номерки:",lottery_numbers3)