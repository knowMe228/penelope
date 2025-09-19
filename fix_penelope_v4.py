#!/usr/bin/env python3

# Very precise script to fix syntax errors in penelope.py

with open('/mnt/shared/Новая папка/penelope/penelope.py', 'rb') as f:
    content = f.read()

content_str = content.decode('utf-8', errors='ignore')

import re

# Fix: while '\n' in error_buffer: -> while '\\n' in error_buffer:
pattern1 = r"while '\\n' in error_buffer:"
replacement1 = r"while '\\\\n' in error_buffer:"

# Fix: .split('\n', 1) -> .split('\\n', 1)
pattern2 = r"\\.split\\('\\n', 1\\)"
replacement2 = r".split('\\\\n', 1)"

content_str = re.sub(pattern1, replacement1, content_str)
content_str = re.sub(pattern2, replacement2, content_str)

# Fix stderr_stream << ... \n
pattern3 = r"stderr_stream << \\(str\\(sys\\.exc_info\\(\\)\\[1\\]\\) \\+ '\\\\n'\\)\\.encode\\(\\)"
replacement3 = r"stderr_stream << (str(sys.exc_info()[1]) + '\\\\n').encode()"
content_str = re.sub(pattern3, replacement3, content_str)

with open('/mnt/shared/Новая папка/penelope/penelope_fixed.py', 'w', encoding='utf-8') as f:
    f.write(content_str)

print("File fixed and saved as penelope_fixed.py")