class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


def inorder_traversal(root):
  if root:
    inorder_traversal(root.left)
    print(root.value)
    inorder_traversal(root.right)


def preorder_traversal(root):
  if root:
    print(root.value)
    preorder_traversal(root.left)
    preorder_traversal(root.right)


def postorder_traversal(root):
  if root:
    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(root.value)


def breadth_first_traversal(root):
  # Create an queue with the root in it
  queue = [root]

  # loop while there are nodes in the queue
  while(len(queue)):
    node = queue.pop(0)
    print(node.value)

    # Add left child
    if node.left:
      queue.append(node.left)

    #Add right child
    if node.right:
      queue.append(node.right)


def search(root, value):
  # Base Case: No Root or Root is value
  # Either return the root or None
  if root is None or root.value == value: return root

  # Case 1: Value is lower
  if root.value > value: return search(root.left, value)

  # Case 2: Value is higher
  return search(root.right, value)


def insert(root, value):
  # Base Case: Found Empty Position or No Root
  if root is None: return Node(value)

  # Case 1: The value already exists
  if root.value == value: return 'The node already exists'

  # Case 2: Value is greater than the root's value
  elif root.value < value: root.right = insert(root.right, value)

  # Case 2: Valie is less than the root's value
  else: root.left = insert(root.left, value)

  return root


root = insert(None, 18)
insert(root, 14)
insert(root, 5)
insert(root, 16)
insert(root, 25)
insert(root, 21)
insert(root, 39)
# inorder_traversal(root)
# preorder_traversal(root)
# postorder_traversal(root)
breadth_first_traversal(root)