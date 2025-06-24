import random
from collections import Counter

# Кількість симуляцій
n = 100000

# Зберігаємо всі суми
sums = []

# Кидки кубиків
for _ in range(n):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    sums.append(total)

# Підрахунок кожної суми
counts = Counter(sums)

# Виведення ймовірностей
print("Сума\tЙмовірність")
for total in range(2, 13):
    probability = counts[total] / n * 100
    print(f"{total}\t{probability:.2f}%")
