class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
        self.left,self.right=ListNode(0,0), ListNode(0,0)
        self.left.next=self.right
        self.right.prev=self.left
    def remove(self,node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    
    def insert(self,node):
        pre,nxt=self.right.prev,self.right
        pre.next=node
        nxt.prev=node
        node.next=nxt
        node.prev=pre
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key]=ListNode(key,value)
        self.insert(self.cache[key])
        if len(self.cache)>self.capacity:
            lru=self.left.next
            self.remove(lru)
            del self.cache[lru.key]
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)