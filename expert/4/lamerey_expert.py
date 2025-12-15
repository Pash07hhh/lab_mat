import numpy as np
import matplotlib.pyplot as plt


def logistic_map(r, x):
    return r * x * (1 - x)


def lamerey_plot_two_trajectories(r, x0, epsilon, num_iterations):
    """
    Строит лестницу Ламерея для двух траекторий с близкими начальными условиями
    """
    y0 = x0 + epsilon  # второе начальное условие

    # Генерация траекторий
    x_sequence = [x0]
    y_sequence = [y0]

    for _ in range(num_iterations):
        x_new = logistic_map(r, x_sequence[-1])
        y_new = logistic_map(r, y_sequence[-1])
        x_sequence.append(x_new)
        y_sequence.append(y_new)

    # Подготовка координат для лестницы Ламерея (первая траектория)
    x_coords1 = [x_sequence[0]]
    y_coords1 = [0]

    for i in range(len(x_sequence) - 1):
        x_coords1.append(x_sequence[i])
        y_coords1.append(x_sequence[i + 1])

        x_coords1.append(x_sequence[i + 1])
        y_coords1.append(x_sequence[i + 1])

    # Подготовка координат для лестницы Ламерея (вторая траектория)
    x_coords2 = [y_sequence[0]]
    y_coords2 = [0]

    for i in range(len(y_sequence) - 1):
        x_coords2.append(y_sequence[i])
        y_coords2.append(y_sequence[i + 1])

        x_coords2.append(y_sequence[i + 1])
        y_coords2.append(y_sequence[i + 1])

    # Построение графика
    x_range = np.linspace(0, 1, 500)

    plt.figure(figsize=(10, 8))

    # Кривая отображения и диагональ
    plt.plot(x_range, logistic_map(r, x_range), 'k', label='$x_{n+1} = f(x_n)$')
    plt.plot(x_range, x_range, 'k--', label='$y=x$')

    # Две траектории разными цветами
    plt.plot(x_coords1, y_coords1, 'b-', linewidth=1.5, alpha=0.6, label=f'Траектория 1 ($x_0$={x0:.6f})')
    plt.plot(x_coords2, y_coords2, 'r-', linewidth=1.5, alpha=0.6, label=f'Траектория 2 ($y_0$={y0:.6f})')

    # Начальные точки
    plt.plot(x0, 0, 'bo', markersize=8, label=f'$x_0$')
    plt.plot(y0, 0, 'ro', markersize=8, label=f'$y_0$')

    plt.title(f'Лестница Ламерея для двух близких начальных условий\n(r={r}, $x_0$={x0:.6f}, ε={epsilon:.1e})')
    plt.xlabel('$x_n$')
    plt.ylabel('$x_{n+1}$')
    plt.legend(loc='best')
    plt.grid(True, alpha=0.3)
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.show()

    # Также вычислим максимальное расхождение
    max_diff = max([abs(x_sequence[i] - y_sequence[i]) for i in range(num_iterations)])
    print(f"Максимальное расхождение траекторий: {max_diff:.6f}")
    print(f"Отношение начального отличия к максимальному: {max_diff / epsilon:.2e}")


# Параметры
r = 4
x0 = 0.3
epsilon = 1e-6  # очень маленькая разница
num_iterations = 50  # достаточно для демонстрации расхождения

# Построение
lamerey_plot_two_trajectories(r, x0, epsilon, num_iterations)