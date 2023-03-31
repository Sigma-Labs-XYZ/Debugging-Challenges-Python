def remove_parentheses(s):
    lvl, out = 0, []
    for c in s:
        lvl += c == "("
        if not lvl:
            out.append(c)
        lvl -= c == ")"
    return "".join(out)
