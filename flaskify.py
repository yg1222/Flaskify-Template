import os
import shutil
from bs4 import BeautifulSoup

def modify_srcs(flask_project_dir):
    templates_dir = os.path.join(flask_project_dir, 'templates')
    for root, _, files in os.walk(templates_dir):
        print(files)
        for file in files:
            if file.endswith(('.html', '.htm')):
                html_file_path = os.path.join(root, file)

                with open(html_file_path, 'r', encoding='utf-8') as f:
                    soup = BeautifulSoup(f, 'html.parser')

                for link in soup.find_all('link', href=True):
                    if not link['href'].startswith('http'):
                        file_name = os.path.basename(link['href'])
                        folder_name = link['href'].split('/')[0]
                        link['href'] = f"{{{{ url_for('static', filename='{folder_name}/{file_name}') }}}}"

                for script in soup.find_all('script', src=True):
                    if not script['src'].startswith('http'):
                        file_name = os.path.basename(script['src'])
                        folder_name = script['src'].split('/')[0]
                        script['src'] = f"{{{{ url_for('static', filename='{folder_name}/{file_name}') }}}}"

                with open(html_file_path, 'w', encoding='utf-8') as f:
                    f.write(str(soup))

def copy_files(theme_dir, flask_project_dir):
    # directories for Flask
    static_dir = os.path.join(flask_project_dir, 'static')
    templates_dir = os.path.join(flask_project_dir, 'templates')
    print(theme_dir)
    print(os.path.isabs(theme_dir))
    os.makedirs(templates_dir, exist_ok=True)
    print(f'templates_dir: {templates_dir}')
    
    for cursor_root, cursor_root_dirs, cursor_root_files in os.walk(theme_dir):
        cursor_root_dirs[:] = [d for d in cursor_root_dirs if d != flask_project_dir]
        print(f'\ncursor_root: {cursor_root}')
        if len(cursor_root_dirs) > 0:
            print(f'cursor_root_dirs: {cursor_root_dirs}')
        
        # if './plugins' in cursor_root:
        #     print(f'files: {cursor_root_files}')

        # processes the root-level directories
        for subfolder in cursor_root_dirs:
            if not os.path.isabs(cursor_root):
                src_subfolder_path = os.path.join(cursor_root, subfolder)
                dest_subfolder_path = os.path.join(static_dir, os.path.relpath(src_subfolder_path))            
                os.makedirs(dest_subfolder_path, exist_ok=True)

                print(f"\nstatic_dir: {static_dir}\nsrc_subfolder_path: {src_subfolder_path}\ndest_subfolder_path: {dest_subfolder_path}")
            else:
                src_subfolder_path = os.path.join(cursor_root, subfolder)
                dest_subfolder_path = os.path.join(static_dir, os.path.relpath(src_subfolder_path))            
                os.makedirs(dest_subfolder_path, exist_ok=True)
                print(f"\nstatic_dir: {static_dir}\nsrc_subfolder_path: {src_subfolder_path}\ndest_subfolder_path: {dest_subfolder_path}")
            

            
        # processes the files
        for file in cursor_root_files:
            src_file_path = os.path.join(cursor_root, file)
            if file.endswith(('.html', '.htm')):
                dest_file_path = os.path.join(templates_dir, cursor_root, file)
                print(f"\n{src_file_path} ===>  {dest_file_path}\n")
                if os.path.isfile(src_file_path):
                    if not os.path.exists(dest_file_path) or not os.path.samefile(src_file_path, dest_file_path):
                        shutil.copy(src_file_path, dest_file_path)
            else:
                # dest_file_path = os.path.join(static_dir, os.path.relpath(cursor_root), file)
                # print(f"static_dir: {static_dir}")
                dest_file_path = os.path.join(static_dir, cursor_root, file)
                # print(f"\n{src_file_path} ===>  {dest_file_path}\n")
                if os.path.isfile(src_file_path):
                    if not os.path.exists(dest_file_path) or not os.path.samefile(src_file_path, dest_file_path):
                        shutil.copy(src_file_path, dest_file_path)
                 

# usage
# theme_dir = os.path.normpath(input("Enter the theme path (relative or absolute path): "))
# flask_project_dir = os.path.normpath(input("Enter you destination flask app path: "))

# test
theme_dir = os.path.normpath('/home/dnoops/Documents/Projects/logistico-tester/')
flask_project_dir = os.path.normpath('/home/dnoops/Documents/Scripts/new_flask_app')

# theme_dir = os.path.normpath('./')
# flask_project_dir = os.path.normpath('flask_app/')

# display_file_copy(theme_dir, flask_project_dir)
copy_files(theme_dir, flask_project_dir)
modify_srcs(flask_project_dir)