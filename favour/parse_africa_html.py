import re

with open('/Users/alt/Desktop/starr/favour/anest_africa_page.html', 'r') as f:
    html = f.read()

# Extract lines or snippets containing South Africa, Egypt, Morocco, etc.
keywords = ['south africa', 'egypt', 'morocco', 'tunisia', 'algeria', 'nigeria', 'kenya', 'africa']

lines = [l.strip() for l in re.sub(r'<[^>]+>', '\n', html).split('\n') if l.strip()]

for i, l in enumerate(lines):
    if any(k in l.lower() for k in keywords):
        print(f"Match L{i}: {l}")
        # Print surrounding 5 lines
        for j in range(max(0, i-2), min(len(lines), i+8)):
            print(f"   [{j}] {lines[j]}")
        print("-" * 50)
