import os
import argparse
import shutil
from bs4 import BeautifulSoup
from boilerplate import generate_structure_and_boilerplate

def main():

    parser = argparse.ArgumentParser(description='Copy files from a theme directory into a flask app directory in a flask-specific structure.')

    parser.add_argument('theme_dir', help='The root directory of the theme or web template (absolute or relative).')
    parser.add_argument('flask_project_dir', help='The flask project directory (absolute or relative).')

    args = parser.parse_args()

    theme_dir = os.path.normpath(args.theme_dir)
    flask_project_dir = os.path.normpath(args.flask_project_dir)

    

    def copy_files(theme_dir, flask_project_dir):
        # directories for Flask
        static_dir = os.path.join(flask_project_dir, 'app', 'static')
        templates_dir = os.path.join(flask_project_dir, 'app', 'templates')
        os.makedirs(templates_dir, exist_ok=True)
        
        for cursor_root, cursor_root_dirs, cursor_root_files in os.walk(theme_dir):
            cursor_root_dirs[:] = [d for d in cursor_root_dirs if d != flask_project_dir]
                
            # processes the files
            for file in cursor_root_files:
                src_file_path = os.path.join(cursor_root, file)
                if file.endswith(('.html', '.htm')):
                    dest_file_path = os.path.join(templates_dir, cursor_root, file)
                    os.makedirs(os.path.dirname(dest_file_path), exist_ok=True)
                    if os.path.isfile(src_file_path):
                        if not os.path.exists(dest_file_path) or not os.path.samefile(src_file_path, dest_file_path):
                            shutil.copy(src_file_path, dest_file_path)
                else:
                    dest_file_path = os.path.join(static_dir, cursor_root, file)
                    os.makedirs(os.path.dirname(dest_file_path), exist_ok=True)
                    if os.path.isfile(src_file_path):
                        if not os.path.exists(dest_file_path) or not os.path.samefile(src_file_path, dest_file_path):
                            shutil.copy(src_file_path, dest_file_path)
                    
    def modify_srcs(flask_project_dir):
        templates_dir = os.path.join(flask_project_dir, 'app', 'templates')
        for root, _, files in os.walk(templates_dir):
            for file in files:
                if file.endswith(('.html', '.htm')):
                    html_file_path = os.path.join(root, file)

                    with open(html_file_path, 'r', encoding='utf-8') as f:
                        soup = BeautifulSoup(f, 'html.parser')
                        
                    for tag in soup.find_all(['link', 'img', 'script'], src=True) + soup.find_all('link', href=True) + soup.find_all('a', href=True):
                        if tag.has_attr('href'):
                            if not tag['href'].startswith(('http', 'mailto', 'tel', 'ftp', 'data')):
                                file_name = os.path.basename(tag['href'])
                                folder_name = tag['href'].split('/')[0]
                                if tag.name == 'link':
                                    tag['href'] = f"{{{{ url_for('static', filename='{folder_name}/{file_name}') }}}}"
                                elif tag.name == 'a':
                                    file_name = os.path.splitext(file_name)[0]  # Strip extension
                                    tag['href'] = f"/{file_name}"
                        elif tag.has_attr('src'):
                            if not tag['src'].startswith('http'):
                                file_name = os.path.basename(tag['src'])
                                folder_name = tag['src'].split('/')[0]
                                tag['src'] = f"{{{{ url_for('static', filename='{folder_name}/{file_name}') }}}}"

                    with open(html_file_path, 'w', encoding='utf-8') as f:
                        f.write(str(soup))


    # theme_dir = os.path.normpath(input("Enter the theme path (relative or absolute path): "))
    # flask_project_dir = os.path.normpath(input("Enter you destination flask app path: "))

    if os.path.isabs(theme_dir):
        os.chdir(theme_dir)
        theme_dir = os.path.relpath(os.getcwd(), theme_dir)

    generate_structure_and_boilerplate(flask_project_dir)
    copy_files(theme_dir, flask_project_dir)
    modify_srcs(flask_project_dir)


if __name__ == "__main__":
    main()