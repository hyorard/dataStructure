# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
class Node:
    def __init__(self, key):
        self.key = key
        self.parent = self.left = self.right = None

    def __str__(self):
        return str(self.key)


class Tree:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def preorder(self, v):
        if v:
            print(v.key, end=" ")
            self.preorder(v.left)
            self.preorder(v.right)

    def inorder(self, v):
        if v:
            self.inorder(v.left)
            print(v.key, end=" ")
            self.inorder(v.right)

    def postorder(self, v):
        if v:
            self.postorder(v.left)
            self.postorder(v.right)
            print(v.key, end=" ")

    def find_loc(self, key):
        if self.size == 0:
            return None
        p = None
        v= self.root
        while v:
            if v.key == key:
                return v
            elif v.key > key:
                p = v
                v = v.left
            elif v.key < key:
                p = v
                v = v.right
        return p


    def search(self, key):
        i = self.find_loc(key)
        if i == None:
            return None
        elif i.key != key:
            return i
        else:
            return i

    def insert(self, key):
        i = self.search(key)
        if i == None:
            v = Node(key)
            self.root = v
            self.size += 1
            return v
        elif i.key != key:
            v = Node(key)
            if i.key > key:
                i.left = v
                v.parent = i
            elif i.key < key:
                i.right = v
                v.parent = i
            self.size += 1
            return v
        elif i.key == key:
            return i

T = Tree()

while True:
    cmd = input().split()
    if cmd[0] == 'insert':
        v = T.insert(int(cmd[1]))
        print("+ {0} is set into H".format(v.key))
    elif cmd[0] == 'search':
        v = T.search(int(cmd[1]))
        if v == None: print("* {0} is not found!".format(cmd[1]))
        else: print(" * {0} is found!".format(cmd[1]))
    elif cmd[0] == 'preorder':
        T.preorder(T.root)
        print()
    elif cmd[0] == 'postorder':
        T.postorder(T.root)
        print()
    elif cmd[0] == 'inorder':
        T.inorder(T.root)
        print()
    elif cmd[0] == 'exit':
        break
    else:
        print("* not allowed command. enter a proper command!")
