from textnode import *
from htmlnode import *

def main():
    new_node = text_node("This is some anchor text", text_type.link, "https://www.boot.dev")
    print(new_node)



main()
