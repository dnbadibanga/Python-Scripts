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

"""Basic example of an adapter class to provide a stack interface to Python's list."""

from exceptions import Empty

class ArrayStack:
  """LIFO Stack implementation using a Python list as underlying storage."""

  def __init__(self):
    """Create an empty stack."""
    self._Edata = []                       # nonpublic list for even stack
    self._Odata = []                       # nonpublic list for odd stack

  def Esize(self):
    """Return the number of elements in the even stack."""
    return len(self._Edata)

  def Osize(self):
    """Return the number of elements in the odd stack."""
    return len(self._Odata)

  def isEEmpty(self):
    """Return True if the even stack is empty."""
    return len(self._Edata) == 0

  def isOEmpty(self):
    """Return True if the odd stack is empty."""
    return len(self._Odata) == 0

  def push(self, e):
    """Add element e to the top of the appropriate stack."""
    if len(self._Edata) + len(self._Odata) == 200:
        return ('Stacks are full')
    else:
        #if value is too high
        if e > 500:
            print ('Value is too high')
        
        elif e % 2 == 0:
            self._Edata.append(e)            # new item stored at end of list
        else:
            self._Odata.append(e)
            

  def Etop(self):
    """Return (but do not remove) the element at the top of the even stack.

    Raise Empty exception if the stack is empty.
    """
    if self.isEEmpty():
        raise Empty('Even Stack is empty')
    else:
        return self._Edata[-1]                 # the last item in the list

  def Otop(self):
    """Return (but do not remove) the element at the top of the odd stack.

    Raise Empty exception if the stack is empty.
    """
    if self.isOEmpty():
        raise Empty('Odd Stack is empty')
    else:
        return self._Odata[-1]                 # the last item in the list

  def Epop(self):
    """Remove and return the element from the top of the even stack (i.e., LIFO).

    Raise Empty exception if the stack is empty.
    """
    if self.isEEmpty():
        raise Empty('Even Stack is empty')
    else:
        return self._Edata.pop()               # remove last item from list

  def Opop(self):
    """Remove and return the element from the top of the odd stack (i.e., LIFO).

    Raise Empty exception if the stack is empty.
    """
    if self.isOEmpty():
        print('Odd Stack is empty')
    else:
        return self._Odata.pop()               # remove last item from list

S = ArrayStack()
print(S.isEEmpty())
S.Opop()
S.push(10)
S.push(7)
S.push(4)
print(S.Osize())
print(S.Esize())
S.push(90)
S.push(33)
S.push(501)
S.push(500)
print(S.Etop())
print(S.Otop())
print(S.isOEmpty())
S.Epop()
S.Opop()
S.Otop()
