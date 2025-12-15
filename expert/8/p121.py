import numpy as np
import matplotlib.pyplot as plt

# Определение отображения
def f(x, r):
    return r * x * (1 - x) * (2 + x)

# Параметры
r_min = 0.0
r_max = 27 / (2 * (7 * np.sqrt(7) - 10))  # ≈ 1.584
num_r = 1000
r_values = np.linspace(r_min, r_max, num_r)

# Итерации
num_transient = 500
num_plot = 100

x_data = []
r_data = []

for r in r_values:
    x = 0.5
    for _ in range(num_transient):
        x = f(x, r)
        if abs(x) > 10:
            break
    for _ in range(num_plot):
        x = f(x, r)
        if abs(x) > 10:
            break
        x_data.append(x)
        r_data.append(r)

# Общая диаграмма
plt.figure(figsize=(12, 8))
plt.scatter(r_data, x_data, s=0.1, c='black', alpha=0.6)
plt.title('Бифуркационная диаграмма для $f(x) = r x (1-x)(2+x)$')
plt.xlabel('$r$')
plt.ylabel('$x_n$')
plt.grid(True, alpha=0.3)
plt.axvline(x=0.5, color='red', linestyle='--', label='$r = 0.5$ (граница устойчивости)')
plt.legend()
plt.xlim(r_min, r_max)
plt.ylim(-1, 2)
plt.savefig('bifurcation.png', dpi=300, bbox_inches='tight')
plt.close()

# Зум на окна периодичности
plt.figure(figsize=(12, 8))
plt.scatter(r_data, x_data, s=0.1, c='blue', alpha=0.6)
plt.title('Окна периодичности ($r \in [0.8, 1.5]$)')
plt.xlabel('$r$')
plt.ylabel('$x_n$')
plt.grid(True, alpha=0.3)
plt.axvline(x=0.5, color='red', linestyle='--', label='$r = 0.5$')
plt.xlim(0.8, 1.5)
plt.ylim(-0.5, 1.0)
plt.legend()
plt.savefig('windows_zoom.png', dpi=300, bbox_inches='tight')
plt.close()