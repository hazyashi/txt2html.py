with open ('blog.txt', 'r') as file: text = file.read()

html_text = '<html>\n<head>\n<title>Blog</title>\n<link rel="stylesheet" href="https://ashi.nekoweb.org/style.css">\n</head><body>\n<div class="blog-post">\n'

for line in text.split('\n'): 
    html_text += f'<p>{line}</p>\n'

html_text +='<br><a href="https://ashi.nekoweb.org/home/blog.html">return-</a></div>\n</body>\n</html>'

import time

base_filename = 'blog.html'
timestamp = time.strftime('%Y_M%m_D%d_H%H')
new_filename = f"{base_filename.rsplit('.', 1)[0]}_{timestamp}.{base_filename.rsplit('.', 1)[-1]}"

with open(new_filename, "w") as file:
    file.write(html_text)
