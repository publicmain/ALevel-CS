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
PAPERS_DIR = '/app/past_papers'

INDEX_TEMPLATE = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Cambridge A-Level Computer Science (9618) - AS & A2 Level</title>
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
.section-header {
  text-align: center; padding: 20px 0 10px;
  margin-top: 30px; margin-bottom: 10px;
  border-top: 1px solid rgba(255,255,255,0.1);
}
.section-header:first-child { margin-top: 0; border-top: none; }
.section-header h2 {
  font-size: 1.4em; color: #a0a0ff;
  letter-spacing: 2px; text-transform: uppercase;
}
.section-header p { color: #7070a0; font-size: 0.9em; margin-top: 4px; }
.footer {
  text-align: center; padding: 30px;
  color: #555; font-size: 0.85em;
}
</style>
</head>
<body>
<div class="header">
  <h1>Cambridge A-Level Computer Science</h1>
  <p>Cambridge International AS & A2 Level (9618) - Interactive Course Materials</p>
</div>
<div class="container">
__CHAPTERS__
__PAST_PAPERS__
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
    '13': ('Advanced Data Representation', 'A2 Level Paper 3'),
    '14': ('Communication & Internet Technologies', 'A2 Level Paper 3'),
    '15': ('Hardware & Virtual Machines', 'A2 Level Paper 3'),
    '16': ('Advanced System Software', 'A2 Level Paper 3'),
    '17': ('Advanced Security', 'A2 Level Paper 3'),
    '18': ('Artificial Intelligence', 'A2 Level Paper 3'),
    '19': ('Computational Thinking & Problem-solving', 'A2 Level Paper 4'),
    '20': ('Advanced Programming', 'A2 Level Paper 4'),
}

# Chapters where code should be VISIBLE by default (programming-heavy)
CODE_VISIBLE_CHAPTERS = {'8', '9', '10', '11', '12', '16', '18', '19', '20'}

# Base CSS shared by both modes
_BASE_CSS = '''
body { padding: 20px; margin: 0 auto; max-width: 960px; }
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
'''

# CSS that goes in <head> - shared by both modes
_HEAD_CSS = '''
<style>
/* Hide CODE cell inputs when body has .code-hidden class */
body.code-hidden .jp-CodeCell .jp-Cell-inputWrapper,
body.code-hidden .jp-CodeCell .jp-InputArea,
body.code-hidden div.code_cell div.input,
body.code-hidden div.code_cell div.input_area {
  display: none !important;
}
/* Hide the old in-notebook toggle button */
.celltag_toggle-button { display: none !important; }
#toggle-code-btn { display: none !important; }
''' + _BASE_CSS + '''
</style>
'''

# Toggle bar HTML that goes right after <body> tag
_TOGGLE_BAR_HIDDEN = '''
<div class="toggle-bar">
  <a href="/index.html">&#8592; Back to Index</a>
  <button id="code-toggle-btn" onclick="
    document.body.classList.toggle('code-hidden');
    this.textContent = document.body.classList.contains('code-hidden') ? 'Show Code' : 'Hide Code';
  ">Show Code</button>
</div>
<script>document.body.classList.add('code-hidden');</script>
'''

_TOGGLE_BAR_VISIBLE = '''
<div class="toggle-bar">
  <a href="/index.html">&#8592; Back to Index</a>
  <button id="code-toggle-btn" onclick="
    document.body.classList.toggle('code-hidden');
    this.textContent = document.body.classList.contains('code-hidden') ? 'Show Code' : 'Hide Code';
  ">Hide Code</button>
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


def convert_to_html(nb_path, output_dir, code_visible=False):
    """Convert notebook to HTML.

    Args:
        code_visible: If True, code cells are shown by default (for programming chapters)
    """
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
            # CSS goes in <head>
            content = content.replace('</head>', _HEAD_CSS + '</head>')
            # Toggle bar + script go right after <body ...> tag
            toggle_bar = _TOGGLE_BAR_VISIBLE if code_visible else _TOGGLE_BAR_HIDDEN
            body_match = re.search(r'<body[^>]*>', content)
            if body_match:
                insert_pos = body_match.end()
                content = content[:insert_pos] + '\n' + toggle_bar + content[insert_pos:]
            # Remove inline display styles on code cells set by old toggle
            content = re.sub(
                r'(class="jp-Cell-inputWrapper"[^>]*) style="display:\s*\w+;?"',
                r'\1',
                content
            )
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
    added_as_header = False
    added_a2_header = False

    for ch_dir in chapter_dirs:
        ch_num = extract_chapter_num(ch_dir)

        # Insert section headers
        if ch_num <= 12 and not added_as_header:
            chapters_html.append('''
<div class="section-header">
  <h2>AS Level</h2>
  <p>Papers 1 & 2 — Sections 1-12</p>
</div>''')
            added_as_header = True
        elif ch_num >= 13 and not added_a2_header:
            chapters_html.append('''
