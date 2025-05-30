from textnode import *
from htmlnode import *

def main():
    new_node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(new_node)



main()
