import matplotlib.pyplot as plt
import math

def koch_snowflake(ax, x1, y1, x2, y2, level):
    if level == 0:
        ax.plot([x1, x2], [y1, y2], color='blue')
    else:
        #Точки ділення відрізка на 3 частини
        dx = (x2 - x1) / 3
        dy = (y2 - y1) / 3

        xA = x1 + dx
        yA = y1 + dy

        xB = x1 + 2 * dx
        yB = y1 + 2 * dy

        #Обчислення координат вершини "піку"
        angle = math.radians(60)
        xM = 0.5 * (xA + xB) - math.sqrt(3)/6 * (yB - yA)
        yM = 0.5 * (yA + yB) + math.sqrt(3)/6 * (xB - xA)

        #Рекурсивно малюємо 4 частини
        koch_snowflake(ax, x1, y1, xA, yA, level - 1)
        koch_snowflake(ax, xA, yA, xM, yM, level - 1)
        koch_snowflake(ax, xM, yM, xB, yB, level - 1)
        koch_snowflake(ax, xB, yB, x2, y2, level - 1)

def draw_snowflake(level):
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.axis('off')

    #Початковий трикутник
    size = 300
    height = size * math.sqrt(3) / 2
    x0, y0 = 0, 0
    x1, y1 = size, 0
    x2, y2 = size / 2, height

    koch_snowflake(ax, x0, y0, x1, y1, level)
    koch_snowflake(ax, x1, y1, x2, y2, level)
    koch_snowflake(ax, x2, y2, x0, y0, level)

    plt.title(f"Сніжинка Коха (рівень {level})")
    plt.show()

if __name__ == "__main__":
    try:
        level = int(input("Введіть рівень рекурсії (наприклад, 3): "))
        if level < 0:
            raise ValueError
        draw_snowflake(level)
    except ValueError:
        print("Введіть ціле число більше або рівне 0.")

   