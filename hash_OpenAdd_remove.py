def remove(sefl,key):
    i = self.find_slot(key)
    if i == FULL:
        print("잘못된 key 값 입력")
        return None
    elif H[i] != None:
        print("잘못된 key 값 입력")
        return None
    initial_i = i
    j = i
    while True:
        H[i] = None
        while True:
            j = (j+1) % m
            if H[j] == None:
                return H[initial_i].key
            k = hash_function(H[j].key)
            if not ((i<j) and (j<=k)) or ((k<i) and (i<j)) or ((j<=k) and (k<i)):
                break
        H[i] = H[j]
        i = j


def find_slot(self,key):
    h = hash_function(key)
    start = h
    j = h
    while j != None and j.value != h.value:
        if j == start:
            return FULL
        j = (j+1) % m
    return j


def remove(self,key):
    i = self.find_slot(key)
    if H[i] == None:
        print("key not exist")
    j = i
    while True:
        H[i] = None
        while True:
            j = (j+1) % m
            if H[j] == None:
                return H[key].key
            k = hash_function(H[j].key)
            if not i<k<=j and j<i<k and k<=j<i:
                break
        H[i] = H[j]
        i = j
