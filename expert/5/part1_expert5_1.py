import numpy as np
import matplotlib.pyplot as plt


def logistic_map(r, x):
    """Логистическое отображение - наша динамическая система"""
    return r * x * (1 - x)


def build_bifurcation_diagram():
    """
    Основная функция для построения бифуркационной диаграммы
    """
    # Параметры построения
    r_min = 0  # минимальное значение r
    r_max = 4.0  # максимальное значение r
    num_r = 2000  # количество точек по r (чем больше, тем детальнее)

    iterations = 1000  # общее число итераций
    last_points = 200  # сколько последних точек использовать для графика
    x0 = 0.5  # начальное значение

    r_values = np.linspace(r_min, r_max, num_r)

    all_x_values = []
    all_r_values = []

    for i, r in enumerate(r_values):

        x = x0  # начинаем с начального значения
        for _ in range(iterations - last_points):
            x = logistic_map(r, x)

        # Шаг 2: Сохраняем последние точки (установившийся режим)
        for _ in range(last_points):
            x = logistic_map(r, x)
            all_x_values.append(x)
            all_r_values.append(r)


    plt.figure(figsize=(12, 8))
    plt.plot(all_r_values, all_x_values, ',k',
             alpha=0.1,
             markersize=0.1)

    plt.title('Бифуркационная диаграмма логистического отображения',
              fontsize=16, pad=20)
    plt.xlabel('Параметр роста $r$', fontsize=14)
    plt.ylabel('Значение $x_n$ в установившемся режиме', fontsize=14)
    plt.grid(True, alpha=0.3)


    # 1. r = 3 - первая бифуркация удвоения периода
    plt.axvline(x=3, color='red', linestyle='--',
                alpha=0.5, linewidth=2,
                label='$r=3$ (первое удвоение периода)')

    # 2. r∞ ≈ 3.5699456 - переход к хаосу
    r_infinity = 3.5699456
    plt.axvline(x=r_infinity, color='green', linestyle='--',
                alpha=0.7, linewidth=2,
                label=f'$r_\infty \\approx 3.5699$ (переход к хаосу)')

    # 3. r = 1 - рождение ненулевой неподвижной точки
    plt.axvline(x=1, color='blue', linestyle='--',
                alpha=0.5, linewidth=2,
                label='$r=1$ (рождение ненулевой точки)')

    plt.legend(loc='upper right', fontsize=11)

    info_text = (
        "Интерпретация:\n"
        "• Одна линия = фиксированная точка\n"
        "• Две линии = цикл периода 2\n"
        "• Четыре линии = цикл периода 4\n"
        "• Сплошная область = хаос\n"
        "• 'Окна' в хаосе = возврат к регулярности"
    )

    plt.text(0.02, 0.02, info_text, transform=plt.gca().transAxes,
             fontsize=10, verticalalignment='bottom',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

    plt.tight_layout()
    plt.show()


build_bifurcation_diagram()