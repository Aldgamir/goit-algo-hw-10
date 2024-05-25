import numpy as np
import scipy.integrate as spi

# Визначення функції, яку потрібно інтегрувати
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Кількість точок, які ми генеруємо
n = 100000

# Генерування n випадкових точок в межах інтегрування
x_random = np.random.uniform(a, b, n)
y_random = np.random.uniform(0, f(b), n)  # Вибираємо максимальне значення y як верхню межу

# Обчислення кількості точок, які потрапили під криву
points_under_curve = sum(y_random <= f(x_random))

# Площа прямокутника
rectangle_area = (b - a) * f(b)

# Обчислення площі під кривою за методом Монте-Карло
integral = rectangle_area * (points_under_curve / n)
# Визначення функції, яку потрібно інтегрувати
def f(x):
    return x**2

# Визначення меж інтегрування
a = 0  # Нижня межа
b = 2  # Верхня межа

# Обчислення інтеграла за допомогою функції quad
result_quad, error = spi.quad(f, a, b)

print("Значення інтеграла разраховано за допомогою функції quad:", result_quad)

print("Значення інтеграла розраховано за методом Монте-Карло:", integral)
