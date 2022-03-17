class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
    self.height = 1

  def __repr__(self):
    return str(self.value)


def inorder_traversal(root):
  if root:
    inorder_traversal(root.left)
    print (f'{root} ', end="")
    inorder_traversal(root.right)


def search(root, value):
  # Base Case: No Root or Root is value
  # Either return the root or None
  if root is None or root.value == value: return root

  # Case 1: Value is lower
  if root.value > value: return search(root.left, value)

  # Case 2: Value is higher
  return search(root.right, value)


def get_height(node):
  if not node: return 0
  return node.height


def get_balance(node):
  if not node: return 0
  return get_height(node.left) - get_height(node.right)


def insert(root, value):
  # Step 1: Do a normal BST insert
  if root is None: return Node(value)
  if root.value == value: return 'The node already exists'
  elif root.value < value: root.right = insert(root.right, value)
  else: root.left = insert(root.left, value)

  # Step 2: Update the heights of all the ancestor nodes
  root.height = 1 + max(get_height(root.left), get_height(root.right))

  # Setp 3: Check the balance
  balance = get_balance(root)


  # Step 4: If the tree is not balanced, we must balance it using 4 different cases
  # Case 1 - Left Rotation: The node is inserted into the right subtree of the right subtree.
  if balance < -1 and value > root.right.value: return rotate_left(root)

  # Case 2 - Right Rotation: The node is inserted into the left subtree of the left subtree.
  if balance > 1 and value < root.left.value: return rotate_right(root)

  # Case 3 - Left-Right Rotation: The node is insterted into the right subtree of the left subtree.
  if balance > 1 and value > root.left.value: 
    root.left = rotate_left(root.left)
    return rotate_right(root)

  # Case 4 - Right-Left Rotation: The node is inserted into the left subtree of the right subtree.
  if balance < -1 and value < root.right.value:
    root.right = rotate_right(root.right)
    return rotate_left(root)

  return root


def rotate_left(root):
  right_child = root.right
  right_left_subtree = right_child.left

  right_child.left = root
  root.right = right_left_subtree
  
  root.height = 1 + max(get_height(root.left), get_height(root.right))
  right_child.height = 1 + max(get_height(right_child.left), get_height(right_child.right))

  return right_child

def rotate_right(root):
  left_child = root.left
  left_right_subtree = left_child.right

  left_child.right = root
  root.left = left_right_subtree

  root.height = 1 + max(get_height(root.left), get_height(root.right))
  left_child.height = 1 + max(get_height(left_child.left), get_height(left_child.right))

  return left_child

root = insert(None, 27)
root = insert(root, 30)
root = insert(root, 32)
root = insert(root, 22)
root = insert(root, 18)
root = insert(root, 19)
root = insert(root, 20)
inorder_traversal(root)
print('')
