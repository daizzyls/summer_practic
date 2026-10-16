import git_pushing
from benchmark import single_benchmark
from git_pushing import git_bish_bash_push
from reporter import save_histogram, save_markdown_table
from sort_dic import SORTS

if __name__ == "__main__":
    # Прогоняем замеры и генерацию файлов для каждой сортировки из вашего словаря
    TARGET_SORT = str(input("PLS ENTER SORT U WANT: "))

    if TARGET_SORT.lower().strip() == "all":
        for sort_name in SORTS.keys():
            print(f"\n==========================================")
            print(f"   ОБРАБОТКА СОРТИРОВКИ: {sort_name.upper()}")
            print(f"==========================================")

            # 1. Запуск замеров
            results = single_benchmark(sort_name)

            # 2. Сохранение Markdown-таблицы в папку reports/
            save_markdown_table(sort_name, results)

            # 3. Генерация и сохранение гистограммы со всеми N в папку img/
            save_histogram(sort_name, results)
    elif TARGET_SORT.lower().strip() in SORTS.keys():
        print(f"\n==========================================")
        print(f"   ОБРАБОТКА СОРТИРОВКИ: {TARGET_SORT.strip().upper()}")
        print(f"==========================================")

        results = single_benchmark(TARGET_SORT.lower().strip())

        save_markdown_table(TARGET_SORT.lower().strip(), results)

        save_histogram(TARGET_SORT.lower().strip(), results)
    else:
        print(f"\n[Ошибка] Сортировка '{TARGET_SORT}' не найдена!")

    git_bish_bash_push()
