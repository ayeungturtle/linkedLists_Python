class Node:
  def __init__(self, d, n = None):
    self.data = d 
    self.next_node = n 
  def get_data(self):
    return self.data
  def set_data(self, new_data):
    self.data = new_data
  def get_next_node (self):
    return self.next_node
  def set_next_node (self, new_node):
    self.next_node = new_node
    
class LinkedList:
  def __init__(self, r = None):
    self.root = r 
    self.size = 0
  def get_size (self):
    return self.size
  def add(self,d):
    new_node = Node(d,self.root)
    self.root = new_node
    self.size += 1
  def remove(self,d):
    cur_node = self.root
    if (cur_node.data == d):
      if cur_node.next_node == None:
        self.root = None
      else:
        self.root = cur_node.next_node
      return True
    while (cur_nod)e:
      last_node = cur_node
      cur_node = cur_node.next_node
      if(cur_node.data == d):
        last_node.next_node = cur_node.next_node
        return True
    return False
  def print(self):
    cur_node = self.root
    while (cur_node.next_node != None):
      print (cur_node.data)
      cur_node = cur_node.next_node
    print (cur_node.data)
  def find(self,d):
    cur_node = self.root
    while (cur_node):
      if (cur_node.data == d):
        return d
      cur_node = cur_node.next_node
    return None
      
    

testLinkedList = LinkedList()
testLinkedList.add(12)
testLinkedList.add(7478)
testLinkedList.add(145)
testLinkedList.add(145)
testLinkedList.add(9087)
testLinkedList.add(12)

print(testLinkedList.remove(12))

testLinkedList.print()
print(testLinkedList.find(12))
        
    