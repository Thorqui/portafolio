with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Increase particle count
html = html.replace('const particleCount = window.innerWidth <= 768 ? 2000 : 4000;', 'const particleCount = window.innerWidth <= 768 ? 4000 : 10000;')

# Increase size of particles slightly so they are visible in a larger volume
html = html.replace('size: 0.1,', 'size: 0.25,')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
