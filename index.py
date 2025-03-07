import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    message = '<h1>It works!</h1>'
    version = sys.version.split()[0]
    major_minor_version = '.'.join(version.split('.')[:2])
    response = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Python Welcome Page</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background-color: #f0f0f0;
            }}
            .container {{
                text-align: center;
            }}
            h1 {{
                color: #333;
            }}
            p {{
                color: #666;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            {message}
            <p>Python Version: {major_minor_version}</p>
        </div>
    </body>
    </html>
    """
    return [response.encode()]
