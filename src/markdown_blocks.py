from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"


def markdown_to_blocks(markdown):
    # lines = markdown.split("\n\n")
    lines = list(map(lambda x: x.strip(), markdown.split("\n\n")))
    for line in lines:
        if line == "":
            lines.remove(line)
    return lines

def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")) :
        return BlockType.HEADING
    if len(lines) >= 3 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        return BlockType.QUOTE if all(line.startswith(">") for line in lines) else BlockType.PARAGRAPH
    if block.startswith("- "):
        return BlockType.ULIST if all(line.startswith("- ") for line in lines) else BlockType.PARAGRAPH
    if block.startswith("1. "):
        for i in range(0,len(lines)):
            if not lines[i].startswith(f"{i+1}. "):
                return BlockType.PARAGRAPH
            return BlockType.OLIST
    return BlockType.PARAGRAPH





