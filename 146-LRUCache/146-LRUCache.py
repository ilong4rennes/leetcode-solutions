# Last updated: 5/6/2025, 6:04:24 PM
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = {}
        self.tail = {}
        self.head['next'] = self.tail
        self.tail['prev'] = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node['val']
        else: return -1    

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        node = {'key': key, 'val': value}
        self._add(node)
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            head = self.head['next']
            self._remove(head)
            del self.cache[head['key']]
    
    def _remove(self, node):
        prev = node['prev']
        next = node['next']
        prev['next'] = next
        next['prev'] = prev
    
    def _add(self, node):
        prev = self.tail['prev']
        prev['next'] = node
        self.tail['prev'] = node
        node['prev'] = prev
        node['next'] = self.tail
        
