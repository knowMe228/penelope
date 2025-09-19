#!/usr/bin/env python3

# Более точный скрипт для исправления синтаксических ошибок в penelope.py

# Читаем файл построчно
with open('/mnt/shared/Новая папка/penelope/penelope.py', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

# Исправляем конкретные строки
# Строка 3459: while '\n' in error_buffer:
# Строка 3460: \tline, error_buffer = error_buffer.split('\n', 1)
# Строка 3472: while '\n' in error_buffer:
# Строка 3473: \tline, error_buffer = error_buffer.split('\n', 1)
# Строка 3481: while '\n' in error_buffer:
# Строка 3482: \tline, error_buffer = error_buffer.split('\n', 1)

# Найдем эти строки по содержимому и заменим их
for i, line in enumerate(lines):
    # Исправляем while '\n' in error_buffer:
    if "while '" in line and "\\n" in line and " in error_buffer:" in line:
        # Это правильная строка, пропускаем
        pass
    elif "while '" in line and "\n" in line and " in error_buffer:" in line:
        # Это неправильная строка, исправляем
        lines[i] = line.replace("'\n'", "'\\n'")
    
    # Исправляем line, error_buffer = error_buffer.split('\n', 1)
    if "line, error_buffer = error_buffer.split('" in line and "\\n" in line:
        # Это правильная строка, пропускаем
        pass
    elif "line, error_buffer = error_buffer.split('" in line and "\n" in line:
        # Это неправильная строка, исправляем
        lines[i] = line.replace("'\n'", "'\\n'")

# Также проверим строку с stderr_stream << (str(sys.exc_info()[1]) + '\n').encode()
# в районе 3414 строки
for i, line in enumerate(lines):
    if "stderr_stream << (str(sys.exc_info()[1]) + '\\\\\\\\n'" in line:
        # Это правильная строка
        pass
    elif "stderr_stream << (str(sys.exc_info()[1]) + '\\n'" in line:
        # Это неправильная строка, исправляем
        lines[i] = line.replace("'\\n'", "'\\\\n'")

# Сохраняем исправленный файл
with open('/mnt/shared/Новая папка/penelope/penelope_fixed.py', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Файл исправлен и сохранен как penelope_fixed.py")