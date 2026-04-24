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
import traceback

SITE_DIR = '/app/site'
NOTEBOOK_DIR = '/app/notebooks'
PAPERS_DIR = '/app/past_papers'
DEMOS_DIR = '/app/demos'
DOWNLOADS_DIR = '/app/site/downloads'

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
__DEMOS__
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

# Shared PDF link + print media CSS — used by both notebook and past paper pages.
# @media print flips the dark theme to light so the generated PDF is readable and printable,
# and hides the toggle bar entirely so it doesn't leak into the PDF.
_PRINT_AND_PDF_CSS = '''
.toggle-bar .spacer { flex: 1; }
.toggle-bar a.pdf-link {
  padding: 6px 14px;
  background: rgba(255,255,255,0.08);
  border-radius: 4px;
  color: #c0c0e0 !important;
  text-decoration: none;
  font-size: 13px;
}
.toggle-bar a.pdf-link:hover { background: rgba(102,126,234,0.3); color: #fff !important; }

/* Force A4 with reasonable margins so WeasyPrint doesn't clip wide content. */
@page { size: A4; margin: 15mm 12mm; }

@media print {
  .toggle-bar { display: none !important; }
  /* Body is 960px max-width on screen, wider than A4 portrait — reset it
     so nothing overflows past the right edge of the PDF page. */
  body, .jp-Notebook, #notebook-container, .container {
    max-width: 100% !important;
    width: auto !important;
    padding: 0 !important;
    margin: 0 !important;
    background: #fff !important;
    color: #000 !important;
  }
  /* Long code lines and preformatted blocks must wrap, not overflow. */
  pre, pre code {
    white-space: pre-wrap !important;
    word-break: break-word !important;
    overflow-wrap: anywhere !important;
  }
  table {
    max-width: 100% !important;
    width: 100% !important;
    font-size: 0.9em !important;
    border-collapse: collapse !important;
    table-layout: fixed;
    word-break: break-word;
  }
  img, svg { max-width: 100% !important; height: auto !important; }

  h1 { color: #000 !important; border-bottom: 2px solid #333 !important; }
  h2 { color: #000 !important; background: none !important;
       border-left: 4px solid #333 !important; padding: 4px 10px !important; }
  h3 { color: #222 !important; }
  p, li { color: #000 !important; }
  pre { background: #f5f5f5 !important; color: #000 !important; border: 1px solid #ddd !important; }
  code { background: #f0f0f0 !important; color: #000 !important; }
  pre code { background: none !important; }
  strong { color: #000 !important; }
  blockquote { color: #555 !important; border-left: 3px solid #999 !important; }
  th { background: #e0e0e0 !important; color: #000 !important; }
  th, td { border: 1px solid #999 !important; padding: 4px 6px !important; }
  .mark-badge { background: #555 !important; color: #fff !important; }
  a { color: #000 !important; text-decoration: none !important; }
  hr { border-top: 1px solid #ccc !important; }
  h1, h2, h3 { page-break-after: avoid; }
  pre, table { page-break-inside: avoid; }
  img { page-break-inside: avoid; }
}
'''

# Base CSS shared by both modes
_BASE_CSS = '''
body { padding: 90px 20px 20px; margin: 0 auto; max-width: 960px; }
/* Fix clipped Chinese characters in headings (top strokes cut off) */
h1, h2, h3, h4, h5, h6 {
  line-height: 1.5 !important;
  padding-top: 0.2em !important;
  overflow: visible !important;
}
/* Give the first heading extra top breathing room */
.jp-Cell:first-of-type h1,
.jp-RenderedHTMLCommon h1:first-child,
#notebook-container h1:first-child {
  margin-top: 0.5em !important;
  padding-top: 0.3em !important;
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
}
.toggle-bar button:hover { background: #764ba2; }
''' + _PRINT_AND_PDF_CSS

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

