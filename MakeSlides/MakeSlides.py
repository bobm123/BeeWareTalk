'''
Generate slideshows from markdown that use the remark.js script

details here:
https://github.com/gnab/remark


Run it like this:
python MakeSlides.py <source_text.md> <Slidestack Title> index.html

'''

import sys
import os


template = '''
<!DOCTYPE html>
<html>
  <head>
    <title>{title_string}</title>
    <meta charset="utf-8">
    <style>{css_string}</style>
  </head>
  <body>
    <textarea id="source">{markdown_string}</textarea>

    <script src="https://remarkjs.com/downloads/remark-latest.min.js">
    </script>
    <script>
      var slideshow = remark.create();
    </script>

  </body>
</html>
'''

def main():
    if len(sys.argv)>2:
        title = sys.argv[2]
    else:
        title = 'Slides'

    with open(sys.argv[1]) as md_file:
        md_string = md_file.read()

    local_path = os.path.dirname(__file__)

    #with open(os.path.join(local_path, 'demo-style.css')) as css_file:
    csspath = os.path.join(local_path, 'demo-style.css')
    with open(csspath, encoding="utf8") as css_file:
        css_string = css_file.read()

    print(template.format(markdown_string=md_string,
                          title_string=title,
                          css_string=css_string))


