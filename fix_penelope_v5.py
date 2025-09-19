#!/usr/bin/env python3

# Прямой скрипт для исправления синтаксических ошибок в penelope.py

# Читаем файл построчно
with open('/mnt/shared/Новая папка/penelope/penelope.py', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

# Создаем новый список строк
new_lines = []

# Проходим по всем строкам
for i, line in enumerate(lines):
    line_num = i + 1
    
    # Проверяем, является ли эта строка проблемной
    # Проблема: у нас есть фактический символ новой строки внутри одинарных кавычек
    # Мы ищем строку, которая содержит "while '" и " in error_buffer:" но не "\\n"
    
    if "while '" in line and " in error_buffer:" in line and "\\n" not in line:
        # Это проблемная строка, исправляем
        # Заменяем ' + \n + ' на \\n
        # Но так как у нас фактический символ новой строки, нужно быть осторожным
        
        # Проверим содержимое строки
        if "'\n" in line:
            # Заменяем
            new_line = line.replace("'\n'", "'\\n'")
            print(f"Исправлена строка {line_num}: {repr(line)} -> {repr(new_line)}")
            new_lines.append(new_line)
        else:
            new_lines.append(line)
    elif ".split('" in line and "', 1)" in line and "\\n" not in line:
        # Это вторая проблемная строка
        if "'\n" in line:
            # Заменяем
            new_line = line.replace("'\n'", "'\\n'")
            print(f"Исправлена строка {line_num}: {repr(line)} -> {repr(new_line)}")
            new_lines.append(new_line)
        else:
            new_lines.append(line)
    else:
        new_lines.append(line)

# Сохраняем исправленный файл
with open('/mnt/shared/Новая папка/penelope/penelope_fixed.py', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Файл исправлен и сохранен как penelope_fixed.py")