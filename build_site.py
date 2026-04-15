#!/usr/bin/env python3
"""
Build static HTML site from Jupyter notebooks.
1. Pre-execute all notebooks
2. Convert to HTML with code hidden by default
3. Generate index.html with chapter navigation
"""
import subprocess
import glob
import os
import json
import re

SITE_DIR = '/app/site'
NOTEBOOK_DIR = '/app/notebooks'

INDEX_TEMPLATE = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Cambridge A-Level Computer Science (9618) - AS Level</title>
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans CJK SC', sans-serif;
  background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
  min-height: 100vh; color: #e0e0e0;
}
.header {
  text-align: center; padding: 50px 20px 30px;
  background: rgba(255,255,255,0.03);
  border-bottom: 1px solid rgba(255,255,255,0.08);
}
.header h1 { font-size: 2.2em; color: #fff; margin-bottom: 10px; }
.header p { font-size: 1.1em; color: #a0a0c0; }
.container { max-width: 1100px; margin: 0 auto; padding: 30px 20px 60px; }
.chapter {
  background: rgba(255,255,255,0.05); border-radius: 12px;
  margin-bottom: 20px; overflow: hidden;
  border: 1px solid rgba(255,255,255,0.08);
  transition: transform 0.2s, box-shadow 0.2s;
}
.chapter:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(0,0,0,0.3);
}
.chapter-header {
  padding: 18px 24px; cursor: pointer;
  display: flex; align-items: center; gap: 15px;
  background: rgba(255,255,255,0.03);
}
.chapter-header:hover { background: rgba(255,255,255,0.07); }
.chapter-num {
  background: linear-gradient(135deg, #667eea, #764ba2);
  color: #fff; width: 44px; height: 44px; border-radius: 10px;
  display: flex; align-items: center; justify-content: center;
  font-weight: bold; font-size: 1.2em; flex-shrink: 0;
}
.chapter-title { font-size: 1.15em; color: #fff; }
.chapter-title-en { font-size: 0.85em; color: #8888aa; margin-top: 2px; }
.arrow { margin-left: auto; color: #666; transition: transform 0.3s; font-size: 1.2em; }
.chapter.open .arrow { transform: rotate(90deg); }
.lessons { display: none; padding: 0 24px 16px; }
.chapter.open .lessons { display: block; }
.lesson {
  display: block; padding: 12px 16px; margin: 6px 0;
  background: rgba(255,255,255,0.04); border-radius: 8px;
  text-decoration: none; color: #c0c0e0;
  border: 1px solid rgba(255,255,255,0.06);
  transition: all 0.2s;
}
.lesson:hover {
  background: rgba(102, 126, 234, 0.15);
  color: #fff; border-color: rgba(102, 126, 234, 0.3);
}
.lesson-icon { margin-right: 8px; }
.footer {
  text-align: center; padding: 30px;
  color: #555; font-size: 0.85em;
}
</style>
</head>
<body>
<div class="header">
  <h1>Cambridge A-Level Computer Science</h1>
  <p>Cambridge International AS Level (9618) - Interactive Course Materials</p>
</div>
<div class="container">
__CHAPTERS__
</div>
<div class="footer">
  <p>Cambridge International AS & A Level Computer Science (9618)</p>
</div>
<script>
document.querySelectorAll('.chapter-header').forEach(h => {
  h.addEventListener('click', () => h.parentElement.classList.toggle('open'));
});
</script>
</body>
</html>'''

CHAPTER_INFO = {
    '1': ('Information Representation', 'AS Level Paper 1'),
    '2': ('Communication & Networks', 'AS Level Paper 1'),
    '3': ('Hardware', 'AS Level Paper 1'),
    '4': ('Processor Fundamentals', 'AS Level Paper 1'),
    '5': ('System Software', 'AS Level Paper 1'),
    '6': ('Security & Data Integrity', 'AS Level Paper 1'),
    '7': ('Ethics & Intellectual Property', 'AS Level Paper 1'),
    '8': ('Databases', 'AS Level Paper 2'),
    '9': ('Algorithm Design & Problem-solving', 'AS Level Paper 2'),
    '10': ('Data Types & Structures', 'AS Level Paper 2'),
    '11': ('Programming', 'AS Level Paper 2'),
    '12': ('Software Development', 'AS Level Paper 2'),
}

# Custom CSS to inject into converted HTML for code toggle
CUSTOM_CSS = '''
<style>
/* Only hide CODE cell inputs, keep markdown text visible */
.jp-CodeCell .jp-Cell-inputWrapper,
.jp-CodeCell .jp-InputArea,
div.code_cell div.input,
div.code_cell div.input_area {
  display: none;
}
body { padding: 20px; }
/* Center content */
#notebook-container, .jp-Notebook, .jp-Cell, body > div:not(.toggle-bar) {
  max-width: 900px; margin-left: auto; margin-right: auto;
}
.jp-RenderedHTMLCommon, .rendered_html, .text_cell_render {
  text-align: center;
}
.jp-RenderedHTMLCommon ul, .jp-RenderedHTMLCommon ol,
.rendered_html ul, .rendered_html ol {
  display: inline-block; text-align: left;
}
.jp-RenderedHTMLCommon table, .rendered_html table {
  margin-left: auto; margin-right: auto;
}
.jp-OutputArea-output, .output_subarea {
  display: flex; flex-direction: column; align-items: center;
}
.jp-OutputArea-output img, .output_subarea img,
.jp-OutputArea-output svg, .output_subarea svg {
  max-width: 100%;
}
.toggle-bar {
  position: fixed; top: 0; left: 0; right: 0; z-index: 9999;
  background: linear-gradient(135deg, #302b63, #24243e);
  padding: 8px 20px; display: flex; align-items: center;
  box-shadow: 0 2px 10px rgba(0,0,0,0.3); gap: 15px;
}
.toggle-bar a {
  color: #a0a0c0; text-decoration: none; font-size: 14px;
}
.toggle-bar a:hover { color: #fff; }
.toggle-bar button {
  padding: 6px 16px; font-size: 13px; cursor: pointer;
  background: #667eea; color: #fff; border: none; border-radius: 4px;
  margin-left: auto;
}
.toggle-bar button:hover { background: #764ba2; }
#notebook-container, .jp-Notebook, body > div { padding-top: 50px !important; }
</style>
<div class="toggle-bar">
  <a href="/index.html">&#8592; Back to Index</a>
  <button onclick="
    var inputs = document.querySelectorAll('.jp-CodeCell .jp-Cell-inputWrapper, .jp-CodeCell .jp-InputArea, div.code_cell div.input');
    var show = this.dataset.show !== 'true';
    this.dataset.show = show;
    this.textContent = show ? 'Hide Code' : 'Show Code';
    inputs.forEach(function(el){ el.style.display = show ? 'block' : 'none'; });
  ">Show Code</button>
</div>
'''


def execute_notebook(nb_path):
    """Pre-execute a notebook in place."""
    print(f'  Executing: {os.path.basename(nb_path)}')
    try:
        subprocess.run([
            'jupyter', 'nbconvert',
            '--execute', '--inplace', '--to', 'notebook',
            '--allow-errors',
            '--ExecutePreprocessor.timeout=120',
            nb_path
        ], check=True, capture_output=True, timeout=180)
        return True
    except Exception as e:
        print(f'  Warning: execution had issues for {nb_path}')
        return False


def convert_to_html(nb_path, output_dir):
    """Convert notebook to HTML."""
    os.makedirs(output_dir, exist_ok=True)
    basename = os.path.splitext(os.path.basename(nb_path))[0]
    html_path = os.path.join(output_dir, basename + '.html')

    try:
        subprocess.run([
            'jupyter', 'nbconvert',
            '--to', 'html',
            '--output-dir', output_dir,
            nb_path
        ], check=True, capture_output=True, timeout=60)

        # Inject custom CSS/JS for toggle bar
        if os.path.exists(html_path):
            with open(html_path, 'r', encoding='utf-8') as f:
                content = f.read()
            content = content.replace('<body', '<body style="padding-top:50px"')
            content = content.replace('</head>', CUSTOM_CSS + '</head>')
            # Fix internal links: .ipynb -> .html
            content = content.replace('.ipynb"', '.html"')
            content = content.replace('.ipynb#', '.html#')
            content = content.replace(".ipynb'", ".html'")
            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(content)
        return html_path
    except Exception as e:
        print(f'  Warning: conversion failed for {nb_path}')
        return None


def extract_chapter_num(dirname):
    """Extract chapter number from directory name like '第1章_信息表示'."""
    m = re.search(r'第(\d+)章', dirname)
    return int(m.group(1)) if m else 999


def extract_chapter_cn_title(dirname):
    """Extract Chinese title from directory name."""
    m = re.search(r'第\d+章[_]?(.*)', dirname)
    return m.group(1) if m else dirname


def build_site():
    os.makedirs(SITE_DIR, exist_ok=True)

    # Find all chapter directories
    chapter_dirs = sorted(
        [d for d in os.listdir(NOTEBOOK_DIR)
         if os.path.isdir(os.path.join(NOTEBOOK_DIR, d)) and '第' in d],
        key=extract_chapter_num
    )

    chapters_html = []

    for ch_dir in chapter_dirs:
        ch_num = extract_chapter_num(ch_dir)
        ch_cn_title = extract_chapter_cn_title(ch_dir)
        ch_en_title = CHAPTER_INFO.get(str(ch_num), ('', ''))[0]
        ch_path = os.path.join(NOTEBOOK_DIR, ch_dir)
        output_dir = os.path.join(SITE_DIR, ch_dir)

        print(f'\nChapter {ch_num}: {ch_cn_title}')

        # Find notebooks in this chapter
        notebooks = sorted(glob.glob(os.path.join(ch_path, '*.ipynb')))

        lessons_html = []
        for nb_path in notebooks:
            # Execute notebook
            execute_notebook(nb_path)

            # Convert to HTML
            html_path = convert_to_html(nb_path, output_dir)
            if html_path:
                nb_name = os.path.splitext(os.path.basename(nb_path))[0]
                # Clean up display name
                display_name = re.sub(r'^\d+[_\s]*', '', nb_name)
                if not display_name:
                    display_name = nb_name
                rel_path = os.path.relpath(html_path, SITE_DIR).replace('\\', '/')
                lessons_html.append(
                    f'<a class="lesson" href="{rel_path}">'
                    f'<span class="lesson-icon">📖</span>{display_name}</a>'
                )

        lessons_block = '\n'.join(lessons_html)
        chapters_html.append(f'''
<div class="chapter">
  <div class="chapter-header">
    <div class="chapter-num">{ch_num}</div>
    <div>
      <div class="chapter-title">{ch_cn_title}</div>
      <div class="chapter-title-en">{ch_en_title}</div>
    </div>
    <span class="arrow">&#9654;</span>
  </div>
  <div class="lessons">{lessons_block}</div>
</div>''')

    # Build index.html
    index_html = INDEX_TEMPLATE.replace('__CHAPTERS__', '\n'.join(chapters_html))
    index_path = os.path.join(SITE_DIR, 'index.html')
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(index_html)
    print(f'\n✅ Site built at {SITE_DIR}')
    print(f'   Index: {index_path}')


if __name__ == '__main__':
    build_site()
