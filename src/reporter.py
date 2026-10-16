import os

import matplotlib.pyplot as plt
import numpy as np

SIZES = [10, 500, 1000, 50000, 1000000]
DATA_TYPES = ["Random", "Sorted", "Reverse", "Almost Sorted"]


def save_markdown_table(
    sort_name: str,
    results: dict,
    os_name: str = "Win",
    interp_name: str = "CPython",
    output_dir: str = "reports",
):
    """Сохраняет таблицу результатов в Markdown-файл в папку reports/."""
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, f"table_{sort_name.lower()}.md")

    headers = ["(~) ОС", "Интерпретатор", "Алгоритм"]
    for n in SIZES:
        headers.append(f"N={n} (время, мс)")
        headers.append(f"N={n} (память, КБ)")

    header_row = "| " + " | ".join(headers) + " |"
    divider_row = "| " + " | ".join(["---"] * len(headers)) + " |"

    lines = [f"# Таблица результатов: {sort_name.upper()}\n", header_row, divider_row]

    for d_type in DATA_TYPES:
        row = [os_name, interp_name, f"{sort_name.capitalize()} ({d_type})"]
        for n in SIZES:
            res = results.get((n, d_type), {})
            time_val = res.get("time_ms")
            mem_val = res.get("memory_kb")

            row.append(f"{time_val}" if time_val is not None else "-")
            row.append(f"{mem_val}" if mem_val is not None else "-")

        lines.append("| " + " | ".join(row) + " |")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"[Успех] Таблица сохранена: {file_path}")


def save_histogram(sort_name: str, results: dict, output_dir: str = "img"):
    """Строит гистограмму ДЛЯ ВСЕХ N с помощью логарифмической шкалы и сохраняет в img/."""
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, f"{sort_name.lower()}_hist.png")

    x = np.arange(len(SIZES))
    width = 0.2

    fig, ax = plt.subplots(figsize=(12, 6))

    for i, d_type in enumerate(DATA_TYPES):
        times = []
        for n in SIZES:
            res = results.get((n, d_type), {})
            t = res.get("time_ms")
            # Если замеров нет или время 0, ставим минимальное значение > 0 для корректной работы лог-шкалы
            times.append(t if t is not None and t > 0 else 1e-4)

        ax.bar(x + (i * width) - (width * 1.5), times, width, label=d_type)

    # Включаем логарифмическую шкалу для отображения микросекунд и секунд на одном графике
    ax.set_yscale("log")

    ax.set_xlabel("Размер массива (N)")
    ax.set_ylabel("Время выполнения в мс (лог. шкала)")
    ax.set_title(f"Время работы {sort_name.upper()} для всех N")
    ax.set_xticks(x)
    ax.set_xticklabels([f"N={n}" for n in SIZES])
    ax.legend(title="Тип данных")
    ax.grid(True, which="both", linestyle="--", alpha=0.5)

    plt.tight_layout()
    plt.savefig(file_path, dpi=300)
    plt.close()

    print(f"[Успех] Гистограмма сохранена: {file_path}")
