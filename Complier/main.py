import numpy as np


""" Node

Class defines a node in the tree
node has value which is the value of the node
left is the value of the node to it's left
right is the value of the node to it's right
"""
class node(object):
    def __init__(self, value = None):
        self.value = value
        self.right = None
        self.left = None

""" Tree

This is a bianary search tree
we can use this to parse the string
take the string and make the string
"""
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

""" main method """
def main():
    inp = input("Enter Kotlin file: ")
    out = input("Enter Swift file: ")

    kt_file = open(inp, 'r')
    #sw_file = open(out, 'w+')

    s = kt_file.read()
    b = parse(s)
    print(b)
    #sw_file.write(s)

    kt_file.close()
    #sw_file.close()

if __name__ == "__main__":
    main()

@staticmethod
def parse(str):
    arr = []
    for char in str:
        arr.append(str(char))
    return arr