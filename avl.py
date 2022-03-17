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
  pass


def get_balance(node):
  pass


def insert(root, value):
  # Step 1: Do a normal BST insert
  if root is None: return Node(value)
  if root.value == value: return 'The node already exists'
  elif root.value < value: root.right = insert(root.right, value)
  else: root.left = insert(root.left, value)

  # Step 2: Update the heights of all the ancestor nodes

  # Setp 3: Check the balance


  # Step 4: If the tree is not balanced, we must balance it using 4 different cases
  # Case 1 - Left Rotation: The node is inserted into the right subtree of the right subtree.

  # Case 2 - Right Rotation: The node is inserted into the left subtree of the left subtree.

  # Case 3 - Left-Right Rotation: The node is insterted into the right subtree of the left subtree.

  # Case 4 - Right-Left Rotation: The node is inserted into the left subtree of the right subtree.




def rotate_left(root):
  pass
  # Set up Holder Variables

  # Rotate

  # Update Heights

  # Return the New Root


def rotate_right(root):
  pass
  # Set up Holder Variables

  # Rotate

  # Update Heights

  # Return the New Root





# Test Left Rotation
# root = insert(None, 27)
# root = insert(root, 30)
# root = insert(root, 32)
# print(root.left, root, root.right)

# Test Right Rotation
# root = insert(None, 27)
# root = insert(root, 25)
# root = insert(root, 22)
# print(root.left, root, root.right)

# Test Left Right Rotation
# root = insert(None, 27)
# root = insert(root, 23)
# root = insert(root, 25)
# print(root.left, root, root.right)

# Test Right Left Rotation
# root = insert(None, 27)
# root = insert(root, 32)
# root = insert(root, 30) 
# print(root.left, root, root.right)