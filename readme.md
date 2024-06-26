# Обчислення інтеграла методом Монте-Карло

У цьому завданні ми обчислюємо значення інтеграла функції за допомогою методу Монте-Карло. Ми використовуємо цей метод для обчислення площі під кривою функції на заданому інтервалу.

## Використані бібліотеки

- `numpy`: для генерації випадкових точок та інших математичних операцій.
- `scipy.integrate`: для обчислення інтеграла за допомогою функції `quad`.

## Опис реалізації

1. Спочатку ми визначаємо функцію, яку потрібно інтегрувати.
2. Задаємо межі інтегрування.
3. Генеруємо випадкові точки в межах інтегрування.
4. Обчислюємо кількість точок, які потрапили під криву функції.
5. Використовуємо формулу Монте-Карло для обчислення площі під кривою.
6. Порівнюємо результати з обчисленням інтеграла за допомогою функції `quad`.

## Висновки

Після порівняння обчислених значень інтеграла методом Монте-Карло та за допомогою функції `quad` з бібліотеки `scipy.integrate`, ми бачимо, що обидва методи дають подібні результати. Але метод Монте_Карло все ж таки більше підходить для рощразунків інтеграла, особливо у випадках, коли аналітичні методи можуть бути складними або неможливими до застосування.

Значення інтеграла разраховано за допомогою функції quad: 2.6666666666666665
Значення інтеграла розраховано за методом Монте-Карло: 2.67472

