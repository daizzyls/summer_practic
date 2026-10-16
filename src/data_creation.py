import random

#DATA_TYPE:
#Rand - full random
#Sort - full sorted
#Rev - reversed
#Alms - sorted for 95% 


def generate_data(size: int, data_type: str, minimum = None, maximum = None):
    
    min_val = minimum if minimum is not None else -10**9
    max_val = maximum if maximum is not None else 10**9

    if data_type == "Rand" or data_type == "Random":
        return random.choices(range(min_val, max_val + 1), k=size)
    
    elif data_type == "Sort" or data_type == "Sorted":
        arr = random.choices(range(min_val, max_val + 1), k=size)
        return sorted(arr)
    
    elif data_type == "Rev" or data_type == "Reverse":
        arr = random.choices(range(min_val, max_val + 1), k=size)
        return sorted(arr, reverse=True)
    
    elif data_type == "Alms" or data_type == "Almost Sorted":
        arr = sorted(random.choices(range(min_val, max_val + 1), k=size))
        
        swap_count = max(1, int(size * 0.05)) # 5% элементов
        for _ in range(swap_count):
            i1 = random.randint(0, size - 1)
            i2 = random.randint(0, size - 1)
            arr[i1], arr[i2] = arr[i2], arr[i1]
        return arr
    