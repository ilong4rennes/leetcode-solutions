class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_frequency = 0
        self.cache = {}  # Maps key to (value, frequency)
        self.frequency_map = defaultdict(list)  # Maps frequency to a list of keys

    def _update_frequency(self, key):
        """Update the frequency of a key."""
        value, freq = self.cache[key]
        # Remove the key from its current frequency list
        self.frequency_map[freq].remove(key)
        if not self.frequency_map[freq]:
            del self.frequency_map[freq]
            if self.min_frequency == freq:
                self.min_frequency += 1
        # Update the frequency and move to the next frequency list
        new_frequency = freq + 1
        self.frequency_map[new_frequency].append(key)
        self.cache[key] = (value, new_frequency)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self._update_frequency(key)
        return self.cache[key][0]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.cache:
            # Update value and frequency
            self.cache[key] = (value, self.cache[key][1])
            self._update_frequency(key)
        else:
            # If the cache is full, evict the least frequently used key
            if len(self.cache) >= self.capacity:
                lfu_key = self.frequency_map[self.min_frequency][0]
                self.frequency_map[self.min_frequency].remove(lfu_key)
                if not self.frequency_map[self.min_frequency]:
                    del self.frequency_map[self.min_frequency]
                del self.cache[lfu_key]
            # Add the new key with frequency 1
            self.cache[key] = (value, 1)
            self.frequency_map[1].append(key)
            self.min_frequency = 1

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)