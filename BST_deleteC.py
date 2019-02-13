def deleteByCopying(self,x):
    if x == None:
        return None
    a,b,pt = x.left, x.right, x.parent
    if a:
        m = a
        while m.right:
            m = m.right
        x.key = m.key
        if m.left:
            m.parent.right = m.left
            m.left.parent = m.parent
        elif m.parent.left == m:
            m.parent.left = None
        elif m.parent.right == m:
            m.parent.right = None
    elif a == None and b:
        m = b
        while m.left:
            m = m.left
        x.key = m.key
        if m.right:
            m.parent.left = m.right
            m.right.parent = m.parent
        elif m.parent.left == m:
            m.parent.left = None
        elif m.parent.right == m:
            m.parent.right == None
    else:
        if pt:
            if pt.right == x:
                pt.right = None
            elif pt.left == x:
                pt.left = None
        else:
            self.root = None
    self.size -= 1