<div class="section-header">
  <h2>A2 Level</h2>
  <p>Papers 3 & 4 — Sections 13-20</p>
</div>''')
            added_a2_header = True
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

            # Convert to HTML (show code for programming chapters)
            show_code = str(ch_num) in CODE_VISIBLE_CHAPTERS
            html_path = convert_to_html(nb_path, output_dir, code_visible=show_code)
            if html_path:
                nb_name = os.path.splitext(os.path.basename(nb_path))[0]
                # Clean up display name
                display_name = re.sub(r'^\d+[_\s]*', '', nb_name)
                if not display_name:
                    display_name = nb_name
                rel_path = os.path.relpath(html_path, SITE_DIR).replace('\\', '/')
                icon = '💻' if show_code else '📖'
                lessons_html.append(
                    f'<a class="lesson" href="{rel_path}">'
                    f'<span class="lesson-icon">{icon}</span>{display_name}</a>'
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

    # Build past papers section
    papers_html = build_past_papers()

    # Build index.html
    index_html = INDEX_TEMPLATE.replace('__CHAPTERS__', '\n'.join(chapters_html))
    index_html = index_html.replace('__PAST_PAPERS__', papers_html)
    index_path = os.path.join(SITE_DIR, 'index.html')
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(index_html)
    print(f'\n✅ Site built at {SITE_DIR}')
    print(f'   Index: {index_path}')


# Past papers HTML template for individual question pages
PAPER_HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>__TITLE__</title>
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans CJK SC', sans-serif;
  background: #1a1a2e; color: #e0e0e0;
  padding: 20px; margin: 0 auto; max-width: 960px;
  padding-top: 60px;
}
.toggle-bar {
  position: fixed; top: 0; left: 0; right: 0; z-index: 9999;
  background: linear-gradient(135deg, #302b63, #24243e);
  padding: 8px 20px; display: flex; align-items: center;
  box-shadow: 0 2px 10px rgba(0,0,0,0.3); gap: 15px;
}
.toggle-bar a { color: #a0a0c0; text-decoration: none; font-size: 14px; }
.toggle-bar a:hover { color: #fff; }
h1 { color: #fff; font-size: 1.6em; margin: 20px 0; border-bottom: 2px solid #667eea; padding-bottom: 10px; }
h2 { color: #a0a0ff; font-size: 1.3em; margin: 30px 0 15px;
     background: rgba(102,126,234,0.1); padding: 10px 15px; border-radius: 8px;
     border-left: 4px solid #667eea; }
h3 { color: #c0c0ff; font-size: 1.1em; margin: 20px 0 10px; }
p, li { line-height: 1.8; margin: 6px 0; }
blockquote { color: #8888aa; border-left: 3px solid #444; padding-left: 12px; margin: 10px 0; }
code { background: rgba(255,255,255,0.08); padding: 2px 6px; border-radius: 3px; font-size: 0.95em; }
pre { background: rgba(0,0,0,0.3); padding: 15px; border-radius: 8px; overflow-x: auto;
      margin: 10px 0; border: 1px solid rgba(255,255,255,0.1); }
pre code { background: none; padding: 0; }
hr { border: none; border-top: 1px solid rgba(255,255,255,0.1); margin: 30px 0; }
ul, ol { padding-left: 25px; }
strong { color: #fff; }
table { border-collapse: collapse; margin: 10px 0; width: 100%; }
th, td { border: 1px solid rgba(255,255,255,0.15); padding: 8px 12px; text-align: left; }
th { background: rgba(102,126,234,0.2); color: #fff; }
.mark-badge { display: inline-block; background: #667eea; color: #fff;
              padding: 2px 8px; border-radius: 12px; font-size: 0.85em; margin-left: 5px; }
</style>
</head>
<body>
<div class="toggle-bar">
  <a href="/index.html">&#8592; Back to Index</a>
</div>
__CONTENT__
</body>
</html>'''


def md_to_html(md_text):
    """Simple markdown to HTML converter for question files."""
    import html as html_mod
    lines = md_text.split('\n')
    result = []
    in_list = False
    in_pre = False

    for line in lines:
        # Code blocks
        if line.strip().startswith('```'):
            if in_pre:
                result.append('</code></pre>')
                in_pre = False
            else:
                result.append('<pre><code>')
                in_pre = True
            continue
        if in_pre:
            result.append(html_mod.escape(line))
            continue

        # Close list if needed
        if in_list and not line.strip().startswith('- ') and not line.strip().startswith('* '):
            result.append('</ul>')
            in_list = False

        # Headers
        if line.startswith('# '):
            result.append(f'<h1>{line[2:]}</h1>')
        elif line.startswith('## '):
            result.append(f'<h2>{line[3:]}</h2>')
        elif line.startswith('### '):
            result.append(f'<h3>{line[4:]}</h3>')
        elif line.startswith('> '):
            result.append(f'<blockquote>{line[2:]}</blockquote>')
        elif line.strip().startswith('- ') or line.strip().startswith('* '):
            if not in_list:
                result.append('<ul>')
                in_list = True
            item = line.strip()[2:]
            result.append(f'<li>{item}</li>')
        elif line.strip() == '---':
            result.append('<hr>')
        elif line.strip() == '':
            result.append('')
        else:
            # Mark allocations styling
            line = re.sub(r'\[(\d+)\s*marks?\]', r'<span class="mark-badge">\1 marks</span>', line)
            # Bold
            line = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', line)
            # Inline code
            line = re.sub(r'`(.+?)`', r'<code>\1</code>', line)
            result.append(f'<p>{line}</p>')

    if in_list:
        result.append('</ul>')
    if in_pre:
        result.append('</code></pre>')

    return '\n'.join(result)


