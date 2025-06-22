from typing import Dict
from collections import defaultdict

#список доступних монет
coins = [50, 25, 10, 5, 2, 1]

#жадібний алгоритм
def find_coins_greedy(amount: int) -> Dict[int, int]:
    result = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            amount -= coin * count
            result[coin] = count
    return result

#динамічне програмування
def find_min_coins(amount: int) -> Dict[int, int]:
    dp = [(float('inf'), {}) for _ in range(amount + 1)]
    dp[0] = (0, {})

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                prev_count, prev_combo = dp[i - coin]
                if prev_count + 1 < dp[i][0]:
                    new_combo = prev_combo.copy()
                    new_combo[coin] = new_combo.get(coin, 0) + 1
                    dp[i] = (prev_count + 1, new_combo)
    return dp[amount][1]

def test_change_algorithms(amount: int):
    import time

    start = time.time()
    greedy_result = find_coins_greedy(amount)
    greedy_time = time.time() - start

    start = time.time()
    dp_result = find_min_coins(amount)
    dp_time = time.time() - start

    print(f"Сума: {amount}\n")
    print(f"Жадібний результат: {greedy_result}, час: {greedy_time:.6f} с\n")
    print(f"Динамічний результат: {dp_result}, час: {dp_time:.6f} с\n")

test_change_algorithms(333)  #можна змінити на будь-яке число 

