#!/bin/bash
PORT=${PORT:-8080}
echo "Starting JupyterLab on port $PORT..."
exec jupyter lab --config=/root/.jupyter/jupyter_lab_config.py --allow-root
