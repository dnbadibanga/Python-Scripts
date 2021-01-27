##Divine Ndaya Badibanga
##201765203

# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from exceptions import Empty

class IntBag:
  """LIFO Stack implementation using a singly linked list for storage."""
  _CAPACITY = 10

  #-------------------------- nested _Node class --------------------------
  class _Node:
    """Lightweight, nonpublic class for storing a singly linked node."""
    __slots__ = '_element', '_next'         # streamline memory usage

    def __init__(self, element, next):      # initialize node's fields
      self._element = element               # reference to user's element
      self._next = next                     # reference to next node

  #------------------------------- bag methods -------------------------------
  def __init__(self):
    """Create an empty bag."""
    self._head = None                       # reference to the head node
    self._size = 0                          # number of bag elements

  def size(self):
    """Return the number of elements in the bag."""
    return self._size

  def isEmpty(self):
    """Return True if the bag is empty."""
    return self._size == 0

  def add(self, e):
    """Add element e to the bag."""
    if self._size < self._CAPACITY:
        self._head = self._Node(e, self._head)  # create and link a new node
        self._size += 1
    else:
        print('Your bag is full')

  def removeOne(self, e):
    """Remove a specified item from a bag"""
    value = e
    prev = None
    curr = self._head
    #if bag is empty
    if self.isEmpty:
        raise Empty('Your bag is empty.')
        return
    #go through all elements in bag
    while curr != None:
        #when value is found
        if curr._element == value:
            #if the value is at the head of the bag
            if prev == None:
                self._head = curr._next
                self._size -= 1
            else:
                prev._next = curr._next
            self._size -= 1
            break
        #update active elements
        prev = curr
        curr = prev._next

  def removeAll(self, e):
    """Remove all occurrences of a specified item."""
    value = e
    prev = None
    curr = self._head
    #if bag is empty
    if self._size == 0:
        raise Empty('Your bag is empty.')
        return
    #go through all elements in bag
    while curr != None:
        #when value is found
        if curr._element == value:
            #if element is at the head of the bag
            if prev == None:
                self._head = curr._next
            else:
                prev._next = curr._next
            self._size -= 1
        #update active elements
        prev = curr
        curr = curr._next

  def count(self, e):
    """Determine the number of occurrences of a specified item in the bag"""
    x = e
    counter = 0
    curr = self._head
    #if bag is empty
    if self._size == 0:
        raise Empty('Your bag is empty.')
        return
    #go through entire list and find at least one occurrence 
    while curr != None:
        if curr._element == x:
            counter += 1
            break
        curr = curr._next
    return counter

  def find(self, e):
    """Determine whether or not a specified item is in the bag"""
    x = e
    found = False
    curr = self._head
    #go through all elements in bag
    while curr != None:
        #when value is found
        if curr._element == x:
            found = True
            return 'found'
        curr = curr._next
        if curr == None and found != True:
            return 'not found'
        

  def openBag(self):
    """print the contents of a bag"""
    if self._size == 0:
        print('Your bag is empty')
        return
    curr = self._head
    #create a list
    bag = []
    #add all elements to list and print list
    while curr != None:
        bag.append(curr._element)
        curr = curr._next
    return bag

#TEST CODE
if True:
    S = IntBag()
    print(S.isEmpty())
    print(S.openBag())
    S.add(3)
    S.add(9)
    S.add(4)
    S.add(3)
    S.add(5)
    print(S.size())
    print(S.openBag())
    print(S.find(2))
    print(S.find(4))
    S.add(1)
    print(S.count(3))
    print(S.openBag())
    S.removeOne(5)
    S.removeAll(3)
    print(S.openBag())
    print(S.isEmpty())
    print(S.size())

   
    