def build_notebook_toggle_bar(code_visible, pdf_url=None):
    """Build toggle bar HTML for notebook pages.

    pdf_url: absolute URL to the pre-generated PDF, or None if unavailable.
    Note: the `code-hidden` class is set on the body tag at build time
    (see _add_body_class) so PDF rendering works without JS.
    """
    pdf_link = (
        f'<a href="{pdf_url}" class="pdf-link" download>&#11015; Download PDF</a>'
        if pdf_url else ''
    )
    btn_text = 'Hide Code' if code_visible else 'Show Code'
    return f'''
<div class="toggle-bar">
  <a href="/index.html">&#8592; Back to Index</a>
  <div class="spacer"></div>
  {pdf_link}
  <button id="code-toggle-btn" onclick="
    document.body.classList.toggle('code-hidden');
    this.textContent = document.body.classList.contains('code-hidden') ? 'Show Code' : 'Hide Code';
  ">{btn_text}</button>
</div>
'''


def _add_body_class(html, cls):
    """Add `cls` to the <body> tag's class attribute. WeasyPrint doesn't run
    JavaScript, so any runtime class toggling must be materialized at build time
    for it to take effect in the generated PDF."""
    def repl(m):
        tag = m.group(0)
        if re.search(r'class\s*=\s*"[^"]*"', tag):
            return re.sub(r'class\s*=\s*"([^"]*)"', lambda n: f'class="{n.group(1)} {cls}"', tag, count=1)
        return tag.replace('<body', f'<body class="{cls}"', 1)
    return re.sub(r'<body\b[^>]*>', repl, html, count=1)


def build_paper_toggle_bar(pdf_url=None):
    """Build toggle bar HTML for past paper pages."""
    pdf_link = (
        f'<a href="{pdf_url}" class="pdf-link" download>&#11015; Download PDF</a>'
        if pdf_url else ''
    )
    return f'''<div class="toggle-bar">
  <a href="/index.html">&#8592; Back to Index</a>
  <div class="spacer"></div>
  {pdf_link}
</div>'''


# Build diagnostics — written to /app/site/pdf-diag.txt at end of build so it can
# be fetched remotely to diagnose PDF generation failures without Railway log access.
_PDF_DIAG = []
_PDF_FAIL_COUNT = 0


def _log_diag(msg):
    print(msg)
    _PDF_DIAG.append(msg)


def check_weasyprint():
    """Loud smoke test at build start: verifies weasyprint imports AND can render."""
    _log_diag('=== WeasyPrint smoke test ===')
    try:
        import weasyprint
        _log_diag(f'weasyprint version: {weasyprint.__version__}')
    except Exception as e:
        _log_diag(f'import FAILED: {type(e).__name__}: {e}')
        _log_diag(traceback.format_exc())
        return False
    try:
        # Render a minimal page with CJK to exercise font resolution.
        weasyprint.HTML(
            string='<html><body><p>test 测试 English</p></body></html>'
        ).write_pdf('/tmp/_wp_smoketest.pdf')
        sz = os.path.getsize('/tmp/_wp_smoketest.pdf')
        os.remove('/tmp/_wp_smoketest.pdf')
        _log_diag(f'smoke render OK ({sz} bytes)')
        return True
    except Exception as e:
        _log_diag(f'smoke render FAILED: {type(e).__name__}: {e}')
        _log_diag(traceback.format_exc())
        return False


def generate_pdf(html_content, pdf_path, base_url=None):
    """Render HTML string to PDF via WeasyPrint. Returns True on success."""
    global _PDF_FAIL_COUNT
    try:
        import weasyprint
        os.makedirs(os.path.dirname(pdf_path), exist_ok=True)
        kwargs = {'string': html_content}
        if base_url:
            kwargs['base_url'] = base_url
        weasyprint.HTML(**kwargs).write_pdf(pdf_path)
        return True
    except Exception as e:
        _PDF_FAIL_COUNT += 1
        name = os.path.basename(pdf_path)
        msg = f'  PDF gen failed ({name}): {type(e).__name__}: {e}'
        print(msg)
        # Capture full traceback for the first 3 failures only (avoid log spam).
        if _PDF_FAIL_COUNT <= 3:
            tb = traceback.format_exc()
            _PDF_DIAG.append(msg + '\n' + tb)
        else:
            _PDF_DIAG.append(msg)
        return False


def _notebook_has_outputs(nb_path):
    """Return True if at least one code cell already has cached outputs."""
    try:
        with open(nb_path, 'r', encoding='utf-8') as f:
            nb = json.load(f)
        for cell in nb.get('cells', []):
            if cell.get('cell_type') == 'code' and cell.get('outputs'):
                return True
        return False
    except Exception:
        return False


