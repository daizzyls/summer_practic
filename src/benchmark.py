import sys

from data_creation import generate_data
from sort_dic import SORTS
from sort_run import profile_sort

SIZES = [10, 500, 1000, 50000, 1000000]
DATA_TYPES = ["Random", "Sorted", "Reverse", "Almost Sorted"]
SLOW_SORTS = ["insert", "selection", "bubble"]


def single_benchmark(sort_name: str):

    sort_clean = sort_name.lower().strip()

    if sort_clean not in SORTS:
        raise ValueError(f"Алгоритм '{sort_name}' не найден в SORTS!")

    sort_func = SORTS[sort_clean]
    results = {}

    print(f"=== Старт тестирования алгоритма: {sort_name.upper()} ===")

    for n in SIZES:
        if n >= 50000 and sort_clean in SLOW_SORTS:  # Скипаем нищие алгоритмы
            for d_type in DATA_TYPES:
                results[(n, d_type)] = {"time_ms": None, "memory_kb": None}
            print(f"[N = {n:<7}] Пропущен (Таймаут O(N^2))")
            continue

        for d_type in DATA_TYPES:
            raw_data = generate_data(size=n, data_type=d_type)  # Generate our arr

            try:
                time_ms, memory_kb = profile_sort(sort_func, raw_data)
                results[(n, d_type)] = {"time_ms": time_ms, "memory_kb": memory_kb}
                print(
                    f"[N = {n:<7} | {d_type:<13}] Время: {time_ms:>8.3f} мс | Память: {memory_kb:>8.2f} КБ"
                )
            except Exception as error:
                print(f"[N = {n:<7} | {d_type:<13}] Ошибка: {error}")
                results[(n, d_type)] = {"time_ms": None, "memory_kb": None}

    return results
