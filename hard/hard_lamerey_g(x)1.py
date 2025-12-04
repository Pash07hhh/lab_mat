import numpy as np
import matplotlib.pyplot as plt


def logistic_map(r, x):
    """
    Кубическое отображение g(x_n)
    """
    return r * x * (1 - x) * (2 + ч)


def lamerey_plot_simplified(r, x0, num_iterations):
    """
    Строит лестницу Ламерея
    """

    x_sequence = [x0]
    for _ in range(num_iterations):
        x_new = logistic_map(r, x_sequence[-1])
        x_sequence.append(x_new)

    x_coords = [x_sequence[0]]
    y_coords = [0]

    current_x = x_sequence[:-1]
    next_x = x_sequence[1:]

    for x_n, x_n_plus_1 in zip(current_x, next_x):
        x_coords.append(x_n)
        y_coords.append(x_n_plus_1)

        x_coords.append(x_n_plus_1)
        y_coords.append(x_n_plus_1)

    x_min = 0
    x_max = 1
    x_range = np.linspace(x_min, x_max, 500)

    plt.figure(figsize=(8, 8))
    plt.plot(x_range, logistic_map(r, x_range), 'k', label='$x_{n+1} = f(x_n)$')
    plt.plot(x_range, x_range, 'k--', label='$y=x$')
    plt.plot(x_coords, y_coords, 'r-', linewidth=1.5, alpha=0.7, label='Траектория (Лестница Ламерея)')
    plt.plot(x_sequence[0], 0, 'go', markersize=5, label='$x_0$')

    plt.title(f'Лестница Ламерея для Логистического Отображения (r={r}, $x_0$={x0})')
    plt.xlabel('$x_n$')
    plt.ylabel('$x_{n+1}$')
    plt.legend()
    plt.grid(True)
    plt.show()

lamerey_plot_simplified(r=1.8, x0=0.8, num_iterations=150)
