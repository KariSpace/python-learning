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

class Node(object):
	def __init__(self, value): 
		self.value = value
		self.left = None
		self.right = None

class BinaryTree(object):
	def __init__(self, root):
		self.root = Node(root)

	def print_tree(self, traversal_type):
		if traversal_type == 'preorder':
			return self.preorder_print(tree.root, '')
		if traversal_type == 'inorder':
			return self.inorder_print(tree.root, '')
		if traversal_type == 'postorder':
			return self.postorder_print(tree.root, '')

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
	def levelorder_wrong_print(self, start):

		if start:
			# print(start.value)
			if(start.left):
				print(start.left.value)
			if(start.left):
				print(start.right.value)
			traversal = self.levelorder_print(start.left)
			traversal = self.levelorder_print(start.right)

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

print(tree.levelorder_print(tree.root))


