import re

file_path = r'c:\Users\darek\VS Code\Inglés\pantalla2.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Simple pattern to find the problematic section
# Just look for the span with all the components in one line
start_marker = '<span class="spec-value">Ryzen 7 9800X3D'
end_marker = '180Hz.</p>'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker, start_idx)

if start_idx != -1 and end_idx != -1:
    # Extract the part to replace
    end_idx += len(end_marker)
    
    # Build the replacement
    replacement = '''<span class="spec-value">Ryzen 7 9800X3D</span>
                </div>
                <div class="spec-item">
                    <span class="spec-label">Graphics</span>
                    <span class="spec-value">RTX 4060 Ti</span>
                </div>
                <div class="spec-item">
                    <span class="spec-label">Memory</span>
                    <span class="spec-value">32GB DDR4</span>
                </div>
                <div class="spec-item">
                    <span class="spec-label">Storage</span>
                    <span class="spec-value">1TB NVMe</span>
                </div>
                <div class="spec-item">
                    <span class="spec-label">Motherboard</span>
                    <span class="spec-value">B550 WiFi</span>
                </div>
                <div class="spec-item">
                    <span class="spec-label">Cooling</span>
                    <span class="spec-value">240mm AIO</span>
                </div>
                <div class="spec-item">
                    <span class="spec-label">Power Supply</span>
                    <span class="spec-value">750W Gold</span>
                </div>
                <div class="spec-item">
                    <span class="spec-label">Case</span>
                    <span class="spec-value">ARGB Case</span>
                </div>
                <div class="spec-item">
                    <span class="spec-label">Monitor</span>
                    <span class="spec-value">24" 180Hz</span>
                </div>'''
    
    # Replace
    content = content[:start_idx] + replacement + content[end_idx:]
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Archivo actualizado correctamente. Reemplazó de {start_idx} a {end_idx}")
else:
    print(f"No se encontró el patrón. Start:{start_idx}, End:{end_idx}")
