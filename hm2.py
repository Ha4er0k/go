import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

#функція для інтегрування
def f(x):
    return x ** 2

#межі інтегрування
a = 0
b = 2

#кількість випадкових точок
N = 100_000

#метод Монте-Карло
x_rand = np.random.uniform(a, b, N)
y_rand = f(x_rand)
integral_mc = (b - a) * np.mean(y_rand)

print(f"Інтеграл методом Монте-Карло: {integral_mc:.6f}\n")

#точне значення для порівняння
result, error = quad(f, a, b)
print(f"Інтеграл функцією quad: {result:.6f}, похибка: {error:.2e}\n")
print(f"Абсолютна різниця: {abs(integral_mc - result):.6f}\n")
