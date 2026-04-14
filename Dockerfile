FROM python:3.11-slim

# Install system dependencies including Chinese fonts
RUN apt-get update && apt-get install -y --no-install-recommends \
    fonts-wqy-zenhei \
    fonts-wqy-microhei \
    fonts-noto-cjk \
    git \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements and install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Configure matplotlib to use Chinese fonts
RUN python3 -c "import matplotlib; print(matplotlib.get_cachedir())" && \
    python3 -c "
import matplotlib
import os
# Update matplotlibrc
rc_path = matplotlib.matplotlib_fname()
with open(rc_path, 'r') as f:
    content = f.read()
content = content.replace('#font.sans-serif:', 'font.sans-serif: WenQuanYi Zen Hei, WenQuanYi Micro Hei, Noto Sans CJK SC, DejaVu Sans,')
content = content.replace('#axes.unicode_minus: True', 'axes.unicode_minus: False')
with open(rc_path, 'w') as f:
    f.write(content)
print('matplotlibrc configured for Chinese fonts')
" && \
    # Clear font cache
    rm -rf /root/.cache/matplotlib /root/.matplotlib/fontlist-*.json

# Copy notebooks
COPY notebooks/ /app/notebooks/

# Copy startup script
COPY start.sh /app/start.sh
RUN chmod +x /app/start.sh

# Create Jupyter config
RUN mkdir -p /root/.jupyter
COPY jupyter_config.py /root/.jupyter/jupyter_lab_config.py

# Expose port (Railway sets PORT env var)
EXPOSE 8080

CMD ["/app/start.sh"]
