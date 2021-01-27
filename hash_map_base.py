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

from map_base import MapBase
from collections import MutableMapping
from random import randrange         # used to pick MAD parameters

class HashMapBase(MapBase):
  """Abstract base class for map using hash-table with MAD compression."""
  _AVAIL = object()

  """Keys must be hashable and non-None.
  """

  def __init__(self, cap=83, p=109345121):
    """Create an empty hash-table map.

    cap     initial table size (default 11)
    p       positive prime used for MAD (default 109345121)
    """
    self._table = cap * [ None ]
    self._n = 0                                   # number of entries in the map
    self._prime = p                               # prime for MAD compression
    self._scale = 1 + randrange(p-1)              # scale from 1 to p-1 for MAD
    self._shift = randrange(p)                    # shift from 0 to p-1 for MAD
    self._a = 33

  def _hash_function(self, k):
    x = k[0-6]
    n = len(k)
    p = x[n-1]
    i = n - 2
    while i >= 0:
      p = p*(self._a) + x[i]
      i = i - 1
    return (p*self._scale + self._shift) % self._prime % len(self._table)

  def __len__(self):
    return self._n

  def __getitem__(self, k):
    j = self._hash_function(k)
    return self._bucket_getitem(j, k)             # may raise KeyError

  def __setitem__(self, k, v):
    j = self._hash_function(k)
    self._bucket_setitem(j, k, v)                 # subroutine maintains self._n
    if self._n > len(self._table) // 2:           # keep load factor <= 0.5
      self._resize(2 * len(self._table) - 1)      # number 2^x - 1 is often prime

  def __delitem__(self, k):
    j = self._hash_function(k)
    self._bucket_delitem(j, k)                    # may raise KeyError
    self._n -= 1

  def _resize(self, c):
    """Resize bucket array to capacity c and rehash all items."""
    old = list(self.items())       # use iteration to record existing items
    self._table = c * [None]       # then reset table to desired capacity
    self._n = 0                    # n recomputed during subsequent adds
    for (k,v) in old:
      self[k] = v                  # reinsert old key-value pair

  def _bucket_getitem(self, j, k):
    found, s = self._find_slot(j, k)
    if not found:
      raise KeyError('Key Error: ' + repr(k))        # no match found
    return self._table[s]._value

  def _bucket_setitem(self, j, k, v):
    found, s = self._find_slot(j, k)
    if not found:
      self._table[s] = self._Item(k,v)               # insert new item
      self._n += 1                                   # size has increased
    else:
      self._table[s]._value = v                      # overwrite existing

  def _bucket_delitem(self, j, k):
    found, s = self._find_slot(j, k)
    if not found:
      raise KeyError('Key Error: ' + repr(k))        # no match found
    self._table[s] = QuadHashMap._AVAIL             # mark as vacated

  def quadraticprobing(self, k):
    found = False
    limit = self._n
    i = 1
    while i <= limit:
      newk = k + (i**2)
      newk = newk % self._n

      if self._table[newk] == 0:
        found = True
      else:
        i += 1
    return found, newk

  def insert(self, k, v):
    self.__setitem__(k,v)

  def delete(self, k):
    self.__delitem__(k)

  def printMap(self):
    return self.__iter__(self)

  
Map = HashMapBase()
f = open('thenames.txt', 'r')

f1 = f.readlines()
for i in range(25):
    word = f1[i]
    Map.insert(word.replace('\n',''))

Map.printMap()

for i in range(10,20):
  word = f1[i]
  Map.delete(word.replace('\n',''))

Map.printMap()

for i in range(26,50):
  word = f1[i]
  Map.insert(word.replace('\n',''))

Map.printMap()




  

