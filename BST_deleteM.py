def deleteByMerging(self,x):
    if x == None:
        return None
    a,b,pt = x.left, x.right, x.parent
    if a == None:
        c = b
    else:
        c = a
        m = a
        while m.right:
            m = m.right
        m.right = b
        if b:
            b.parent = m
    if self.root == x:
        self.root = c
        if c:
            c.parent = None
    else:
        if pt.left == x:
            pt.left = c
            if c:
                c.parent = pt
        else:
            pt.right = c
            if c:
                c.parent = pt
