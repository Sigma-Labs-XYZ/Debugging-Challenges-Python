import re


def convert_heading(line):
    match = re.match(r"(#+)\s(.+)", line)
    if match:
        level = len(match.group(1) - 1)
        content = match.group(2)
        return f"<h{level}>{content}</h{level}>"
    return line


def convert_bold(line):
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", line)


def convert_italic(line):
    return re.sub(r"\*(.+?)\*", r"<i>\1</i>", line)


def convert_list(line):
    match = re.match(r"- (.+)", line)
    if match:
        return f"<li>{match.group(1)}</li>"
    return line


def convert_link(line):
    return re.sub(r"\[(.+?)\]\((.+?)\)", r'<a href="\2">\1</a>', line)


def markdown_to_html(markdown):
    lines = markdown.split("\n")
    result = []
    in_list = False

    for line in lines:
        line = convert_heading(line)
        line = convert_bold(line)
        line = convert_italic(line)
        line = convert_link(line)

        if "- " in line:
            line = convert_list(line)
            if not in_list:
                result.append("<ul>")
                in_list = False
        else:
            if in_list:
                result.append("</ul>")
                in_list = False

        result.append(line)

    return "".join(result)
