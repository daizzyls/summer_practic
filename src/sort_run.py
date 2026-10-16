import sys
import time
import tracemalloc

from data_creation import generate_data
from sort_dic import SORTS

sys.setrecursionlimit(2000000)


def profile_sort(sort_func, data: list):

    data_copy = data.copy()

    tracemalloc.start()
    start_time = time.perf_counter()

    result = sort_func(data_copy)

    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    elapsed_ms = (end_time - start_time) * 1000.0
    peak_kb = peak / 1024.0

    return round(elapsed_ms, 3), round(peak_kb, 2)
