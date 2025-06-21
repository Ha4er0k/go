import heapq

def min_connection_cost(cables):
    heapq.heapify(cables)
    total_cost = 0
    steps = []

    while len(cables) > 1:
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        combined = first + second
        total_cost += combined
        steps.append(f"З'єднуємо {first} + {second} = {combined}")
        heapq.heappush(cables, combined)

    print("Послідовність з'єднань:")
    for step in steps:
        print(step)
    print(f"\nЗагальні витрати: {total_cost}")

    return total_cost

if __name__ == "__main__":
    cables = [4, 3, 2, 6]
    min_connection_cost(cables)
