import os
import shutil
import sys
from copystatic import copy_dir
from generating_html import *

dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"
def_base_path = "/"

def main():
    base_path = def_base_path
    if len(sys.argv) > 1:
        base_path = sys.argv[1]


    print(f"dir_path_content : {dir_path_content}")
    print("Deleting public directory...")
    print("Copying static files to public directory...")
    copy_dir(dir_path_static, dir_path_public)
    
    print("Generating page...")
    generate_pages_recursive(
        dir_path_content,
        template_path,
        dir_path_public, 
        base_path
    )


main()
