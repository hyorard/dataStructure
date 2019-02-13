class Node:
    def __init__(self, key=None):
        self.key = key
        self.next = self
        self.prev = self

    def __str__(self):
        return str(self.key)

class DoublyLinkedList:
    def __init__(self):
        self.head = Node()


    def __iter__(self):
        v = self.head.next
        while v != self.head:
            yield v
            v = v.next
    def __str__(self):
        return " -> ".join(str(v.key) for v in self)

    def splice(self, a, b, x): # cut [a..b] after x
        # assert a <= b, x and head are not in [a..b]
        if a == None or b == None or x == None:
            return None
        else:
            ap = a.prev
            bn = b.next
            ap.next = bn
            bn.prev = ap
            xn = x.next
            x.next = a
            xn.prev = b
            a.prev = x
            b.next = xn

    def moveAfter(self, a, x): # move a after x
        self.splice(a,a,x)
    def insertAfter(self, x, key): # insert node of key after x
        self.moveAfter(Node(key),x)
    def pushFront(self, key, value):
        self.insertAfter(self.head,key)
    def remove(self, x): # remove x
        xp = x.prev
        xn = x.next
        xp.next = xn
        xn.prev = xp
        x_key = x.key
        del x
        return x_key
    def search(self, key):
        v = self.head.next
        found = False
        while v != self.head:
          if v.key == key:
              found = True
              break
          v = v.next
        if found == False:
            return None
        else:
            return v

class HashChaining:
    def __init__(self, size=10):
        self.size = size
        self.H = [DoublyLinkedList() for x in range(self.size)]
    def __str__(self):
        s = ""
        i = 0
        for k in self:
            s += "|{0:-3d}| ".format(i) + str(k) + "\n"
            i += 1
        return s
    def __iter__(self):
        for i in range(self.size):
            yield self.H[i]
    def hash_function(self, key):
        return key % self.size

    #def find_slot(self, key):
    def set(self, key, value=None):
        index = key % self.size
        result = self.H[index].search(key)
        if result == None:
          self.H[index].pushFront(key,value)
        else:
          result.value = value
    def remove(self, key):
        index = key % self.size
        result = self.search(key)
        if result == None:
          return None
        else:
          return self.H[index].remove(result)
    def search(self, key):
        index = key % self.size
        result = self.H[index].search(key)
        if result == None:
          return None
        else:
          return result

H = HashChaining(10)
while True:
    cmd = input().split()
    if cmd[0] == 'set':
        key = H.set(int(cmd[1]))
        print("+ {0} is set into H".format(cmd[1]))
    elif cmd[0] == 'search':
        key = H.search(int(cmd[1]))
        if key == None: print("* {0} is not found!".format(cmd[1]))
        else: print(" * {0} is found!".format(cmd[1]))
    elif cmd[0] == 'remove':
        key = H.remove(int(cmd[1]))
        if key == None:
            print("- {0} is not found, so nothing happens".format(cmd[1]))
        else:
            print("- {0} is removed".format(cmd[1]))
    elif cmd[0] == 'print':
        print(H)
    elif cmd[0] == 'exit':
        break
    else:
        print("* not allowed command. enter a proper command!")
