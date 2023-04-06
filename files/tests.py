import unittest
from files import (
    FileSystemNode,
    add_prefix,
    add_suffix,
    FileSystemTree,
    replace,
)


def compare_trees(tree1, tree2):
    """
    Compare two FileSystemTree objects for equality.

    Returns True if the trees have the same structure, metadata, and node names,
    False otherwise.
    """
    # Check if the roots have the same name and type
    if (
        tree1.root.name != tree2.root.name
        or tree1.root.is_directory != tree2.root.is_directory
    ):
        return False

    # Check if the roots have the same number of children
    if len(tree1.root.children) != len(tree2.root.children):
        return False

    # Check if the children have the same names and types
    for child1, child2 in zip(tree1.root.children, tree2.root.children):
        if (
            child1.name != child2.name
            or child1.is_directory != child2.is_directory
        ):
            return False

        # If the child is a directory, recursively compare its children
        if child1.is_directory:
            if not compare_trees(
                FileSystemTree(child1), FileSystemTree(child2)
            ):
                return False

    # If we've made it this far, the trees are equal
    return True


class TestFileSystemTree(unittest.TestCase):
    def setUp(self):
        # Create a test FileSystemTree object
        self.root_node = FileSystemNode("root", True)
        self.dir1_node = FileSystemNode("dir1", True)
        self.dir2_node = FileSystemNode("dir2", True)
        self.file1_node = FileSystemNode("file1.txt", False)
        self.file2_node = FileSystemNode("file2.txt", False)
        self.root_node.add_child(self.dir1_node)
        self.root_node.add_child(self.dir2_node)
        self.dir1_node.add_child(self.file1_node)
        self.dir2_node.add_child(self.file2_node)
        self.tree = FileSystemTree(self.root_node)

    def test_replace(self):
        replace(self.tree, "file", "new")
        expected_root_node = FileSystemNode(
            "root",
            True,
            [
                FileSystemNode(
                    "dir1",
                    True,
                    [
                        FileSystemNode("new1.txt", False),
                    ],
                ),
                FileSystemNode(
                    "dir2",
                    True,
                    [
                        FileSystemNode("new2.txt", False),
                    ],
                ),
            ],
        )
        expected_tree = FileSystemTree(expected_root_node)
        self.assertTrue(compare_trees(self.tree, expected_tree))

    def test_add_prefix(self):
        add_prefix(self.tree, "prefix_")
        expected_root_node = FileSystemNode(
            "prefix_root",
            True,
            [
                FileSystemNode(
                    "prefix_dir1",
                    True,
                    [
                        FileSystemNode("prefix_file1.txt", False),
                    ],
                ),
                FileSystemNode(
                    "prefix_dir2",
                    True,
                    [
                        FileSystemNode("prefix_file2.txt", False),
                    ],
                ),
            ],
        )
        expected_tree = FileSystemTree(expected_root_node)
        self.assertTrue(compare_trees(self.tree, expected_tree))

    def test_add_suffix(self):
        add_suffix(self.tree, ".suffix")
        expected_root_node = FileSystemNode(
            "root.suffix",
            True,
            [
                FileSystemNode(
                    "dir1.suffix",
                    True,
                    [
                        FileSystemNode("file1.txt.suffix", False),
                    ],
                ),
                FileSystemNode(
                    "dir2.suffix",
                    True,
                    [
                        FileSystemNode("file2.txt.suffix", False),
                    ],
                ),
            ],
        )
        expected_tree = FileSystemTree(expected_root_node)
        self.assertTrue(compare_trees(self.tree, expected_tree))

    def test_replace_no_rename_directories(self):
        replace(self.tree, "file", "new", rename_directories=False)
        expected_root_node = FileSystemNode(
            "root",
            True,
            [
                FileSystemNode(
                    "dir1",
                    True,
                    [
                        FileSystemNode("new1.txt", False),
                    ],
                ),
                FileSystemNode(
                    "dir2",
                    True,
                    [
                        FileSystemNode("new2.txt", False),
                    ],
                ),
            ],
        )
        expected_tree = FileSystemTree(expected_root_node)
        self.assertTrue(compare_trees(self.tree, expected_tree))

    def test_add_prefix_no_rename_directories(self):
        add_prefix(self.tree, "prefix_", rename_directories=False)
        expected_root_node = FileSystemNode(
            "root",
            True,
            [
                FileSystemNode(
                    "dir1",
                    True,
                    [
                        FileSystemNode("prefix_file1.txt", False),
                    ],
                ),
                FileSystemNode(
                    "dir2",
                    True,
                    [
                        FileSystemNode("prefix_file2.txt", False),
                    ],
                ),
            ],
        )
        expected_tree = FileSystemTree(expected_root_node)
        self.assertTrue(compare_trees(self.tree, expected_tree))

    def test_add_suffix_no_rename_directories(self):
        add_suffix(self.tree, ".suffix", rename_directories=False)
        expected_root_node = FileSystemNode(
            "root",
            True,
            [
                FileSystemNode(
                    "dir1",
                    True,
                    [
                        FileSystemNode("file1.txt.suffix", False),
                    ],
                ),
                FileSystemNode(
                    "dir2",
                    True,
                    [
                        FileSystemNode("file2.txt.suffix", False),
                    ],
                ),
            ],
        )
        expected_tree = FileSystemTree(expected_root_node)
        self.assertTrue(compare_trees(self.tree, expected_tree))


if __name__ == "__main__":
    unittest.main()
