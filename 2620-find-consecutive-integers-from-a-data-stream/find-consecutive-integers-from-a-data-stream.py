class DataStream:

    def __init__(self, value: int, k: int):
        self.queue=deque()
        self.value=value
        self.k=k
        self.count=0
        

    def consec(self, num: int) -> bool:
        self.queue.append(num)
      
        if num == self.value:
            self.count+=1
     

        if len(self.queue) > self.k:
            if self.queue[0] ==  self.value:
                self.count-=1
            self.queue.popleft()

        if len(self.queue) == self.k:
            if self.count == self.k :
                return True
        return False
        
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)