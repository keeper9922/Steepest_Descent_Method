import math
from funcs import *
from matplotlib import pyplot as plt

def distance_squared(theta, phi):
    # Точка на первой кривой (окружность)
    x1 = 1 + math.sqrt(2) * math.cos(theta)
    y1 = -2 + math.sqrt(2) * math.sin(theta)

    # Точка на второй кривой (параметрическая)
    x2 = math.cos(phi) ** 3 - 1
    y2 = 2 + math.sin(phi) ** 3

    # Квадрат расстояния
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


# Метод наискорейшего спуска
def gradient_descent(start_x, start_y, num_iterations, _h: float = 0.001, eps: float = 1e-7):
    x = start_x
    y = start_y

    # Список для хранения значений функции, чтобы потом проверить сходимость
    # history = []

    first = [x]
    second = [y]
    l = eps - _h
    for i in range(num_iterations):
        # Вычисляем значение функции в текущей точке
        value = distance_squared(x, y)
        # history.append(value)

        # Вычисляем градиент
        grad_x, grad_y = gradient(x, y, distance_squared, _h)

        if grad_x <= eps or grad_y <= eps:
            print("Невозможно определить направление убывания функции")
            return x, y, first, second
        # Обновляем x и y, двигаясь против градиента
        x = x - l * grad_x
        y = y - l * -grad_y
        first.append(x)
        second.append(y)
        # Выводим информацию о текущей итерации
        print(f"Итерация {i + 1}: x = {x:.4f}, y = {y:.4f}, f(x, y) = {value:.4f}")

    return x, y, first, second

# Параметры
start_theta = 0.0  # Начальное значение theta
start_phi = 0.0    # Начальное значение phi
iters = 50000
h = 0.001

# Запускаем градиентный спуск
final_theta, final_phi, all_x, all_y = gradient_descent(start_theta, start_phi, iters, h)
# Вычисляем точки на кривых
x1 = 1 + math.sqrt(2) * math.cos(final_theta)
y1 = -2 + math.sqrt(2) * math.sin(final_theta)
x2 = math.cos(final_phi) ** 3 - 1
y2 = 2 + math.sin(final_phi) ** 3

# Минимальное расстояние
min_distance = math.sqrt(distance_squared(final_theta, final_phi))

print(f"\nНайденные параметры: theta = {final_theta:.4f}, phi = {final_phi:.4f}")
print(f"Точка на первой кривой: ({x1:.4f}, {y1:.4f})")
print(f"Точка на второй кривой: ({x2:.4f}, {y2:.4f})")
print(f"Минимальное расстояние: {min_distance:.4f}")


# Параметры окружности (первая кривая)
theta_values = [t for t in [i * math.pi / 50 for i in range(101)]]
m_x1 = [1 + math.sqrt(2) * math.cos(t) for t in theta_values]
m_y1 = [-2 + math.sqrt(2) * math.sin(t) for t in theta_values]

# Параметры второй кривой
phi_values = [p for p in [i * math.pi / 50 for i in range(101)]]
m_x2 = [math.cos(p) ** 3 - 1 for p in phi_values]
m_y2 = [2 + math.sin(p) ** 3 for p in phi_values]

# Создание графика
plt.figure(figsize=(8, 8))
plt.plot(m_x1, m_y1, label='Окружность: (x-1)^2 + (y+2)^2 = 2', color='blue')
plt.plot(m_x2, m_y2, label='Кривая: x = cos^3phi - 1, y = 2 + sin^3phi', color='red')

# Отметка точек минимального расстояния
plt.plot(x1, y1, 'go', label='Точка на окружности')
plt.plot(x2, y2, 'yo', label='Точка на кривой')
plt.plot([x1, x2], [y1, y2], 'g--', label='Минимальное расстояние')

# Настройки графика
plt.title('Минимальное расстояние между кривыми')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.axis('equal')  # Чтобы окружность выглядела как окружность
plt.show()
