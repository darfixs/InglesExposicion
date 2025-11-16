#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

with open('pantalla2.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the broken spec-value span - multiline replacement
pattern = r'<span class="spec-value">Ryzen 7 9800X3D.*?180Hz\.</p>'
replacement = '''<span class="spec-value">Ryzen 7 9800X3D • RTX 4060 Ti • 32GB • 1TB NVMe • B550 WiFi • 240mm AIO • 750W Gold • ARGB Case • 24" 180Hz</span>
                </div>
            </div>'''

content = re.sub(pattern, replacement, content, flags=re.DOTALL)

with open('pantalla2.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed HTML structure")
