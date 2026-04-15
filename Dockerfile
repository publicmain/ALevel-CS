FROM python:3.11-slim

# Install system dependencies including Chinese fonts
RUN apt-get update && apt-get install -y --no-install-recommends \
    fonts-wqy-zenhei \
    fonts-wqy-microhei \
    fonts-noto-cjk \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements and install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Configure matplotlib to use Chinese fonts
RUN python3 -c "import matplotlib; import os; rc_path = matplotlib.matplotlib_fname(); f = open(rc_path, 'r'); content = f.read(); f.close(); content = content.replace('#font.sans-serif:', 'font.sans-serif: WenQuanYi Zen Hei, WenQuanYi Micro Hei, Noto Sans CJK SC, DejaVu Sans,'); content = content.replace('#axes.unicode_minus: True', 'axes.unicode_minus: False'); f = open(rc_path, 'w'); f.write(content); f.close(); print('matplotlibrc configured for Chinese fonts')" && \
    rm -rf /root/.cache/matplotlib /root/.matplotlib/fontlist-*.json

# Copy notebooks, past papers, and build script
COPY notebooks/ /app/notebooks/
COPY past_papers/ /app/past_papers/
COPY build_site.py /app/build_site.py
COPY serve.py /app/serve.py

# Build static HTML site (execute notebooks + convert to HTML)
ENV MPLBACKEND=Agg
RUN python3 build_site.py

# Expose port
EXPOSE 8080

CMD ["python3", "/app/serve.py"]
