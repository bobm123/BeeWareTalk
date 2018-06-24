template = '''
<!DOCTYPE html>
<html>
  <head>
    <title>{title_string}</title>
    <meta charset="utf-8">
    <style>{style_string}</style>
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
