class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity
    self.priority = [0]*capacity
    self.result = False
    self.temp = []

  def append(self, item):
    mina = self.priority[0]
    minI = 0

    for i in range(0,len(self.storage)):

      if self.storage[i] is None:
        self.storage[i] = item
        self.priority[i] = len(self.storage)
        break
      else:
        if(self.priority[i]>0):
          self.priority[i] -= 1

    if len(self.temp) == len(self.storage):
      for i in range(1,len(self.priority)):
        if mina > self.priority[i]:
          mina = self.priority[i]
          minI = i
      
      for i in range(0,len(self.storage)):
        if i == minI :
          self.storage[i] = item
          self.priority[i] = len(self.storage)
        else:
          self.priority[i] -= 1     

  def get(self):
    print(f'priority : {self.priority}')
    res = [] 
    for val in self.storage: 
      if val != None : 
        res.append(val)
    self.temp = list(res)
    return res