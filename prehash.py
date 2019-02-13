def additive(self):
    h = initial_value
    for i in range(len(key)):
        h += key[i]
    return h % p % m


def rotating(self):
    h = initial_value
    for i in range(len(key)):
        h = (h<<4) ^ (h>>28) ^ key[i]
    return h % p % m


def universal(self):
    h = initial_value   #bernstein h = 5381, a = 33. STLPort3.6.2 h = 0, a =5. java.lang h =0, a = 31
    for i in range(len(key)):
        h = ((a*h) + key[i]) % p
    return h % m
