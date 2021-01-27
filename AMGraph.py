#!/usr/bin/python3

from array_queue import ArrayQueue

class AMGraph:
  """ Partial Graph ADT represented by an adjacency matrix.
      From this point on, the term 'adjacency matrix' is denoted 'AM'. """

  #------------------------- nested Vertex class -------------------------
  class Vertex:
    """ Lightweight vertex structure for a graph. """
    __slots__ = '_element', '_label'

    def __init__(self, x, label="UNEXPLORED"):
      """ Do not call constructor directly. Use Graph's addVertex(). """
      self._element = x
      self._label = label

    def element(self):
      """Return element associated with this vertex."""
      return self._element

    def getLabel(self, label):
      """ Get label assigned to this vertex. """
      return self._label

    def setLabel(self, label):
      """ Set label after the vertex has been created. """
      self._label = label

    def __str__(self):
      """ Used when printing this object. """
      return str(self._element)

  #------------------------- nested Edge class -------------------------
  class Edge:
    """ Lightweight edge structure for a graph. """
    __slots__ = '_origin', '_destination', '_element', '_label'

    def __init__(self, u, v, x=None, label="UNEXPLORED"):
      """Do not call constructor directly. Use Graph's addEdge(). """
      self._origin = u
      self._destination = v
      self._element = x
      self._label = label

    def getLabel(self, label):
      """ Get label assigned to this edge. """
      return self._label

    def setLabel(self, label):
      """ Set label after the edge has been created. """
      self._label = label

    def endpoints(self):
      """ Return (u,v) tuple for vertices u and v. """
      return (self._origin, self._destination)

    def opposite(self, v):
      """ Return the vertex that is opposite v on this edge. """
      if not isinstance(v, AMGraph.Vertex):
        raise TypeError('v must be a Vertex')
      return self._destination if v is self._origin else self._origin
      raise ValueError('v not incident to edge')

    def element(self):
      """ Return element associated with this edge. """
      return self._element

    def __str__(self):
      """ Used when printing this object. """
      return '({0},{1},{2})'.format(self._origin,self._destination,self._element)


  #------------------------- Graph methods -------------------------
  __slots__ = '_AM', '_V', '_E'  # A 2D list representing the AM
  # Implement this

  #-- c'tor
  def __init__(self, filename):
    # ... Implement this
    # Open the given file, create an AM of the size specified in the file
    #open file
    # Read data from the file, and insert edges into the AM
    file = open(filename,'r')
    f1 = file.readlines()

    #set up matrix    
    m = int(f1[0])
    n = int(f1[1])
    self._AM = [0] * m
    for i in range(m):
      self._AM[i] = [0] * m

    #store vertices and edges
    self._V = []
    self._E = []

    #add edges to matrix
    for i in range(2, len(f1)):
        x = f1[i]
        x = x.split(' ')
        x[1] = int(x[1].replace('\n',''))
        x[0] = int(x[0])
        self._AM[int(x[0])][int(x[1])] = 1
        self._AM[int(x[1])][int(x[0])] = 1

        #create the edge
        if self.Edge(x[0], x[1]) not in self._E:
          self._E.append(AMGraph.Edge(x[0],x[1]))

    #create vertices
    for i in range(len(self._AM)):
      self._V.append(AMGraph.Vertex(i))

    #for visualization
    for i in range(m):
        print(i, self._AM[i])
        print()

    return

  #-- Public methods
  def vertexCount(self):
    """ Return the number of vertices in the graph. """
    # ... Implement this
    return len(self._V)


  def vertices(self):
    """ Return an iteration of all vertices of the graph. """
    # ... Implement this
    return self._V


  def edgeCount(self):
    """ Return the number of edges in the graph. """
    # ... Implement this
    return len(self._E)

  def edges(self):
    """ Return a set of all edges of the graph. """
    # ... Implement this
    E = []
    for edges in range(len(self._E)):
      E.append((self._E[edges]._origin, self._E[edges]._destination))
    return E


  def addEdge(self, v1, v2):
    """ Add the edge represented by vertices v1 and v2 to the AM. """
    # ... Implement this
    self._AM[v1][v2] == 1
    self._AM[v2][v1] == 1
    self._E.append(AMGraph.Edge(v1, v2))
    return


  def getEdge(self, v1, v2):
    """ Return the edge from v1 to v2, or None if not adjacent. """
    # ... Implement this
    if self._E[v1][v2] == 1:
      return self._E[v1][v2]
    else:
      return None


  def incidentEdges(self, v):
    """ Return a collection of all edges incident to vertex v in the graph. """
    # ... Implement this
    v.edges = []
    for vertex in range(len(self._AM)):
      if self._AM[v][vertex] == 1:
        v.edges.append((v, vertex))
    return v.edges


def BFS(g, minlevel=1):
  # ... Implement this according to the algorithm from the class notes,
  # and with the extra restrictions mentioned in the assignment
  Q = ArrayQueue()
  done = []
  Q.enqueue(0)

  def _BFS(g, minlevel):
    if Q.is_empty() == True:
      print(minlevel) 
    else:
      m = Q.dequeue()
      for vertex in range(len(g._AM)):
        if g._AM[m][vertex] == 1 and m not in done:
          print(m, vertex)
          Q.enqueue(vertex)
      done.append(m)
      return _BFS(g, minlevel)
  
  if Q.is_empty() == True:
    return minlevel
  else:
    _BFS(g, minlevel)


#-- Main method

g = AMGraph("stations.txt")

# Test various methods
print("Vertices:", g.vertexCount())
for v in g.vertices():
  print(v, end=' ')
print()

print("Edges:", g.edgeCount())
for e in g.edges():
  print(e, end=' ')
print()

# Implement the algorithm from the assignment (repeated BFS traversals, etc)
# ...
print(BFS(g))
