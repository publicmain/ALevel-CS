#!/usr/bin/env python3
"""Fix text alignment in matplotlib diagrams across all notebooks.

The core problem: many diagrams place text at y + small_constant instead of
centering text vertically within rectangles (y + h/2).

This script parses each code cell, finds rectangle+text pairs, and adjusts
the text y-position to be centered.
"""
import json
import glob
import re
import os
import copy


def fix_layer_loop_pattern(source_lines):
    """Fix the pattern where a loop iterates over layers with 'y' and 'h' keys,
    and text is placed at layer['y'] + constant instead of layer['y'] + layer['h']/2.

    Example broken:
        ax.text(5, layer['y'] + 0.5, layer['name'], ...)
    Fixed:
        ax.text(5, layer['y'] + layer['h']/2, layer['name'], ...)
    """
    changed = False
    new_lines = []
    for line in source_lines:
        # Match: .text(..., layer['y'] + 0.5, ...) or similar with any variable name
        m = re.search(
            r"(\.text\([^,]+,\s*)(\w+)\['y'\]\s*\+\s*[\d.]+(\s*,)",
            line
        )
        if m:
            var = m.group(2)
            old = m.group(0)
            new = f"{m.group(1)}{var}['y'] + {var}['h']/2{m.group(3)}"
            line = line.replace(old, new)
            changed = True
        new_lines.append(line)
    return new_lines, changed


def fix_stacked_boxes_pattern(source_lines):
    """Fix stacked box diagrams where rectangles are at computed y positions
    with known heights, but text uses a fixed offset.

    Looks for patterns like:
        rect = FancyBboxPatch((x, y), w, 1.0, ...)
        ax.text(cx, y + 0.3, ...)
    Where 0.3 should be 0.5 (half of height 1.0)
    """
    source = '\n'.join(source_lines)
    changed = False

    # Find FancyBboxPatch with explicit height values in loops
    # Pattern: FancyBboxPatch((expr, y_var), w_expr, h_value, ...)
    # Then text at y_var + offset where offset != h_value/2

    # First collect all patches with their heights from the source
    patch_heights = re.findall(
        r'FancyBboxPatch\(\s*\([^)]+\)\s*,\s*[\w.]+\s*,\s*([\d.]+)',
        source
    )

    if not patch_heights:
        return source_lines, False

    # If all patches share the same height, check if text offsets match h/2
    from collections import Counter
    height_counts = Counter(patch_heights)
    if len(height_counts) == 1:
        h = float(patch_heights[0])
        correct_offset = h / 2

        new_lines = []
        for line in source_lines:
            # Find text calls with y + offset
            m = re.search(r'(\.text\([^,]+,\s*\w+\s*\+\s*)([\d.]+)(\s*,)', line)
            if m:
                current_offset = float(m.group(2))
                if abs(current_offset - correct_offset) > 0.05 and current_offset < h:
                    line = line.replace(
                        m.group(0),
                        f"{m.group(1)}{correct_offset}{m.group(3)}"
                    )
                    changed = True
            new_lines.append(line)
        return new_lines, changed

    return source_lines, False


def fix_row_based_pattern(source_lines):
    """Fix diagrams where boxes are drawn row by row with variables like
    row_y, base_y, y_pos, etc. and text is offset incorrectly.

    Looks for known height constants and adjusts text offsets to h/2.
    """
    source = '\n'.join(source_lines)
    changed = False

    # Look for height assignments like: h = 0.8, box_h = 1.0, etc.
    height_vars = {}
    for m in re.finditer(r'(\w*h\w*)\s*=\s*([\d.]+)', source):
        name = m.group(1)
        val = float(m.group(2))
        if 0.3 <= val <= 3.0 and name.lower() in ('h', 'box_h', 'row_h', 'height', 'bh', 'rh'):
            height_vars[name] = val

    # Look for FancyBboxPatch height from parameters
    patch_h_matches = re.findall(
        r'FancyBboxPatch\([^)]+\)\s*,\s*[\w.]+\s*,\s*(\w+)',
        source
    )

    return source_lines, changed


def fix_notebook(nb_path):
    """Fix all diagram text alignment issues in a notebook."""
    with open(nb_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    total_fixed = 0

    for ci, cell in enumerate(nb['cells']):
        if cell['cell_type'] != 'code':
            continue

        src = ''.join(cell['source'])
        if 'add_patch' not in src or '.text(' not in src:
            continue

        lines = src.split('\n')

        # Try each fix pattern
        new_lines, c1 = fix_layer_loop_pattern(lines)
        if c1:
            lines = new_lines
            total_fixed += 1

        new_lines, c2 = fix_stacked_boxes_pattern(lines)
        if c2:
            lines = new_lines
            total_fixed += 1

        if c1 or c2:
            # Write back: convert to proper notebook source format
            new_src = '\n'.join(lines)
            # Split into proper source array for notebook JSON
            src_lines = []
            for i, line in enumerate(new_src.split('\n')):
                if i < len(new_src.split('\n')) - 1:
                    src_lines.append(line + '\n')
                else:
                    src_lines.append(line)
            cell['source'] = src_lines

    if total_fixed > 0:
        with open(nb_path, 'w', encoding='utf-8') as f:
            json.dump(nb, f, ensure_ascii=False, indent=1)
        return total_fixed
    return 0


def main():
    base = 'notebooks'
    fixed_total = 0
    files_fixed = 0

    for nb_path in sorted(glob.glob(os.path.join(base, '**', '*.ipynb'), recursive=True)):
        n = fix_notebook(nb_path)
        if n > 0:
            name = os.path.basename(os.path.dirname(nb_path)) + '/' + os.path.basename(nb_path)
            print(f'  Fixed {n} cells in {name}')
            fixed_total += n
            files_fixed += 1

    print(f'\nTotal: {fixed_total} cells fixed in {files_fixed} files')


if __name__ == '__main__':
    main()
