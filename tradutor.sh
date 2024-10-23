#!/bin/bash

# Ищем файл tradutor.py в системе, начиная с домашней директории
file_path=$(find ~ -name "tradutor.py" 2>/dev/null)

# Проверяем, нашёлся ли файл
if [ -z "$file_path" ]; then
  echo "Файл tradutor.py не найден!"
  exit 1
fi

# Получаем директорию, в которой находится файл
dir_path=$(dirname "$file_path")

# Переходим в директорию с найденным файлом
cd "$dir_path" || exit

# Проверяем версию Python
python3 --version

# Запускаем найденный Python-скрипт
python3 tradutor.py
