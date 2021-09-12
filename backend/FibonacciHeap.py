import copy
class FibonacciHeap:

  class Node:
    def  __init__(self, key, process = None):
      self.key = key
      self.parent = None
      self.prev = None
      self.next = None
      self.child = None
      self.rank = 0
      self.mark = False
      self.process = process
    
    def __str__(self):
      return "Key: " + str(self.key) + " next key: " + str((self.next).key) + " prev key: " + str((self.prev).key) + " rank: " + str(self.rank) + " child: ( " + str(self.child) + " )" 

  def __init__(self):
    self.heap = None
    self.head = None

  def insert(self, key, process):
    node = self.Node(key, process)
    
    if self.head is None:
      node.prev = node
      node.next = node
      self.heap = node
      self.head = node

    else:

      ((self.head).prev).next = node
      node.prev = ((self.head).prev)
      node.next = self.head
      (self.head).prev = node

      if (node.key < (self.head).key):
        self.head = node
        
  def printHeap(self):
    print((self.head))
    if self.head is not None:
      next = (self.head).next
      while next != self.head:
        print(next)
        next = next.next

  def findNewMin(self):
    node = (self.head).next
    minNode = node
    while (node != self.head):
      if node.key < minNode.key:
        minNode = node
      node = node.next

    return minNode

  def ascend(self, node):
    #elegimos el menor de los hijos
    minNode = node
    nextNode = node.next
    while nextNode.key != node.key:
      if nextNode.key < minNode.key:
        minNode = nextNode
      nextNode = nextNode.next
    
    #print('Minimo para ascension: (' + str(minNode) + ')' +' reemplaza a ' + str(node.parent))
    nextNode = minNode.next
    #print('primer hermano: ' +str(nextNode))
    while nextNode != minNode:
      actNode = copy.deepcopy(nextNode)
      nextNode = nextNode.next
      #print('1:' + str(actNode))
      self.deleteReference(actNode)
      self.insertChild(minNode,actNode)
      #print('2' + str(minNode))

    minNode.padre = None
    self.insertNodeToRoot(minNode)
  
  def delete(self):
    x = self.head

    if self.head is None:
      return None
    if self.head == self.head.next and self.head.child is None:
        self.head = None
    else:
      if self.head.child is not None:
        self.ascend(self.head.child)
      newMin = self.findNewMin()
      self.deleteReference(self.head)

      self.head = newMin


      self.consolidate()

    return x

  def consolidate(self):
    rankings = {}
    node = self.head.next
    rankings[self.head.rank] = self.head
    #print("head: " + str(self.head.key))
    while node != self.head:
      #print("node: " + str(node.key))
      if rankings.get(node.rank) is None:
        rankings[node.rank] = node
      else:
        self.merge(rankings.get(node.rank), node)
        break
      node = node.next

  def deleteReference(self,node):
    #print("deleting reference:" + str(node.key))
    if node.next == node:
      if node.parent is not None and node.parent.child == node:
        (node.parent).child = None
      else:
        self.heap = None
        self.head = None

    else:
      if node.parent is not None and node.parent.child == node:
        node.parent.child = node.next 
      (node.next).prev = node.prev
      (node.prev).next = node.next    

    #self.printHeap()

  def insertChild(self, parent, child):
    #print("inserting child: " + str(child.key) + " to parent: " + str(parent.key))
    child.parent = parent
    parent.rank += 1

    if parent.child is None:
      parent.child = child
      child.next = child
      child.prev = child
    
    else:
      ((parent.child).prev).next = child
      child.prev = ((parent.child).prev)

      child.next = parent.child
      parent.child.prev = child

  def merge(self, node1, node2):
    #print("Merging: " + str(node1.key) + " with " + str(node2.key) )
    if node1.key < node2.key:
      self.deleteReference(node2)
      self.insertChild(node1,node2)
    else:
      self.deleteReference(node1)
      self.insertChild(node2,node1)

    #self.printHeap()
    self.consolidate()

  def insertNodeToRoot(self, node):

    ((self.head).prev).next = node
    node.prev = ((self.head).prev)
    node.next = self.head
    (self.head).prev = node
    node.parent = None

    if (node.key < (self.head).key):
      self.head = node
  
  def decreaseKey(self, node, k):
    if node.key < k:
      print("It's greater than the original key")
      return

    node.key = k
    parent = node.parent
    if parent is not None and node.key < parent.key:
      self.deleteReference(node)
      self.insertNodeToRoot(node)
      if parent.mark:
        parent.mark = False
        self.decreaseKey(parent, parent.key)
      
      else:
          parent.mark = True
    