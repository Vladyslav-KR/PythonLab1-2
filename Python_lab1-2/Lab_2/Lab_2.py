# Кравченко Владислав
import math

# === Завдання 1 ===
print("Завдання 1: Площі трьох прямокутників")
for i in range(1, 4):
    a = float(input(f"Введіть сторону A прямокутника №{i}: "))
    b = float(input(f"Введіть сторону B прямокутника №{i}: "))
    area = a * b
    print(f"Площа прямокутника №{i}: {area}")

# === Завдання 2 ===
print("\nЗавдання 2: Гіпотенузи двох трикутників")

def hypotenuse(a, b):
    return math.sqrt(a2 + b2)

a1 = float(input("Катет A трикутника 1: "))
b1 = float(input("Катет B трикутника 1: "))
a2 = float(input("Катет A трикутника 2: "))
b2 = float(input("Катет B трикутника 2: "))

h1 = hypotenuse(a1, b1)
h2 = hypotenuse(a2, b2)

print(f"Гіпотенуза 1: {h1:.2f}")
print(f"Гіпотенуза 2: {h2:.2f}")

if h1 > h2:
    print("Перша гіпотенуза більша")
elif h2 > h1:
    print("Друга гіпотенуза більша")
else:
    print("Гіпотенузи рівні")

# === Завдання 3 ===
print("\nЗавдання 3: Перевірка, які точки лежать всередині кола")

def is_inside_circle(x, y, a, b, R):
    return (x - a)**2 + (y - b)**2 < R**2

a = float(input("Центр кола A (x): "))
b = float(input("Центр кола B (y): "))
R = float(input("Радіус кола R: "))

# Введення координат точок
p1, p2 = map(float, input("Координати точки P (через пробіл): ").split())
f1, f2 = map(float, input("Координати точки F (через пробіл): ").split())
l1, l2 = map(float, input("Координати точки L (через пробіл): ").split())

count = 0
if is_inside_circle(p1, p2, a, b, R): count += 1
if is_inside_circle(f1, f2, a, b, R): count += 1
if is_inside_circle(l1, l2, a, b, R): count += 1

print(f"Кількість точок всередині кола: {count}")

# === Завдання 4 ===
print("\nЗавдання 4: Площа чотирикутника з прямим кутом між X і Y")

X = float(input("Сторона X: "))
Y = float(input("Сторона Y: "))
Z = float(input("Сторона Z: "))
T = float(input("Сторона T: "))

# Розбиваємо чотирикутник на два трикутники:
# один — прямокутний (XY), другий — через формулу Герона
area1 = 0.5 * X * Y
s2 = (Z + T + math.hypot(X, Y)) / 2
area2 = math.sqrt(s2 * (s2 - Z) * (s2 - T) * (s2 - math.hypot(X, Y)))

total_area = area1 + area2
print(f"Загальна площа чотирикутника: {total_area:.2f}")

# === Завдання 5 ===
print("\nЗавдання 5: Натуральні числа, що діляться на всі задані")

n = int(input("Введіть n (межа): "))
nums = list(map(int, input("Введіть дільники через пробіл: ").split()))

print("Числа, що діляться на всі задані дільники:")
for i in range(1, n + 1):
    if all(i % d == 0 for d in nums):
        print(i, end=' ')
