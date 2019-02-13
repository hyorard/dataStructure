class Node:
    def __init__(self, key):
        self.key = key
        self.parent = self.left = self.right = None

    def __str__(self):
        return str(self.key)


class BST:  # BST 실습 내용을 그대로
    def __init__(self):
        self.root = None
        self.size = 0
    def __len__(self):
        return self.size

    def preorder(self, v):
        if v != None:
            print(v.key,end=' ')
            if v.left:
                print("<-",end=' ')
            self.preorder(v.left)
            if v.right:
                print("->",end=' ')
            self.preorder(v.right)

    def inorder(self, v):
        if v != None:
            print("<-",end=' ')
            if v.left:
                print("<-",end=' ')
            print(v.key,end=' ')
            if v.right:
                print("->",end=' ')
            self.inorder(v.right)

    def postorder(self, v):
        if v != None:
            print("<-",end=' ')
            if v.left:
                print("<-",end=' ')
            if v.right:
                print("->",end=' ')
            self.postorder(v.right)
            print(v.key, end=' ')

    def find_loc(self, key):
        if self.root == None:
            return None
        p = None
        v = self.root
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
        k = self.find_loc(key)
        if self.root == None:
            return None
        if k.key == key:
            return k
        else:
            return None

    def insert(self, key):
        k = self.find_loc(key)
        if self.root == None:
            self.root = Node(key)
            self.size += 1
            return self.root
        if k.key == key:
            return None
        else:
            v = Node(key)
            if k.key > key:
                k.left = v
            else:
                k.right = v
            v.parent = k
            self.size += 1
            return v


class SplayTree(BST):

    def rotateLeft(self, x):
        if x == None:
            return None
        y = x.right
        if y == None:
            return
        b = y.left
        if x.parent:
            if x.parent.right == x:
                x.parent.right = y
            else:
                x.parent.left = y
        y.parent = x.parent
        x.parent = y
        y.left = x
        if b:
            b.parent = x
        x.right = b
        if self.root == x:
            self.root = y

    def rotateRight(self, x):
        if x == None:
            return None
        y = x.left
        if y == None:
            return
        if x.parent:
            if x.parent.right == x:
                x.parent.right = y
            else:
                x.parent.left = y
        y.parent = x.parent
        b = y.right
        y.right = x
        x.parent = y
        if b:
            b.parent = x
        x.left = b
        if self.root == x:
            self.root = y

    def splay(self, x):
        if x== None:
            return
        while x.parent != None:
            p = x.parent
            if p:
                pp = p.parent
            if p == self.root:
                if p.left == x:
                    self.rotateRight(p)
                else:
                    self.rotateLeft(p)
            elif pp.left == p and p.left == x:
                self.rotateRight(p)
                self.rotateRight(pp)
            elif pp.right == p and p.right == x:
                self.rotateLeft(p)
                self.rotateLeft(pp)
            elif pp.left == p and p.right == x:
                self.rotateLeft(p)
                self.rotateRight(pp)
            elif pp.right == p and p.left == x:
                self.rotateRight(p)
                self.rotateRight(pp)
            self.preorder(T.root)
            print()
        return x



    def search(self, key):
        v = super(SplayTree, self).search(key)
        if v:
            self.root = self.splay(v)
        return v

    def insert(self, key):
        v = super(SplayTree, self).insert(key)
        return self.splay(v)


    def delete(self, x):
        self.splay(x)
        if x == None:
            return None
        L,R = x.left, x.right
        if L:
            m = L
            while m.right:
                m = m.right
            self.splay(m)
            m.right = None
            m.right = R
            if R:
                R.parent = m
            self.root = m
        elif R:
            R.parent = None
            self.root = R
        else:
            self.root = None



    def preorder(self, v):
        super(SplayTree, self).preorder(v)

    def postorder(self, v):
        super(SplayTree, self).postorder(v)

    def inorder(self, v):
        super(SplayTree, self).inorder(v)

T = SplayTree()

while True:
    cmd = input().split()
    if cmd[0] == 'in':
        v = T.insert(int(cmd[1]))
        print("+ {0} is inserted".format(v.key))
    elif cmd[0] == 'del':
        v = T.search(int(cmd[1]))
        T.delete(v)
        print("- {0} is deleted".format(int(cmd[1])))
    elif cmd[0] == 'find':
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
