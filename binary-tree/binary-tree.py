from turtle import left


class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
   
    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value

    def size(self):
        return len(self.items)

    def __len__(self):
        return self.size()

    def __str__(self):
        return str(self.items)

class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)

class Node():
	def __init__(self, value): 
		self.value = value
		self.left = None
		self.right = None


# MAIN
class BinaryTree(): 
	def __init__(self, root):
		self.root = Node(root)

	# pre-order
	def preorder_print(self, start, traversal):
		if start:
			traversal += (str(start.value) + ' ')
			traversal = self.preorder_print(start.left, traversal)
			traversal = self.preorder_print(start.right, traversal)
		return traversal


	# in-order
	def inorder_print(self, start, traversal):
		if start:
			traversal = self.inorder_print(start.left, traversal)
			traversal += (str(start.value) + ' ')
			traversal = self.inorder_print(start.right, traversal)
		return traversal

	
	# post-order
	def postorder_print(self, start, traversal):
		if start:
			traversal = self.postorder_print(start.left, traversal)
			traversal = self.postorder_print(start.right, traversal)
			traversal += (str(start.value) + ' ')
		return traversal

	
	# level-order
	def levelorder_print(self, start):  

		if start is None:
			return 
		queue = Queue()
		queue.enqueue(start)

		traversal = ""
		while len(queue) > 0:
			traversal += str(queue.peek()) + " "
			node = queue.dequeue()
			
			if node.left:
				queue.enqueue(node.left)
			if node.right:
				queue.enqueue(node.right)
				
			
		return traversal


	# reverse_levelorder-order
	def reverse_levelorder_print(self, start):  
		if start is None:
			return 

		queue = Queue()
		stack = Stack()
		stack2 = Stack()
		queue.enqueue(start)

		traversal = ""
		while len(queue) > 0:
			node = queue.dequeue()
			stack.push(node)
			stack2.push(node.value)

			if node.right:
				queue.enqueue(node.right)
			if node.left:
				queue.enqueue(node.left)

		while len(stack) > 0:
			node = stack.pop()
			traversal += str(node.value) + " "
		return traversal


	#  reverse-order
	def reverse_order_print(self, start):  
		if start is None:
			return 

		queue = Queue()
		stack = Stack()
		queue.enqueue(start)

		traversal = ""
		while len(queue) > 0:
			node = queue.dequeue()
			stack.push(node)
			if node.left:
				queue.enqueue(node.left)

			if node.right:
				queue.enqueue(node.right)

		while len(stack) > 0:
			node = stack.pop()
			traversal += str(str(node.value)) + " "
		return traversal


	# pre-order
	def tree_height(self, start, height, counter):
		if counter>height : height = counter
		counter+=1
		# print(height)
		if start:
			height = self.tree_height(start.left, height, counter)
			height = self.tree_height(start.right, height, counter)
		return height


	def size(self,  size = 0):  
		if self.root is None:
			return 0

		stack = Stack()
		stack.push(self.root)

		while stack:
			node = stack.pop()
			if node.left:
				stack.push(node.left)
				size+=1

			if node.right:
				stack.push(node.right)
				size+=1

		return 1+size # add root node


	def size_short(self, node):  
		if node is None:
			return 0

		return 1 + self.size_short(node.left) + self.size_short(node.right) # add root node


	def height(self, node):
		if node is None:
			return -1

		left_height = self.height(node.left)
		right_height = self.height(node.left)

		return 1 + max(right_height, left_height)

# Full binary tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

tree.root.left.left.left = Node(8)
tree.root.left.left.right = Node(9)
tree.root.left.right.left = Node(10)
tree.root.left.right.right = Node(11)

tree.root.right.left.left = Node(12)
tree.root.right.left.right = Node(13)
tree.root.right.right.left = Node(14)
tree.root.right.right.right = Node(15)


# print(tree.preorder_print(tree.root, ''))

# print(tree.inorder_print(tree.root, ''))

# print(tree.postorder_print(tree.root, ''))

# print(tree.reverse_levelorder_print(tree.root))

# print(tree.tree_height(tree.root.left, 0, 0))

# print(tree.height(tree.root.left, 0, 0))


print(tree.size_short(tree.root))


