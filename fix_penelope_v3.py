#!/usr/bin/env python3

# Очень точный скрипт для исправления синтаксических ошибок в penelope.py

# Читаем весь файл как бинарные данные, чтобы избежать проблем с кодировкой
with open('/mnt/shared/Новая папка/penelope/penelope.py', 'rb') as f:
    content = f.read()

# Преобразуем в строку, игнорируя ошибки декодирования
content_str = content.decode('utf-8', errors='ignore')

# Ищем и заменяем проблемный паттерн
# Проблема: у нас есть фактический символ новой строки внутри одинарных кавычек
# Т.е. ' + 
 + ' вместо \\n

# Заменяем ' + 
 + ' на \\n
# Это сложнее, потому что у нас фактический символ новой строки внутри строки
import re

# Ищем паттерн: while '<символ новой строки>' in error_buffer:
# и заменяем на: while '\\n' in error_buffer:
pattern1 = r"while '\n' in error_buffer:"
replacement1 = r"while '\\n' in error_buffer:"

# Ищем паттерн: .split('<символ новой строки>', 1)
# и заменяем на: .split('\\n', 1)
pattern2 = r"\.split\('\n', 1\)"
replacement2 = r".split('\\n', 1)"

# Выполняем замены
content_str = re.sub(pattern1, replacement1, content_str)
content_str = re.sub(pattern2, replacement2, content_str)

# Также проверим и исправим проблему с stderr_stream << ... \\n
# Ищем паттерн с одинарным \n и заменяем на двойной \\n
pattern3 = r"stderr_stream << \(str\(sys\.exc_info\(\)\[1\]\) \+ '\\n'\)\.encode\(\)"
replacement3 = r"stderr_stream << (str(sys.exc_info()[1]) + '\\\\n').encode()"
content_str = re.sub(pattern3, replacement3, content_str)

# Сохраняем исправленный файл
with open('/mnt/shared/Новая папка/penelope/penelope_fixed.py', 'w', encoding='utf-8') as f:
    f.write(content_str)

print("Файл исправлен и сохранен как penelope_fixed.py")