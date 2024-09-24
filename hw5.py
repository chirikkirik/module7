import os
import time

def print_file_info(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            last_modified_time = time.ctime(os.path.getmtime(file_path))
            parent_directory = os.path.dirname(file_path)

            print(f"Файл: {file_path}")
            print(f"Размер: {file_size} байт")
            print(f"Последнее изменение: {last_modified_time}")
            print(f"Родительская директория: {parent_directory}")
            print("-" * 20)

directory = r"C:\Users\КирикЧирик\PycharmProjects\module7"

print_file_info(directory)
