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
        if v != None:
            print(v.key, end=' ')
            self.preorder(v.left)
            self.preorder(v.right)

    def inorder(self, v):
        if v != None:
            self.inorder(v.left)
            print(v.key, end=' ')
            self.inorder(v.right)

    def postorder(self, v):
        if v != None:
            self.postorder(v.left)
            self.postorder(v.right)
            print(v.key,end=' ')

    def find_loc(self, key):
        if self.root == None:
            return None
        p = None
        v = self.root
        while v:
            if key == v.key:
                return v
            elif key < v.key:
                p = v
                v = v.left
            elif key > v.key:
                p = v
                v = v.right
        return p

    def search(self, key):
        v = self.find_loc(key)
        if v and v.key == key:
            return v
        else:
            return None

    def insert(self, key):
        p = self.find_loc(key)
        if p == None or p.key != key:
            v = Node(key)
            if p == None:
                self.root = v
            else:
                v.parent = p
                if v.key > p.key:
                    p.right = v
                else:
                    p.left = v
            self.size += 1
            return v
        else:
            return p

    def deleteByMerging(self, x):
        if x == None:
            return None
        a,b,pt = x.left,x.right,x.parent
        if a == None:
            c = b
        else:
            c = a
            m = c
            while m.right:
                m = m.right
            m.right = b
            if b:
                b.parent = m
        if self.root == x:
            if c:
                c.parent = None
            self.root = c
        else:
            if c:
                c.parent = pt
            if pt.right == x:
                pt.right = c
            elif pt.left == x:
                pt.left = c
        self.size -= 1


    def deleteByCopying(self, x):
        if x == None:
            return None
        a,b,pt = x.left,x.right,x.parent
        if a:
            m = a
            while m.right:
                m = m.right
            x.key = m.key
            if m.left:
                c = m.left
                m.parent.left = c
                c.parent = m.parent
            elif m.parent.right == m:   #왼쪽에서 제일 큰 자손 노드가 왼쪽 자식이 없을 때
                m.parent.right = None
            elif m.parent.left == m:    #왼쪽 자식 노드가 하나일때
                m.parent.left = None

        elif a == None and b:
            m = b
            while m.left:
                m = m.left
            x.key = m.key
            if m.right:
                c = m.right
                m.parent.right = c
                c.parent = m.parent
            elif m.parent.left == m:    #오른쪽에서 제일 작은 자손노드가 자식이 없을 때
                m.parent.left = None
            elif m.parent.right == m:   #오른쪽 자식 노드가 하나일 때
                m.parent.right = None
        else:
            if pt:
                if pt.right == x:
                    pt.right = None
                elif pt.left == x:
                    pt.left = None
            else:
                self.root = None
        self.size -= 1




T = Tree()

while True:
    cmd = input().split()
    if cmd[0] == 'insert':
        v = T.insert(int(cmd[1]))
        print("+ {0} is inserted".format(v.key))
    elif cmd[0] == 'deleteC':
        v = T.search(int(cmd[1]))
        T.deleteByCopying(v)
        print("- {0} is deleted by copying".format(int(cmd[1])))
    elif cmd[0] == 'deleteM':
        v = T.search(int(cmd[1]))
        T.deleteByMerging(v)
        print("- {0} is deleted by merging".format(int(cmd[1])))
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
