import pulp

#створення задачі лінійного програмування (максимізація)
model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

#змінні рішень: кількість лимонаду (x) та фруктового соку (y)
x = pulp.LpVariable("Lemonade", lowBound=0, cat='Integer')
y = pulp.LpVariable("Fruit_Juice", lowBound=0, cat='Integer')

#цільова функція: максимізувати загальну кількість напоїв
model += x + y, "Total_Products"

#обмеження на ресурси:
model += 2 * x + 1 * y <= 100, "Water"
model += 1 * x <= 50, "Sugar"
model += 1 * x <= 30, "Lemon_Juice"
model += 2 * y <= 40, "Fruit_Puree"
model.solve()

print("Status:", pulp.LpStatus[model.status])
print("Кількість лимонаду:", int(x.varValue))
print("Кількість фруктового соку:", int(y.varValue))
print("Загальна кількість напоїв:", int(x.varValue + y.varValue))
