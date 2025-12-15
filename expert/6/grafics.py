import numpy as np
import matplotlib.pyplot as plt


def logistic_map(r, x):
    return r * x * (1 - x)


def zoom_bifurcation_diagram(center_r=3.83, zoom_factor=50, width=0.1):
    r_min = center_r - width / zoom_factor
    r_max = center_r + width / zoom_factor
    num_r = 2000
    iterations = 2000
    last_points = 300

    r_values = np.linspace(r_min, r_max, num_r)
    all_x = []
    all_r = []

    for r_val in r_values:
        x = 0.5
        for _ in range(iterations - last_points):
            x = logistic_map(r_val, x)
        for _ in range(last_points):
            x = logistic_map(r_val, x)
            all_x.append(x)
            all_r.append(r_val)

    plt.figure(figsize=(12, 8))
    plt.plot(all_r, all_x, ',k', alpha=0.1, markersize=0.1)
    plt.title(f'Увеличенный фрагмент\nЦентр: $r = {center_r}$, увеличение: {zoom_factor}$\\times$', fontsize=16)
    plt.xlabel('Параметр $r$', fontsize=14)
    plt.ylabel('$x_n$', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.axvline(x=center_r, color='red', linestyle='--', alpha=0.5, linewidth=2)

    info_text = f"Диапазон: r ∈ [{r_min:.6f}, {r_max:.6f}]\nШирина: {(r_max - r_min):.6f}"
    plt.text(0.02, 0.02, info_text, transform=plt.gca().transAxes, fontsize=10,
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
    plt.tight_layout()
    plt.show()


def find_periodic_windows(target_period=3, r_start=3.82, r_end=3.86):
    num_r = 5000
    iterations = 5000
    tolerance = 1e-4

    r_values = np.linspace(r_start, r_end, num_r)
    windows = []

    for r_val in r_values:
        x = 0.5
        history = []
        for _ in range(iterations // 2):
            x = logistic_map(r_val, x)
        for _ in range(target_period * 10):
            x = logistic_map(r_val, x)
            history.append(x)

        if len(history) >= target_period * 2:
            cycle_found = True
            for j in range(target_period):
                if abs(history[j] - history[j + target_period]) > tolerance:
                    cycle_found = False
                    break
            if cycle_found:
                windows.append(r_val)

    if windows:
        windows = np.array(windows)
        intervals = []
        start = windows[0]
        for i in range(1, len(windows)):
            if windows[i] - windows[i - 1] > (r_end - r_start) / num_r * 10:
                intervals.append((start, windows[i - 1]))
                start = windows[i]
        intervals.append((start, windows[-1]))
        return intervals
    return []


def plot_window(ax, r_min, r_max, period, color, title):
    num_r = 1000
    iterations = 1000
    last_points = 200

    r_values = np.linspace(r_min, r_max, num_r)
    x_values = []
    r_plot = []

    for r_val in r_values:
        x = 0.5
        for _ in range(iterations - last_points):
            x = logistic_map(r_val, x)
        for _ in range(last_points):
            x = logistic_map(r_val, x)
            x_values.append(x)
            r_plot.append(r_val)

    ax.plot(r_plot, x_values, ',', color=color, alpha=0.3, markersize=1)
    ax.set_title(title, fontsize=14)
    ax.set_ylabel('$x_n$', fontsize=12)
    ax.grid(True, alpha=0.2)
    ax.set_xlim(r_min, r_max)
    ax.text(0.5, 0.95, f'Период: {period}', transform=ax.transAxes,
            ha='center', fontsize=11, bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))


def visualize_periodic_windows():
    fig, axes = plt.subplots(3, 1, figsize=(12, 12))

    plot_window(axes[0], 3.82, 3.86, 3, 'red', 'Окно периода 3')
    plot_window(axes[1], 3.73, 3.75, 5, 'blue', 'Окно периода 5')
    plot_window(axes[2], 3.62, 3.64, 6, 'green', 'Окно периода 6')

    fig.text(0.5, 0.04, 'Параметр $r$', ha='center', fontsize=14)
    plt.tight_layout(rect=[0, 0.05, 1, 0.95])
    plt.show()


if __name__ == "__main__":
    zoom_bifurcation_diagram(center_r=3.83, zoom_factor=50, width=0.1)

    period_3 = find_periodic_windows(target_period=3, r_start=3.82, r_end=3.86)
    period_5 = find_periodic_windows(target_period=5, r_start=3.73, r_end=3.75)
    period_6 = find_periodic_windows(target_period=6, r_start=3.62, r_end=3.64)

    visualize_periodic_windows()