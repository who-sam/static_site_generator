#!/bin/bash

# Directory containing the files
TARGET_DIR="./srC"

# Loop through all regular files in the directory
for file in "$TARGET_DIR"/*; do
  if [ -f "$file" ]; then
    nvim --headless "$file" +'%s/normal/TEXT/g' +wq
    nvim --headless "$file" +'%s/bold/BOLD/g' +wq
    nvim --headless "$file" +'%s/italic/ITALIC/g' +wq
    nvim --headless "$file" +'%s/code/CODE/g' +wq
    nvim --headless "$file" +'%s/link/LINK/g' +wq
    nvim --headless "$file" +'%s/image/IMAGE/g' +wq
    nvim --headless "$file" +'%s/text_type/TextType/g' +wq
    nvim --headless "$file" +'%s/text_node/TextNode/g' +wq
    nvim --headless "$file" +'%s/html_node/HTMLNode/g' +wq
    nvim --headless "$file" +'%s/leaf_node/LeafNode/g' +wq
    nvim --headless "$file" +'%s/parent_node/ParentNode/g' +wq
    echo "Processed: $file"
  fi
done
