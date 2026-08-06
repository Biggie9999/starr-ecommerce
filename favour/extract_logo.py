import re
import base64

with open('email_template.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find the base64 image tag
match = re.search(r'<img src="data:image/png;base64,([^"]+)"([^>]*)>', html)
if match:
    # Remove all characters that are not valid base64
    b64_data = re.sub(r'[^A-Za-z0-9+/=]', '', match.group(1))
    
    # Pad to multiple of 4
    b64_data += "=" * ((4 - len(b64_data) % 4) % 4)
    rest_of_tag = match.group(2)
    
    # Decode and save to logo.png
    with open('logo.png', 'wb') as f:
        f.write(base64.b64decode(b64_data))
        
    # Replace in HTML
    new_img_tag = f'<img src="cid:logo.png"{rest_of_tag}>'
    new_html = html[:match.start()] + new_img_tag + html[match.end():]
    
    with open('email_template.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Successfully extracted logo.png and updated email_template.html")
else:
    print("Could not find the base64 image.")
