with open ('blog.txt', 'r') as file: text = file.read()

html_text = '<html>\n<head>\n<title>Blog</title>\n<link rel="stylesheet" href="https://ashi.nekoweb.org/style.css">\n</head><body> \n <div class="nav-header"><nav>\n<a href="https://ashi.nekoweb.org/index.html">/home/</a>\n<a href="https://ashi.nekoweb.org/home/about.html">/about/</a>\n<a href="https://ashi.nekoweb.org/home/blog.html">/blog/</a>\n<a href="https://ashi.nekoweb.org/home/contact.html">/contact/</a>\n<a href="https://ashi.nekoweb.org/home/games.html">/games/</a></nav></div>\n<div class="header"><br><p>\n<span style="color: #eb6f92;"> ~/home/blog/posts</span></p></div>\n<div class="blog-post">\n'

for line in text.split('n'): 
    html_text += f'<p>{line}</p>\n'

html_text +='</div>\n</body>\n</html>'

import time

base_filename = 'blog.html'
timestamp = time.strftime('%Y|M%m|D%d|H%H')
new_filename = f"{base_filename.rsplit('.', 1)[0]}_{timestamp}.{base_filename.rsplit('.', 1)[-1]}"

with open(new_filename, "w") as file:
    file.write(html_text)