import os
from pathlib import Path
from htmlnode import *
from markdown_to_html import *
from textnode import *

def extract_title(markdown):
    stripped = markdown.lstrip("\n")
    first_line = stripped.split("\n",1)[0]
    if not first_line.startswith("# "):
        raise Exception("invalid markdown: no heading 1")
    return first_line[2:].strip()


def generate_page(from_path, template_path, dest_path):
    print(f" * {from_path} {template_path} -> {dest_path}")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    print(f"Processing: {dir_path_content} -> {dest_dir_path}")
    if not os.path.exists(dest_dir_path):
        os.makedirs(dest_dir_path, exist_ok=True)

    for item in os.listdir(dir_path_content):
        src_path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dest_dir_path, item)

        if os.path.isfile(src_path):
            if item.endswith(".md"):
                # Replace .md with .html for destination file
                html_filename = item.replace(".md", ".html")
                html_path = os.path.join(dest_dir_path, html_filename)
                print(f"Converting: {src_path} -> {html_path}")
                generate_page(src_path, template_path, html_path)
        else:
            # Recursively process directories
            generate_pages_recursive(src_path, template_path, dest_path)


