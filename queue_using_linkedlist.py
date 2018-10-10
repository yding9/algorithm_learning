# Do not use nested classes.
#implementation of queue using a linked list

#Create the Node class
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
      
  def getData(self):
    return self.data
    
  def getNext(self):
    return self.next
      
  def setData(self, newdata):
    self.data = newdata
    
  def setNext(self, newnext):
    self.next = newnext


#Create the Linked List class      
class Linkedlist:
  def __init__(self):
    self.head = None
    self.tail = None

  def isEmpty(self):
    return self.head == None and self.tail == None
      
  def addTail(self, item):
    addNode = Node(item)
    if self.isEmpty():
      self.head = addNode
    else:  
      self.tail.next = addNode
    self.tail = addNode

      
  def removeHead(self):
    if self.isEmpty():
      raise Exception('This is empty')
    removed = self.head
    self.head = self.head.next
    return removed


#Create the queue class
class Queue:
  def __init__(self):
    self.data = Linkedlist()
    self.length = 0
       
  def size(self):
    return self.length
       
  def enqueue(self, item):
    self.data.addTail(item)
    self.length = self.length + 1
    
  def dequeue(self):
    if self.size() ==0:
      raise Exception('This is an empty queue')
    dequeued = self.data.removeHead()
    self.length = self.length -1
    return dequeued.data
    
    
def main():
  q = Queue()
  q.enqueue("A")
  q.enqueue("B")
  q.enqueue("C")
  q.enqueue("D")
  q.enqueue("E")
  print(q.size())
  print(q.dequeue())
  print(q.size())
  print(q.dequeue())
  print(q.size())
  print(q.dequeue())
  print(q.size())
  print(q.dequeue())
  print(q.size())
  print(q.dequeue())
  print(q.size())
  q.dequeue()  # this is used to raise an error empty queue.


if __name__ == "__main__":
  main()    
     
     
