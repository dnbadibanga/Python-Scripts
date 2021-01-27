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

class ArrayStack:
  """FIFO queue implementation using a Python list as underlying storage."""
  DEFAULT_CAPACITY = 10          # moderate capacity for all new queues

  def __init__(self):
    """Create an empty queue."""
    self._data = [None] * ArrayStack.DEFAULT_CAPACITY
    self._size = 0
    self._front = 0

  def __len__(self):
    """Return the number of elements in the stack."""
    return self._size

  def length(self):
      return self._size
 
  def is_empty(self):
    """Return True if the stack is empty."""
    return self._size == 0

  def push(self, e):
    ##Add an element to the stack

    ##when stack is empty
    if self._size == 0:
        self._data[self._front] = e

    ##when stack is full
    elif self._size == len(self._data):
        raise Empty('Stack is full')

    ##when stack already contains some elements
    else:
        index = self._size - 1
        while index > 0:
            self._data[index] = self._data[index-1]
            index -= 1
        self._data[self._front] = e

    ##increment size of queue by one
    self._size += 1

  def top(self):
    ##Return, but do not remove, the element at the top of the stack
    return self._data[self._front]

  def pop(self):
    ##Remove and return the element at the top of the stack

    if self.is_empty():
        print('This stack is empty')
    else:
        x = self._data[self._front]
        index = 1
        while index != self._size:
            self._data[index-1] = self._data[index]
            index += 1

        self._size -= 1
        return x
      

if True:
    S = ArrayStack()
    print(S.is_empty())
    S.push(5)
    print(S.length())
    print(S.top())
    S.push(9)
    print(S.length())
    S.push(7)
    print(S.length())
    print(S.top())
    S.pop()
    print(S.length())
    print(S.top())
    S.pop()
    S.pop()
    S.pop()
    print(S.length())
    

            
        
      
