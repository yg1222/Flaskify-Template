import os

def generate_structure_and_boilerplate(base_path):
    # Define the folder structure
    structure = {
            "app": {
                "templates": ["base.html", "index.html", "login.html", "signup.html", "billing.html"],
                "static": {
                    "css": [],
                    "js": [],
                    "img": []
                },
                "blueprints": ["auth.py", "billing.py"],
                "models": ["user.py", "subscription.py"],
                "services": ["stripe_service.py"],
                "__init__.py": "",
                "config.py": "",
                "forms.py": "",
                "views.py": "",
            },
            "migrations": {},
            "tests": ["test_auth.py", "test_billing.py"],
            ".env": "",
            ".gitignore": "",
            ".dockerignore":"",
            "Dockerfile": "",
            "Pipfile": "",
            "Procfile": "",
            "README.md": "",
            "requirements.txt": "",
            "wsgi.py": ""
        }

    # Boilerplate content for some of the files
    ignores="""# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# Environment variables
.env

# Flask cache
instance/
*.sqlite3

# Logs
*.log

# Virtual environment
venv/
pip-selfcheck.json

# Pytest cache
.cache/

# Migrations
migrations/"""
    page_extensions = """{% extends "base.html" %}

    {% block title %}Home{% endblock %}

    {% block content %}
        <div class="text-center">
            <h1>Welcome to My Flask App!</h1>
            <p class="lead">This is a page in your Flask application.</p>
        </div>
    {% endblock %}
    """

    boilerplate_files = {
        "app/__init__.py": """from flask import Flask, render_template, request
from flask_mail import Mail, Message
import app.config
import logging
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

# Logging configs
log_format = '[%(asctime)s] %(levelname)s [line %(lineno)d in %(module)s]: %(message)s'
log_datefmt='%Y-%m-%d %H:%M:%S'
logging.basicConfig(
    format=log_format,
    datefmt=log_datefmt,
    level=logging.DEBUG
)

app = Flask(__name__)

# Loading configuration from config.Config
app.config.from_object(config.Config)

# Blueprints registerations
from app.blueprints.auth import auth
app.register_blueprint(auth)
from app.blueprints.billing import billing
app.register_blueprint(billing)

# Initializations
mail = Mail(app)
current_year = datetime.now().year

@app.before_request
def before_request():
    ...
    # if not access_allowed():
    #     return jsonify({"message":"Unauthorized access"}), 403

@app.route('/')
def index():
    return render_template('index.html')

    """,
        "app/config.py": """import os
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    STRIPE_API_KEY = os.environ.get('STRIPE_API_KEY')
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT'))
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = ("Display Name", "email@email.com")
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    """,
        "app/blueprints/auth.py": """from flask import Blueprint
    auth = Blueprint('auth', __name__)

    @auth.route('/login')
    def login():
        return "Login Page"

    @auth.route('/signup')
    def signup():
        return "Signup Page"
    """,
        "app/blueprints/billing.py": """from flask import Blueprint
    billing = Blueprint('billing', __name__)

    @billing.route('/billing')
    def billing_page():
        return "Billing Page"
    """,
        "app/services/stripe_service.py": """import stripe
    stripe.api_key = os.environ.get('STRIPE_API_KEY')

    def create_checkout_session():
        # Stripe integration logic
        pass
    """,
        "wsgi.py": """from app import app

if __name__ == "__main__":
    app.run()
""",
    ".gitignore": ignores,
    ".dockerignore": ignores,
    "app/templates/base.html":"""<!DOCTYPE html>
    <html lang="en">
    <head>
    {% block head %}
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- mobile metas -->
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="viewport" content="initial-scale=1, maximum-scale=1">
    <!-- site metas -->
    <meta name="keywords" content="">
    <meta name="description" content="">
    <meta name="author" content="">
    
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    
        <!-- style css -->
    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/style.css') }}">
    
    <link rel="icon" href="{{ url_for('static', filename='media/favicon.ico') }}" type="image/gif" />
    
    <title>{% block title %}{% endblock %} - App</title>
    {% endblock %}
    </head>

    <body>
        <!-- Navbar -->
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <div class="container-fluid">
                <a class="navbar-brand" href="#">My Flask App</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarNav">
                    <ul class="navbar-nav ms-auto">
                        <li class="nav-item">
                            <a class="nav-link" href="/">Home</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="/login">Login</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="/signup">Signup</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
        
        <!-- Main Content -->
    <div class="page-content" id="content">
        {% block content %}{% endblock %}
    </div>


    <!--footer section start -->
    <div class="footer_section layout_padding">
        <div class="container">
            <div class="row">
                <div class="col-lg-4 col-sm-6">
                <div class="footer_logo"><img src="#"></div>
                <p class="dolor_text"></p>
                </div>
                <div class="col-lg-4 col-sm-6">
                <h4 class="address_text">Legal</h4>
                <a href="#"><p class="dolor_text">Privacy Policy</p></a>
                <a href="#"><p class="dolor_text">Terms of service</p></a>
                
                </div>
                <div class="col-lg-4 col-sm-12">
                <h4 class="address_text">Contact</h4>
                <a href="mailto:#><p class="dolor_text">name@email.com</p></a>
                
                </div>
            </div>
        
        </div>
    </div>
    <!--footer section end -->
    <!-- copyright section start -->
    <div class="copyright_section">
        <div class="copyright_text">&copy; {{current_year}} CB App. All Rights Reserved.</div>
    </div>
    <!-- copyright section end -->

    <!-- Javascript files-->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
    <script src="{{ url_for('static', filename='js/index.min.js') }}"></script>

    </body>
    </html>
    """,
    ".env":"""SECRET_KEY=""
STRIPE_API_KEY=""
MAIL_SERVER=""
MAIL_PORT="465"
MAIL_USERNAME="x@x.com"
MAIL_PASSWORD=""
# MAIL_DEFAULT_SENDER=("Flask App", "x@x.com")
# """,
    "requirements.txt":"""Flask
    flask-blueprint
    Flask-Mail
    Flask-SQLAlchemy
    python-dotenv
    requests
    SQLAlchemy""",

    }

    # Create the folder structure
    def create_structure(base_path, structure):
        for name, content in structure.items():
            path = os.path.join(base_path, name)
            if isinstance(content, dict):
                # Create directories
                os.makedirs(path, exist_ok=True)
                create_structure(path, content)
            elif isinstance(content, list):
                # Create files in the list
                os.makedirs(path, exist_ok=True)
                for filename in content:
                    open(os.path.join(path, filename), 'w').close()
            else:
                # Create files
                open(path, 'w').close()

    # Write boilerplate content to specific files
    def write_boilerplate_content(base_path, boilerplate_files):
        for filepath, content in boilerplate_files.items():
            full_path = os.path.join(base_path, filepath)
            full_path = os.path.normpath(full_path)
            file_dir = os.path.dirname(full_path)
            # print(full_path)
            if not os.path.exists(file_dir):
                os.makedirs(file_dir, exist_ok=True)
            with open(full_path, 'w') as file:
                file.write(content)

    
    create_structure(base_path, structure)
    write_boilerplate_content(base_path, boilerplate_files)
    print(f"Flask project structure created successfully at {base_path}")