def execute_notebook(nb_path):
    """Pre-execute a notebook in place. Skipped if already has outputs,
    which is the biggest build-time saving — re-executing every notebook
    each build cost many minutes. Set FORCE_EXEC=1 to re-execute anyway."""
    if os.environ.get('FORCE_EXEC') != '1' and _notebook_has_outputs(nb_path):
        print(f'  Skip exec (cached outputs): {os.path.basename(nb_path)}')
        return True
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


def convert_to_html(nb_path, output_dir, code_visible=False,
                    pdf_abs_path=None, pdf_rel_url=None):
    """Convert notebook to HTML; optionally also generate a companion PDF.

    Args:
        code_visible: If True, code cells are shown by default (for programming chapters)
        pdf_abs_path: Absolute path where PDF should be written. If None, no PDF is generated.
        pdf_rel_url:  URL to the PDF (relative to site root) used in the Download PDF button.
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

        if not os.path.exists(html_path):
            return None

        with open(html_path, 'r', encoding='utf-8') as f:
            content = f.read()
        # CSS goes in <head>
        content = content.replace('</head>', _HEAD_CSS + '</head>')
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

        # For non-programming chapters, code cells are hidden by a `code-hidden`
        # class normally added by JS. WeasyPrint doesn't run JS — materialize
        # the class directly on <body> so the PDF matches the on-screen view.
        # (This also removes the brief "flash of visible code" on page load.)
        if not code_visible:
            content = _add_body_class(content, 'code-hidden')

        # Generate PDF BEFORE injecting the toggle bar so the PDF content stays clean.
        # @media print would hide the bar anyway, but skipping it avoids WeasyPrint
        # ever laying out UI chrome that will be discarded.
        pdf_ok = False
        if pdf_abs_path:
            pdf_ok = generate_pdf(content, pdf_abs_path, base_url=html_path)

        # Now inject toggle bar with the download link (only if PDF generation succeeded).
        toggle_bar = build_notebook_toggle_bar(
            code_visible,
            pdf_url=pdf_rel_url if pdf_ok else None,
        )
        body_match = re.search(r'<body[^>]*>', content)
        if body_match:
            insert_pos = body_match.end()
            content = content[:insert_pos] + '\n' + toggle_bar + content[insert_pos:]

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

    # Run WeasyPrint smoke test up front so any fatal config issue is
    # visible at the top of the build log and captured in pdf-diag.txt.
    check_weasyprint()

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
            nb_basename = os.path.splitext(os.path.basename(nb_path))[0]
            pdf_abs_path = os.path.join(DOWNLOADS_DIR, ch_dir, nb_basename + '.pdf')
            pdf_rel_url = f'/downloads/{ch_dir}/{nb_basename}.pdf'
            html_path = convert_to_html(
                nb_path, output_dir, code_visible=show_code,
                pdf_abs_path=pdf_abs_path, pdf_rel_url=pdf_rel_url,
            )
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
    demos_html = build_demos()

    # Build index.html
    index_html = INDEX_TEMPLATE.replace('__CHAPTERS__', '\n'.join(chapters_html))
    index_html = index_html.replace('__PAST_PAPERS__', papers_html)
    index_html = index_html.replace('__DEMOS__', demos_html)
    index_path = os.path.join(SITE_DIR, 'index.html')
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(index_html)
    print(f'\n✅ Site built at {SITE_DIR}')
    print(f'   Index: {index_path}')

    # Write PDF build diagnostics to a known URL so the site operator can
    # fetch /pdf-diag.txt after deploy and see exactly why generation failed.
    _log_diag(f'\nPDF generation failures: {_PDF_FAIL_COUNT}')
    diag_path = os.path.join(SITE_DIR, 'pdf-diag.txt')
    with open(diag_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(_PDF_DIAG))
    print(f'   PDF diag: {diag_path}')


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
''' + _PRINT_AND_PDF_CSS + '''
</style>
</head>
<body>
__TOGGLE_BAR__
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


HOMEWORK_ANSWER_PASSWORD = '123456!'

# Template for password-protected homework answer pages
PROTECTED_HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>__TITLE__ (Protected)</title>
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
#password-gate {
  text-align: center; padding: 80px 20px;
}
#password-gate h2 { text-align: center; border: none; background: none; color: #fff; font-size: 1.5em; }
#password-gate input {
  padding: 12px 20px; font-size: 16px; border-radius: 8px; border: 2px solid #667eea;
  background: rgba(255,255,255,0.05); color: #fff; margin: 20px 10px; width: 250px;
  outline: none;
}
#password-gate input:focus { border-color: #764ba2; }
#password-gate button {
  padding: 12px 30px; font-size: 16px; cursor: pointer;
  background: linear-gradient(135deg, #667eea, #764ba2); color: #fff;
  border: none; border-radius: 8px;
}
#password-gate button:hover { opacity: 0.9; }
#password-gate .error { color: #e74c3c; margin-top: 10px; display: none; }
#answer-content { display: none; }
''' + _PRINT_AND_PDF_CSS + '''
</style>
</head>
<body>
<div class="toggle-bar">
  <a href="/index.html">&#8592; Back to Index</a>
</div>
<div id="password-gate">
  <h2>__TITLE__</h2>
  <p style="color:#8888aa;margin:10px 0 30px;">This content is password-protected / 此内容需要密码访问</p>
  <div>
    <input type="password" id="pwd-input" placeholder="Enter password / 输入密码"
           onkeydown="if(event.key==='Enter')document.getElementById('pwd-btn').click()">
    <button id="pwd-btn" onclick="tryUnlock()">Unlock</button>
  </div>
  <p class="error" id="pwd-error">Incorrect password / 密码错误</p>
</div>
<div id="answer-content"></div>
<script>
var encData = "__ENCRYPTED__";
var passHash = "__PASSHASH__";
async function sha256(msg) {
  var buf = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(msg));
  return Array.from(new Uint8Array(buf)).map(function(b){return b.toString(16).padStart(2,'0')}).join('');
}
function xorDecrypt(data, key) {
  var raw = atob(data);
  var rawBytes = new Uint8Array(raw.length);
  for (var i = 0; i < raw.length; i++) rawBytes[i] = raw.charCodeAt(i);
  var keyBytes = new TextEncoder().encode(key);
  var dec = new Uint8Array(rawBytes.length);
  for (var i = 0; i < rawBytes.length; i++) dec[i] = rawBytes[i] ^ keyBytes[i % keyBytes.length];
  return new TextDecoder().decode(dec);
}
async function tryUnlock() {
  var pwd = document.getElementById('pwd-input').value;
  var hash = await sha256(pwd);
  if (hash === passHash) {
    var content = xorDecrypt(encData, pwd);
    document.getElementById('answer-content').innerHTML = content;
    document.getElementById('answer-content').style.display = 'block';
    document.getElementById('password-gate').style.display = 'none';
  } else {
    var err = document.getElementById('pwd-error');
    err.style.display = 'block';
    setTimeout(function(){ err.style.display = 'none'; }, 2000);
  }
}
</script>
</body>
</html>'''


def encrypt_content(html_content, password):
    """XOR encrypt HTML content with password, return base64."""
    import base64
    key = password.encode('utf-8')
    data = html_content.encode('utf-8')
    encrypted = bytes([data[i] ^ key[i % len(key)] for i in range(len(data))])
    return base64.b64encode(encrypted).decode('ascii')


def get_password_hash(password):
    """SHA-256 hash of password."""
    import hashlib
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


def build_demos():
    """Copy demo HTML files to site and return index section."""
    import shutil
    if not os.path.isdir(DEMOS_DIR):
        print('\nNo demos directory found, skipping.')
        return ''

    demos_output = os.path.join(SITE_DIR, 'demos')
    os.makedirs(demos_output, exist_ok=True)

    demo_files = sorted(glob.glob(os.path.join(DEMOS_DIR, '*.html')))
    if not demo_files:
        print('\nNo demo HTML files found.')
        return ''

    print(f'\nCopying demos ({len(demo_files)} files)...')

    DEMO_INFO = {
        'network_demo': ('Communication & Networks', 'Ch2 — Packet Switching, DNS, Topologies, TCP/IP, CSMA/CD'),
    }

    demo_links = []
    for demo_path in demo_files:
        basename = os.path.splitext(os.path.basename(demo_path))[0]
        html_name = os.path.basename(demo_path)
        dest = os.path.join(demos_output, html_name)
        shutil.copy2(demo_path, dest)
        print(f'  {html_name}')

        rel_path = f'demos/{html_name}'
        info = DEMO_INFO.get(basename)
        if info:
            display_name, subtitle = info
        else:
            display_name = basename.replace('_', ' ').title()
            subtitle = ''

        demo_links.append(
            f'<a class="lesson" href="{rel_path}">'
            f'<span class="lesson-icon">🎮</span>{display_name}'
            f'{" — " + subtitle if subtitle else ""}</a>')

    if not demo_links:
        return ''

    return f'''
<div class="section-header">
  <h2>Classroom Demos</h2>
  <p>Interactive demonstrations for classroom teaching / 课堂互动演示</p>
</div>
<div class="chapter open">
  <div class="chapter-header">
    <div class="chapter-num" style="background:linear-gradient(135deg,#00b894,#00cec9);">🎮</div>
    <div>
      <div class="chapter-title">互动演示 Interactive Demos</div>
      <div class="chapter-title-en">Visual demonstrations for key concepts</div>
    </div>
    <span class="arrow">&#9654;</span>
  </div>
  <div class="lessons">{chr(10).join(demo_links)}</div>
</div>'''


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

    # Categorize files
    questions_html = []
    answers_html = []
    homework_html = []
    hw_answers_html = []

    for md_path in md_files:
        basename = os.path.splitext(os.path.basename(md_path))[0]
        html_name = basename + '.html'
        html_path = os.path.join(papers_output, html_name)

        with open(md_path, 'r', encoding='utf-8') as f:
            md_content = f.read()

        first_line = md_content.split('\n')[0]
        title = first_line.lstrip('# ').strip() if first_line.startswith('#') else basename

        is_hw_answer = 'Homework_Answers' in basename or 'Homework_Answer' in basename

        if is_hw_answer:
            # Password-protected page — no PDF (content is encrypted).
            html_content = md_to_html(md_content)
            encrypted = encrypt_content(html_content, HOMEWORK_ANSWER_PASSWORD)
            pass_hash = get_password_hash(HOMEWORK_ANSWER_PASSWORD)
            page = PROTECTED_HTML_TEMPLATE.replace('__TITLE__', title)
            page = page.replace('__ENCRYPTED__', encrypted)
            page = page.replace('__PASSHASH__', pass_hash)
            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(page)
        else:
            # Normal page: generate PDF, then inject toggle bar with download link if OK.
            html_content = md_to_html(md_content)
            pdf_abs_path = os.path.join(DOWNLOADS_DIR, 'papers', basename + '.pdf')
            pdf_rel_url = f'/downloads/papers/{basename}.pdf'

            # Render a PDF-only version (no toggle bar) so the PDF is clean.
            pdf_page = (PAPER_HTML_TEMPLATE
                        .replace('__TITLE__', title)
                        .replace('__TOGGLE_BAR__', '')
                        .replace('__CONTENT__', html_content))
            pdf_ok = generate_pdf(pdf_page, pdf_abs_path, base_url=html_path)

            toggle_bar = build_paper_toggle_bar(pdf_rel_url if pdf_ok else None)
            page = (PAPER_HTML_TEMPLATE
                    .replace('__TITLE__', title)
                    .replace('__TOGGLE_BAR__', toggle_bar)
                    .replace('__CONTENT__', html_content))
            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(page)

        # Build link for index
        rel_path = f'past_papers/{html_name}'
        display = re.sub(r'^Ch\d*_', '', basename).replace('_', ' ')

        if is_hw_answer:
            hw_answers_html.append(
                f'<a class="lesson" href="{rel_path}">'
                f'<span class="lesson-icon">🔒</span>{display}</a>')
        elif 'Homework' in basename:
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
        print(f'  {"[PROTECTED] " if is_hw_answer else ""}{basename}.html')

    if not questions_html and not answers_html and not homework_html and not hw_answers_html:
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

    if hw_answers_html:
        sections.append(f'''
<div class="chapter">
  <div class="chapter-header">
    <div class="chapter-num" style="background:linear-gradient(135deg,#8e44ad,#9b59b6);">🔒</div>
    <div>
      <div class="chapter-title">作业答案 Homework Answers (Password Protected)</div>
      <div class="chapter-title-en">Teacher access only / 仅教师可访问</div>
    </div>
    <span class="arrow">&#9654;</span>
  </div>
  <div class="lessons">{chr(10).join(hw_answers_html)}</div>
</div>''')

    return '\n'.join(sections)


if __name__ == '__main__':
    build_site()
