import numpy as np

class node(object):
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.right = None
        self.left = None

class tree(object):
    def __init__(self):
        self.root = None
    def insert(self, value):
        if self.root is None:
            self.root = node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left  is None:
                cur_node.left = node(value)
            else:
                self._insert(value, cur_node.left)
        elif value > cur_node.value:
            if cur_node.right is None:
                cur_node.right = node(value)
            else:
                self._insert(value, cur_node.right)
        else:
            print("value already in tree.")

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node is not None:
            self._print_tree(cur_node.left)
            print(cur_node.value)
            self._print_tree(cur_node.right)

# tree aproach