def build_past_papers():
    """Convert past paper markdown files to HTML and return index section."""
    if not os.path.isdir(PAPERS_DIR):
        print('\nNo past_papers directory found, skipping.')
        return ''

    papers_output = os.path.join(SITE_DIR, 'past_papers')
    os.makedirs(papers_output, exist_ok=True)

    md_files = sorted(glob.glob(os.path.join(PAPERS_DIR, '*.md')))
    if not md_files:
        print('\nNo past paper markdown files found.')
        return ''

    print(f'\nBuilding past papers ({len(md_files)} files)...')

    # Categorize files into Questions, Answers, Homework
    questions_html = []
    answers_html = []
    homework_html = []

    for md_path in md_files:
        basename = os.path.splitext(os.path.basename(md_path))[0]
        html_name = basename + '.html'
        html_path = os.path.join(papers_output, html_name)

        with open(md_path, 'r', encoding='utf-8') as f:
            md_content = f.read()

        # Extract title from first line
        first_line = md_content.split('\n')[0]
        title = first_line.lstrip('# ').strip() if first_line.startswith('#') else basename

        # Convert and write
        html_content = md_to_html(md_content)
        page = PAPER_HTML_TEMPLATE.replace('__TITLE__', title).replace('__CONTENT__', html_content)
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(page)

        # Build link for index - categorize by type
        rel_path = f'past_papers/{html_name}'
        display = re.sub(r'^Ch\d*_', '', basename).replace('_', ' ')

        if 'Homework' in basename:
            homework_html.append(
                f'<a class="lesson" href="{rel_path}">'
                f'<span class="lesson-icon">📋</span>{display}</a>')
        elif 'Answers' in basename:
            answers_html.append(
                f'<a class="lesson" href="{rel_path}">'
                f'<span class="lesson-icon">✅</span>{display}</a>')
        else:
            questions_html.append(
                f'<a class="lesson" href="{rel_path}">'
                f'<span class="lesson-icon">📝</span>{display}</a>')
        print(f'  {basename}.html')

    if not questions_html and not answers_html and not homework_html:
        return ''

    sections = []
    sections.append('''
<div class="section-header">
  <h2>Past Papers & Homework</h2>
  <p>Cambridge 9618 — Questions, Answers & Assignments</p>
</div>''')

    if questions_html:
        sections.append(f'''
<div class="chapter">
  <div class="chapter-header">
    <div class="chapter-num" style="background:linear-gradient(135deg,#e67e22,#e74c3c);">📝</div>
    <div>
      <div class="chapter-title">历年考试题 Past Paper Questions</div>
      <div class="chapter-title-en">Papers 1 & 2 — Sorted by Topic (2021-2024)</div>
    </div>
    <span class="arrow">&#9654;</span>
  </div>
  <div class="lessons">{chr(10).join(questions_html)}</div>
</div>''')

    if answers_html:
        sections.append(f'''
<div class="chapter">
  <div class="chapter-header">
    <div class="chapter-num" style="background:linear-gradient(135deg,#27ae60,#2ecc71);">✅</div>
    <div>
      <div class="chapter-title">参考答案 Mark Scheme Answers</div>
      <div class="chapter-title-en">Detailed answers with marking points</div>
    </div>
    <span class="arrow">&#9654;</span>
  </div>
  <div class="lessons">{chr(10).join(answers_html)}</div>
</div>''')

    if homework_html:
        sections.append(f'''
<div class="chapter">
  <div class="chapter-header">
    <div class="chapter-num" style="background:linear-gradient(135deg,#3498db,#2980b9);">📋</div>
    <div>
      <div class="chapter-title">课后作业 Homework Assignments</div>
      <div class="chapter-title-en">Practice worksheets for each chapter</div>
    </div>
    <span class="arrow">&#9654;</span>
  </div>
  <div class="lessons">{chr(10).join(homework_html)}</div>
</div>''')

    return '\n'.join(sections)


if __name__ == '__main__':
    build_site()
