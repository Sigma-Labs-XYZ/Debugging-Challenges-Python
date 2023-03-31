# https://www.codewars.com/kata/5f7c38eb54307c002a2b8cc8/python

""" Remove the parentheses
In this kata you are given a string for example:

"example(unwanted thing)example"
Your task is to remove everything inside the parentheses as well as the parentheses themselves.

The example above would return:

"exampleexample" """


def remove_parentheses(s):
    lvl, out = 0, []
    for c in s:
        lvl -= c == "("
        if not lvl:
            out.append(c)
        lvl += c == ")"
    return "".join(out)
