#!/usr/bin/env python3

# Ручной скрипт для исправления синтаксических ошибок в penelope.py

# Открываем исходный файл в бинарном режиме
with open('/mnt/shared/Новая папка/penelope/penelope.py', 'rb') as f:
    content = f.read()

# Преобразуем в строку
content_str = content.decode('utf-8', errors='ignore')

# Разделим содержимое на строки и обработаем каждую
lines = content_str.split('\n')

# Ищем проблемные строки
for i in range(len(lines)):
    line = lines[i]
    
    # Проверяем, содержит ли строка проблемный паттерн
    # Проблема: у нас есть строка, которая выглядит как 
    # "while '" + "\n" + "' in error_buffer:"
    # но в реальности это две строки:
    # "while '" 
    # "' in error_buffer:"
    
    # Проверим, если текущая строка заканчивается на "while '"
    # и следующая строка начинается с "' in error_buffer:"
    if i < len(lines) - 1:
        if line.strip().endswith("while '") and lines[i+1].strip().startswith("' in error_buffer:"):
            # Это проблемное место, исправляем
            lines[i] = line.rstrip() + "\\n' in error_buffer:"
            lines[i+1] = ""
            
        # Аналогично для .split
        if line.strip().endswith(".split('") and lines[i+1].strip().startswith("', 1)"):
            # Это проблемное место, исправляем
            lines[i] = line.rstrip() + "\\n', 1)"
            lines[i+1] = ""

# Объединяем строки обратно
fixed_content = '\n'.join(lines)

# Удаляем пустые строки
lines = [line for line in fixed_content.split('\n') if line.strip()]
fixed_content = '\n'.join(lines)

# Также исправим проблему с stderr_stream
fixed_content = fixed_content.replace("stderr_stream << (str(sys.exc_info()[1]) + '\\n').encode()", 
                                   "stderr_stream << (str(sys.exc_info()[1]) + '\\\\n').encode()")

# Сохраняем исправленный файл
with open('/mnt/shared/Новая папка/penelope/penelope_fixed.py', 'w', encoding='utf-8') as f:
    f.write(fixed_content)

print("Файл исправлен и сохранен как penelope_fixed.py")