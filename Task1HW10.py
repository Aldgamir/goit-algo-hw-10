import pulp

# Створюємо модель
model = pulp.LpProblem("Maximize_Drink_Production", pulp.LpMaximize)

# Змінні для кількості виробництва "Лимонаду" і "Фруктового соку"
lemonade = pulp.LpVariable("Лимонад", lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable("Фпукирвий сік", lowBound=0, cat='Integer')

# Функція цілі: максимізувати загальну кількість вироблених продуктів
model += lemonade + fruit_juice, "Всього вироблено напоїв"

# Обмеження ресурсів
model += 2 * lemonade + 1 * fruit_juice <= 100, "Вода"
model += 1 * lemonade <= 50, "Цукоп"
model += 1 * lemonade <= 30, "Лимонний сік"
model += 2 * fruit_juice <= 40, "Фруктове пюре"

# Розв'язання моделі
model.solve()

# Виводимо результати
print(f"Статус: {pulp.LpStatus[model.status]}")
print(f"Лимонад: {lemonade.varValue} одиниць")
print(f"Фруктовий сік: {fruit_juice.varValue} одиниць")
print(f"Загальна кількість продуктів: {pulp.value(model.objective)} одиниць")
