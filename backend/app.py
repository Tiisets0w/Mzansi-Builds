from flask import Flask
import os

# Absolute paths for templates and static folders
template_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates')
static_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static')

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

# Import routes after app is defined
from backend import routes

if __name__ == "__main__":
    app.run(debug=True)