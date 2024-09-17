
# Web Template to Flask Project Converter

This Python script automates the process of converting a static HTML web template into a Flask project structure. It handles copying CSS, JS, and image directories to the `static` folder, moves HTML files to the `templates` folder, and modifies references to scripts and stylesheets to match the Flask project's structure. This eliminates the need to manually adjust paths in HTML files and copy assets.

## Features
- **Automatic Folder Restructuring**: Copies `css`, `js`, `img`, `images`, and `plugins` directories (and their subdirectories) from the web template into the Flask project's `static` directory.
- **Template Management**: Moves all HTML files to the `templates` folder for Flask compatibility.
- **Path Modification**: Updates the relative paths in HTML files for CSS, JS, and image files to Flask’s structure (i.e., `{{ url_for('static', filename='...') }}`).
- **Recursive File Handling**: Copies all necessary subdirectories and files, ensuring the integrity of the project's assets and templates.

## Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/your-username/web-template-to-flask-converter.git
    cd web-template-to-flask-converter
    ```

2. **Install Python Dependencies**
    This script requires Python 3.x. Install any required dependencies by running:
    ```bash
    pip install -r requirements.txt
    ```
   _Note: No external packages are required unless you choose to add features that require specific libraries._

## Usage

1. **Prepare the Web Template**

    Place the web template's files in a directory structure similar to this:
    ```
    web_template/
    ├── css/
    ├── js/
    ├── img/
    ├── index.html
    └── ...
    ```

2. **Run the Script**

    Run the script with the path to your web template and the target Flask project directory:
    ```bash
    python convert_to_flask.py <template_directory> <flask_project_directory>
    ```
   - `<template_directory>`: Path to the root of your web template.
   - `<flask_project_directory>`: Path to the Flask project where files will be copied and converted.

   Example:
    ```bash
    python convert_to_flask.py ./web_template ./flask_app
    ```

3. **Resulting Flask Project Structure**

    After running the script, your Flask project will look like:
    ```
    flask_app/
    ├── static/
    │   ├── css/
    │   ├── js/
    │   ├── img/
    ├── templates/
    │   ├── index.html
    │   └── ...
    ├── app.py
    └── ...
    ```

    The script will modify the HTML files so that CSS, JS, and image references use Flask's `url_for` function:
    ```html
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
    <script src="{{ url_for('static', filename='js/script.js') }}"></script>
    ```

## Customization

If your template contains different folder names for assets (e.g., `assets`, `scripts`, etc.), you can modify the list of directories in the script to include those folder names.

```python
asset_folders = ['css', 'js', 'img', 'images', 'plugins']
```

You can also extend the script to handle any specific file types or folder structures unique to your template.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
