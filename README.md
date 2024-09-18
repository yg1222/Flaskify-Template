# Theme to Flask Project Copier

## Overview

This script copies files from a theme directory into a Flask project directory, organizing them into the appropriate `static` and `templates` subdirectories. It also updates HTML files within the `templates` directory to use Flask's `url_for` function for referencing static files.

## Features

- Copies HTML, HTM, and other static files from a theme directory to a Flask project's `templates` and `static` directories.
- Updates HTML and script file references to use Flask's `url_for` for static file paths.

## Requirements

- Python 3.x
- `BeautifulSoup4` library (install via `pip install beautifulsoup4`)

## Usage

1. **Install dependencies:**
   ```bash
   pip install beautifulsoup4
   ```

2. **Run the script:**
   ```bash
   python script.py <theme_dir> <flask_project_dir>
   ```
   - `<theme_dir>`: The root directory of the theme or web template (absolute or relative).
   - `<flask_project_dir>`: The Flask project directory (absolute or relative).

## Example

```bash
python flaskify.py /path/to/theme /path/to/flask_project
