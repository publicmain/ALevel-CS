FROM python:3.11-slim

# Install system dependencies: Chinese fonts + WeasyPrint runtime libs
# fontconfig (not just libfontconfig1) provides fc-cache + fonts.conf —
# without it WeasyPrint can't resolve the CJK fonts and every render fails.
RUN apt-get update && apt-get install -y --no-install-recommends \
    fonts-wqy-zenhei \
    fonts-wqy-microhei \
    fonts-noto-cjk \
    fontconfig \
    libpango-1.0-0 \
    libpangoft2-1.0-0 \
    libharfbuzz0b \
    libfontconfig1 \
    && rm -rf /var/lib/apt/lists/* \
    && fc-cache -f

# Set working directory
WORKDIR /app

# Copy requirements and install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Verify WeasyPrint can render at build time — fail fast if system libs
# or Python package versions are incompatible.
RUN python3 -c "import weasyprint; weasyprint.HTML(string='<p>smoke 测试</p>').write_pdf('/tmp/_wp.pdf'); print('weasyprint smoke test OK')"

# Configure matplotlib to use Chinese fonts
RUN python3 -c "import matplotlib; import os; rc_path = matplotlib.matplotlib_fname(); f = open(rc_path, 'r'); content = f.read(); f.close(); content = content.replace('#font.sans-serif:', 'font.sans-serif: WenQuanYi Zen Hei, WenQuanYi Micro Hei, Noto Sans CJK SC, DejaVu Sans,'); content = content.replace('#axes.unicode_minus: True', 'axes.unicode_minus: False'); f = open(rc_path, 'w'); f.write(content); f.close(); print('matplotlibrc configured for Chinese fonts')" && \
    rm -rf /root/.cache/matplotlib /root/.matplotlib/fontlist-*.json

# Copy notebooks, past papers, demos, and build script
COPY notebooks/ /app/notebooks/
COPY past_papers/ /app/past_papers/
COPY demos/ /app/demos/
COPY build_site.py /app/build_site.py
COPY serve.py /app/serve.py

# Build static HTML site (execute notebooks + convert to HTML)
ENV MPLBACKEND=Agg
RUN python3 build_site.py

# Expose port
EXPOSE 8080

CMD ["python3", "/app/serve.py"]
