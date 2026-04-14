c = get_config()

import os

port = int(os.environ.get('PORT', 8080))

c.ServerApp.ip = '0.0.0.0'
c.ServerApp.port = port
c.ServerApp.open_browser = False
c.ServerApp.allow_remote_access = True
c.ServerApp.root_dir = '/app/notebooks'

# Token-based auth (set JUPYTER_TOKEN env var in Railway, or disable for public)
token = os.environ.get('JUPYTER_TOKEN', '')
if token:
    c.ServerApp.token = token
else:
    c.ServerApp.token = ''
    c.ServerApp.password = ''

c.ServerApp.allow_origin = '*'
c.ServerApp.tornado_settings = {
    'headers': {
        'Content-Security-Policy': "frame-ancestors 'self' *",
    }
}

# Disable terminal for security on public deployment
c.ServerApp.terminals_enabled = False
