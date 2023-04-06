import re


class FileSystemNode:
    def __init__(self, name: str, is_directory: bool, children=None):
        self.name = name
        self.is_directory = is_directory
        self.children = children if children is not None else []

    def add_child(self, node):
        if not self.is_directory:
            raise NotADirectoryError(
                "Cannot add child to a node that is not a directory."
            )
        self.children.append(node)

    def remove_child(self, node):
        self.children.remove(node)

    def __repr__(self):
        if self.is_directory:
            return f"<Directory {self.name}>"
        else:
            return f"<File {self.name}>"


class FileSystemTree:
    def __init__(self, root: FileSystemNode):
        self.root = root

    def __repr__(self):
        return self._get_tree_string(self.root)

    def _get_tree_string(self, node: FileSystemNode, prefix="", is_last=True):
        tree_str = prefix + ("└── " if is_last else "├── ") + str(node) + "\n"
        prefix += "    " if is_last else "│   "
        child_count = len(node.children)
        for i, child in enumerate(node.children):
            is_last = i == child_count - 1
            tree_str += self._get_tree_string(child, prefix, is_last)
        return tree_str

    def get_node(self, path):
        # Given a path string, return the node corresponding to that path in the tree
        # Example path: "/home/user/file.txt"
        parts = path.split("/")
        current_node = self.root
        for part in parts:
            if part == "":
                continue
            child_node = None
            for child in current_node.children:
                if child.name == part:
                    child_node = child
                    break
            if child_node is None:
                return None
            current_node = child_node
        return current_node


def _rename_node(node, rename_func, rename_directories=True):
    if not node.is_directory:
        node.name = rename_func(node.name)
    elif rename_directories:
        node.name = rename_func(node.name)
    for child in node.children:
        _rename_node(child, rename_func, rename_directories)


def add_prefix(tree, prefix, rename_directories=True):
    def add_prefix_to_name(name):
        return prefix + name

    _rename_node(tree.root, add_prefix_to_name, rename_directories)


def add_suffix(tree, suffix, rename_directories=True):
    def add_suffix_to_name(name):
        return name + suffix

    _rename_node(tree.root, add_suffix_to_name, rename_directories)


def replace(tree, regex, new_text, rename_directories=True):
    compiled_regex = re.compile(regex)

    def replace_regex_in_name(name):
        return compiled_regex.sub(new_text, name)

    _rename_node(tree.root, replace_regex_in_name, rename_directories)
