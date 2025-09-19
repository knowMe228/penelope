#!/usr/bin/env python3

# Скрипт для исправления синтаксических ошибок в penelope.py

import re

# Читаем файл
with open('/mnt/shared/Новая папка/penelope/penelope.py', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Исправляем проблему с '\n' в строках 3459, 3460, 3472, 3473, 3481, 3482
# Заменяем '\n' на '\\n' в этих конкретных местах
# Мы должны быть очень точны, чтобы не испортить другие части кода

# Найдем и исправим проблемные строки
# Проблема в том, что в строке 3459 есть:
# while '\n' in error_buffer:
# и в строке 3460:
# line, error_buffer = error_buffer.split('\n', 1)

# Эти строки находятся внутри большой f-строки, которая начинается примерно с 3365 строки
# и заканчивается около 3500 строки.

# Мы будем искать конкретные паттерны и заменять их

# Паттерн 1: while '\n' in error_buffer:
pattern1 = r"while '\\n' in error_buffer:"
replacement1 = r"while '\\\\n' in error_buffer:"

# Паттерн 2: line, error_buffer = error_buffer.split('\n', 1)
pattern2 = r"line, error_buffer = error_buffer\\.split\\('\\n', 1\\)"
replacement2 = r"line, error_buffer = error_buffer.split('\\\\n', 1)"

# Выполняем замены
content = re.sub(pattern1, replacement1, content)
content = re.sub(pattern2, replacement2, content)

# Также проверим и исправим другие возможные случаи
# Например, в коде агента может быть аналогичная проблема

# Сохраняем исправленный файл
with open('/mnt/shared/Новая папка/penelope/penelope_fixed.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Файл исправлен и сохранен как penelope_fixed.py")
