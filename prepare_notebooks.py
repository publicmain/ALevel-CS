#!/usr/bin/env python3
"""
Prepare notebooks for presentation mode:
1. Set all code cells to source_hidden (collapsed by default in JupyterLab)
2. Insert a toggle button cell at the top of each notebook
"""
import json
import glob
import os

TOGGLE_CELL = {
    "cell_type": "code",
    "execution_count": None,
    "metadata": {
        "jupyter": {"source_hidden": True},
        "tags": ["toggle-button"],
        "editable": False
    },
    "outputs": [],
    "source": [
        "from IPython.display import HTML, display\n",
        "display(HTML('''\n",
        "<div style=\"text-align:right;padding:8px 0;\">\n",
        "<button id=\"toggle-code-btn\" style=\"\n",
        "  padding:8px 18px;font-size:14px;cursor:pointer;\n",
        "  background:#4a90d9;color:white;border:none;border-radius:5px;\n",
        "  box-shadow:0 2px 4px rgba(0,0,0,0.2);\n",
        "\" onclick=\"\n",
        "  var cells = document.querySelectorAll('.jp-Cell-inputWrapper');\n",
        "  var btn = document.getElementById('toggle-code-btn');\n",
        "  var show = btn.dataset.show !== 'true';\n",
        "  btn.dataset.show = show;\n",
        "  btn.textContent = show ? '\\u9690\\u85cf\\u4ee3\\u7801 \\ud83d\\udd12' : '\\u663e\\u793a\\u4ee3\\u7801 \\ud83d\\udd13';\n",
        "  cells.forEach(function(c){ c.style.display = show ? '' : 'none'; });\n",
        "\">\\u663e\\u793a\\u4ee3\\u7801 \\ud83d\\udd13</button>\n",
        "</div>\n",
        "'''))\n"
    ]
}

def process_notebook(path):
    with open(path, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    cells = nb.get('cells', [])

    # Remove existing toggle button cells (if re-running)
    cells = [c for c in cells if not (
        c.get('metadata', {}).get('tags') and
        'toggle-button' in c['metadata']['tags']
    )]

    # Set source_hidden on all code cells
    for cell in cells:
        if cell['cell_type'] == 'code':
            if 'metadata' not in cell:
                cell['metadata'] = {}
            if 'jupyter' not in cell['metadata']:
                cell['metadata']['jupyter'] = {}
            cell['metadata']['jupyter']['source_hidden'] = True

    # Insert toggle button at position 0
    cells.insert(0, TOGGLE_CELL.copy())

    nb['cells'] = cells

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)

    return True

if __name__ == '__main__':
    notebooks = glob.glob('notebooks/**/*.ipynb', recursive=True)
    count = 0
    for nb_path in notebooks:
        if process_notebook(nb_path):
            count += 1
            count += 1
    print('Total: ' + str(count) + ' notebooks processed')
