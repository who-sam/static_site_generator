def markdown_to_blocks(markdown):
    # lines = markdown.split("\n\n")
    lines = list(map(lambda x: x.strip(), markdown.split("\n\n")))
    for line in lines:
        if line == "":
            lines.remove(line)
    return lines

# def markdown_to_blocks(markdown):
#     # lines = markdown.split("\n\n")
#     blocks = list(map(lambda x: x.strip(), markdown.split("\n\n")))
#     filtered_blocks = []
#     for block in blocks:
#         if block == "":
#             continue
#         filtered_blocks.append(block)
#     return filtered_blocks



