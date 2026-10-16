import subprocess


def git_bish_bash_push(commit_msg: str = "Таблицы и гистограммы были заPUSHены в Git"):
    try:
        subprocess.run(["git", "add", "."], check=True)

        res = subprocess.run(["git", "commit", "-m", commit_msg])

        if res.returncode == 0:
            subprocess.run(["git", "push"], check=True)
            print("[Успех] Изменения закоммичены и отправлены!")
        else:
            print("[Инфо] Нет новых изменений для коммита.")

    except subprocess.CalledProcessError as error:
        print(f"[Ошибка Git] Не удалось выполнить команду: {error}")
    except Exception as error:
        print(f"[Ошибка] Произошел сбой при работе с Git: {error}")
