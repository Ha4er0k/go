items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)

    total_calories = 0
    chosen_items = []

    for name, data in sorted_items:
        if data['cost'] <= budget:
            chosen_items.append(name)
            budget -= data['cost']
            total_calories += data['calories']

    return chosen_items, total_calories

def dynamic_programming(items, budget):
    names = list(items.keys())
    n = len(names)

    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        cost = items[names[i-1]]["cost"]
        cal = items[names[i-1]]["calories"]
        for j in range(budget + 1):
            if cost <= j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost] + cal)
            else:
                dp[i][j] = dp[i-1][j]

    chosen_items = []
    i, j = n, budget
    while i > 0 and j >= 0:
        if dp[i][j] != dp[i-1][j]:
            chosen_items.append(names[i-1])
            j -= items[names[i-1]]["cost"]
        i -= 1

    return chosen_items[::-1], dp[n][budget]

budget = 100

print("Greedy Algorithm:")
chosen, calories = greedy_algorithm(items, budget)
print("Chosen items:", chosen)
print("Total calories:", calories)

print("\nDynamic Programming:")
chosen, calories = dynamic_programming(items, budget)
print("Chosen items:", chosen)
print("Total calories:", calories)
