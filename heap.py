class Heap:
	def __init__(self, L=[]):
		self.A = L
		self.make_heap()
	def __str__(self):
		return str(self.A)
	def __len__(self):
		return len(self.A)
	def heapify_down(self, k, n=None): # heapify heap[k]
		while 2*k+1 < n:
			L , R = 2*k+1, 2*k+2
			if L < n and self.A[L] > self.A[k]:
				m = L
			else:
				m = k
			if R < n and self.A[R] > self.A[m]:
				m = R
			if m != k:
				self.A[k] , self.A[m] = self.A[m] , self.A[k]
				k = m
			else:
				break

	def make_heap(self):
		n = len(self.A)
		for k in range(n//2,-1,-1):
			self.heapify_down(k,n)

	def heap_sort(self):
		n = len(self.A)
		for k in range(len(self.A)-1,-1,-1):
			self.A[k], self.A[0] = self.A[0], self.A[k]
			n -= 1
			self.heapify_down(0,n)

	def heapify_up(self, k):
		while k > 0 and self.A[(k-1)//2] < self.A[k]:
			self.A[(k-1)//2], self.A[k] = self.A[k], self.A[(k-1)//2]
			k = (k-1) // 2

	def insert(self, key):
		self.A.append(key)
		self.heapify_up(len(self.A)-1)

	def delete_max(self):
		if len(self.A) == 0:
			return None
		else:
			key = self.A[0]
			self.A[0], self.A[len(self.A)-1] = self.A[len(self.A)-1], self.A[0]
			self.A.pop()
			self.heapify_down(0,len(self.A))
			return key

	def find_max(self):
		return self.A[0]

# 아래 코드는 변경하지 말것!
H = Heap()
while True:
	cmd = input().split()
	if cmd[0] == 'insert':
		key = int(cmd[1])
		H.insert(key)
		print("+", key, "is inserted into H.")
	elif cmd[0] == 'd_max':
		key = H.delete_max()
		if key == None:
			print("* heap is empty.")
		else:
			print("-", key, "is the maximum and deleted.")
	elif cmd[0] == 'f_max':
		key = H.find_max()
		if key == None:
			print("* heap is empty.")
		else:
			print("*", key, "is the maximum.")
	elif cmd[0] == 'sort':
		H.heap_sort()
		print("sorted heap:", H)
		H.make_heap()
	elif cmd[0] == 'print':
		print(H)
	elif cmd[0] == 'exit':
		break
	else:
		print("not allowed operation.")
print("It's over now!")
