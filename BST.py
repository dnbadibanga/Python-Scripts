#!/usr/bin/python3

import random

class BST:
  """Binary search tree based on 'BTNode's."""
  __slots__ = 'root'

  #-------------------------- nested BTNode class --------------------------
  class _BTNode:
    """ Lightweight, nonpublic class for storing a BTNode. """
    __slots__ = 'key','element', 'left', 'right'

    def __init__(self, key, element, left = None, right = None):
      self.key = key
      self.element = element
      self.left    = left
      self.right   = right

    def hasLeft(self):
      """ Returns whether this node has a left child. """
      return self.left != None

    def hasRight(self):
      """ Returns whether this node has a right child. """
      return self.right != None

    def __lt__(self, other):
      """ Return True if other is a BTNode and this node is less than other. """
      return type(other) is type(self) and self.element < other.element

    def __gt__(self, other):
      """ Return True if other is a BTNode and this node is greater than other. """
      return type(other) is type(self) and self.element > other.element

    def __eq__(self, other):
      """ Return True if other is a BTNode and this node is equal to the other. """
      return type(other) is type(self) and self.element == other.element

  #-- c'tor
  def __init__(self):
    self.root = None


  #-- Public methods
  def insert(self, key, element):
    """ Insert element into the BST, keeping the BST property. """
    def _insert(root, key, element):
      if self.root == None:
        self.root = self._BTNode(key, element)
        #print(root.key, root.element)
      elif key < self.root.key:
        if self.root.hasLeft():
          self.root = root.left
          return _insert(self.root, key, element)
        else:
          self.root.left = self._BTNode(key, element)
        print(self.root.left.key, self.root.left.element)
      elif key > self.root.key:
        if self.root.hasRight():
          self.root = self.root.right
          return _insert(self.root, key, element)
        else:
          self.root.right = self._BTNode(key, element)
        print(self.root.right.key, self.root.right.element)
      else:
        # We don't insert duplicate elements
        # However, in a map we *can* update the value if the key is the same
        self.root.element = element
        print(self.root.element)

    return _insert(self.root, key, element)

    #if self.root == None:   # Special case for when tree is empty
    #  self.root = self
    #else:


  def remove(self, key):
    """ Remove key from the BST, keeping the BST property.
        Return True if deletion succeeded, else False. """
    # ... Implement this
    return False


  def find(self, element):
    """ Search for key in the BST, returning the corresponding value (-1 if not found). """
    # ... Implement this
    return -1


  def keys(self):
    """ Collect all keys into a list, then return it. """
    # ... Implement this
    return []


  def values(self):
    """ Collect all values into a list, then return it. """
    # ... Implement this
    return []


  def print(self):
    """ Print tree using inorder traversal. """
    def _print(root):
      if self.root != None:
        if self.root.hasLeft():
          return
        #_print(root.left)
        #print(root.element, end=' ')
        #_print(root.right)

    return _print(self.root)
    #print()


  def draw(self):
    """ Draw tree keys in a triangular pattern.
        For example, if key insertion was '2 1 3', then output should be similar to:
            2
          1   3
        Hint: Do a 'level-order' traversal on the tree and place the results in a list,
              using '_' when a gap occurs.  Then use this list to properly space the
              output horizontally.  Essentially, you want to create the equivalent
              to an array-based BST, with '_' for gaps.  The length of this list then
              determines how to space the output.

        ALGORITHM levelOrderTraversal(root)
          place root in a Queue
          while Queue not empty
            remove node from queue
            process its contents
            place its left and right children in the queue
    """
    # ... Implement this


#-- Main method
###  DO NOT CHANGE ANY CODE BELOW!  YOU WILL RECEIVE 0% FOR THIS QUESTION
###  IF YOU DO!!!  YOUR CODE *MUST* WORK WITH THIS MAIN FUNCTION.
tree = BST()

print("Inserting 10 random key/value pairs ...")
for x in range(9):
  tree.insert(random.randint(1,100), random.randint(1,21))
tree.insert(100, "found me!")
print()

print("Testing print ...")
tree.print()
print()

print("Testing lookup ...")
print("Searching for", 2, ": ", tree.find(2))
print("Searching for", 100, ": ", tree.find(100))
print()

print("Testing deletion ...")
print("Remove", 2, ": ", tree.remove(2))
print("Remove", 100, ": ", tree.remove(100))
print()

print("Requesting all keys ...")
for key in tree.keys():
  print(key, end=' ')
print()
print()

print("Requesting all values ...")
for value in tree.values():
  print(value, end=' ')
print()
print()

print("Drawing the BST keys ...")
tree.draw()
print()
