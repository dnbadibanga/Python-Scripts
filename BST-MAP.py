#!/usr/bin/python3

import random

from array_queue import ArrayQueue

class BST:
  """Binary search tree based on 'BTNode's."""
  __slots__ = 'root'

  #-------------------------- nested BTNode class --------------------------
  class _BTNode:
    """ Lightweight, nonpublic class for storing a BTNode. """
    __slots__ = 'key', 'value', 'left', 'right'

    def __init__(self, key, value, left = None, right = None):
      self.key = key
      self.value = value 
      self.left  = left
      self.right = right

    def hasLeft(self):
      """ Returns whether this node has a left child. """
      return self.left != None

    def hasRight(self):
      """ Returns whether this node has a right child. """
      return self.right != None

    def __lt__(self, other):
      """ Return True if other is a BTNode and this node is less than other. """
      return type(other) is type(self) and self.key < other.key

    def __gt__(self, other):
      """ Return True if other is a BTNode and this node is greater than other. """
      return type(other) is type(self) and self.key > other.key

    def __eq__(self, other):
      """ Return True if other is a BTNode and this node is equal to the other. """
      return type(other) is type(self) and self.key == other.key

  #-- c'tor
  def __init__(self):
    self.root = None


  #-- Public methods
  def insert(self, key, value):
    """ Insert element into the BST, keeping the BST property. """
    def _insertNode(root, key, value):
      if root == None:
        # Because of the way this method is written, we can never hit
        # this case; however it's good practice to test for None anyway
        return
      elif key < root.key:   # Go left
        if root.hasLeft():
          _insertNode(root.left, key, value)
        else:
          root.left = node
      elif key > root.key:   # Go right
        if root.hasRight():
          _insertNode(root.right, key, value)
        else:
          root.right = node
      #else:
        # We don't insert duplicate elements
        # However, in a map we *can* update the value if the key is the same

    # Create node to insert
    node = self._BTNode(key, value)

    if self.root == None:   # Special case for when tree is empty
      self.root = node
    else:
      _insertNode(self.root, key, value)


  def remove(self, key):

    def _remove(root, key, test=False):
      """ Remove key from the BST, keeping the BST property.
      Return True if deletion succeeded, else False. """
      if root == None:
        return False

      elif key < root.key:
        if root.hasLeft():
          if(root.left.key == key and test):
            root.left = None
          else:
            return _remove(root.left, key, test)
        else:
          return False

      elif key > root.key:
        if root.hasRight():
          if(root.right.key == key and test):
            root.right = None
          else:
            return _remove(root.right, key, test)
        else:
          return False

      else:
        
        if root.hasRight():
          return True
          temp = root.right         #store the right node
          temp = self.minValue(temp)     #search for the key greater than but closest to the node
          tKey = temp.key           #keep the key of the min value
          tVal = temp.value         #keep the value of the min value
          _remove(self.root, temp.key)             #delete the min value
          root.key = tKey           #replace the deleted key with the min value
          root.value = tVal
        elif root.hasLeft():
          lkey = root.left.key
          lvalue = root.left.value
          _remove(self.root, root.left.key)
          root.key = lkey
          root.value = lvalue
        else:
          _remove(self.root, key, True)

        return True
    
    return _remove(self.root, key)


  def minValue(self, node=None): 

    def _minValue(root, node=None):
      if root != None:
        minKey = root
        if root.hasLeft():
          minKey = _minValue(root.left)
        
        return minKey

    return _minValue(self.root)


  def find(self,key):
    """ Search for key in the BST, returning the corresponding value (-1 if not found). """
    def _find(root, key):
      if root == None:
        return -1

      else:
        if key == root.key:
          return root.value
        
        elif key < root.key:
          return _find(root.left, key)

        elif key > root.key:
          return _find(root.right, key)

    return _find(self.root, key)


  def keys(self):
    """ Collect all keys into a list, then return it. """
    listKeys = []
    def _keys(root):
      if root != None:
        _keys(root.left)
        listKeys.append(root.key)
        _keys(root.right)

    _keys(self.root)

    return listKeys


  def values(self):
    """ Collect all values into a list, then return it. """
    listValues = []
    def _values(root):
      if root != None:
        _values(root.left)
        listValues.append(root.value)
        _values(root.right)

    _values(self.root)

    return listValues 


  def print(self):
    """ Print tree using inorder traversal. """
    def _print(root):
      if root != None:
        _print(root.left)
        print(root.key, end=' ')
        _print(root.right) 

    _print(self.root)
    print()


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
    keys = []
    Q = ArrayQueue()
    Q.enqueue(self.root)
    keys.append(self.root.key)
    #print(self.root.key)

    space = 8
    s = ' ' * space 

    while Q.is_empty() == False:
      
      node = Q.dequeue()
      if self.root.key == node.key:
        print(s, self.root.key)
        space -= 2
        s = ' ' * space
      if node.hasLeft():
        Q.enqueue(node.left)
        keys.append(node.left.key)
        print(s, node.left.key, end=' ')
      elif node.hasLeft() == False:
        print('  ', end=' ')
        #keys.append('_')
        #Q.enqueue('blank')
      if node.hasRight():
        Q.enqueue(node.right)
        keys.append(node.right.key)
        print(node.right.key)
      #elif node.hasRight() == False:
        #keys.append('_')
        #Q.enqueue('blank')
      space -= 2
      s = ' ' * space

    print(keys)
    





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
