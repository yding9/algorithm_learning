#stack first in last out
class Stack:
  def __init__(self):
    self.data = []
    self.length = 0
    self.top = 0 # this is recording the next top's element location
  
  def isEmpty(self):
    return self.length == 0
      
  def push(self,item):
    self.data.append(item)
    self.length = self.length + 1
    self.top = self.top + 1
    
  def peek(self):
    if self.isEmpty():
      raise Exception('this is an empty stack') 
    return self.data[self.top-1]
  
  def size(self):
    return self.length
   
  def pop(self):
    if self.isEmpty(): 
      raise Exception('this is an empty stack')
    popitem = self.data[self.top-1]
    self.data.pop()
    self.top = self.top - 1
    self.length = self.length -1
    return popitem
    
    
def main():
  s = Stack()
  s.push("A")
  s.push("B")
  s.push("C")
  s.push("D")
  print(s.peek())
  print(s.size())
  print(s.pop())
  print(s.pop())
  print(s.pop()) 
  print(s.size())
  print(s.pop())
  print(s.pop()) #this will raise an error (this is an empty stack)

if __name__ == "__main__":
  main() 