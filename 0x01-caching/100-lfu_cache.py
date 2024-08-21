#!/usr/bin/env python3
"""
Create a class LFUCache that inherits from BaseCaching and is a
 caching system:

You must use self.cache_data - dictionary from the parent class BaseCaching
You can overload def __init__(self): but don’t forget to call the parent
 init: super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher that
BaseCaching.MAX_ITEMS:
you must discard the least frequency used item (LFU algorithm)
if you find more than 1 item to discard, you must use the LRU algorithm to
 discard only the least recently used
you must print DISCARD: with the key discarded and following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """cache system with the LFU algorithm"""
    def __init__(self):
        """initialize"""
        super().__init__()
        self.hits = {}

    def put(self, key, item):
        """storing data into cache"""
        if key is None or item is None:
            return
        if len(self.cache_data) < self.MAX_ITEMS:
            # normal
            self.cache_data.update({key: item})
            if key in self.hits:
                self.hits[key] += 1
            else:
                self.hits[key] = 1
        else:
            # craziness starts here
            if key in self.cache_data:
                self.cache_data.update({key: item})
                self.hits[key] += 1
                return
            key_with_the_lowest_hits = min(self.hits, key=self.hits.get)
            del self.cache_data[key_with_the_lowest_hits]
            del self.hits[key_with_the_lowest_hits]
            self.put(key, item)
            print(f"DISCARD: {key_with_the_lowest_hits}")

    def get(self, key):
        """getting data from cache"""
        if key is None or key not in self.cache_data:
            return
        self.hits[key] += 1
        return self.cache_data[key]


if __name__ == "__main__":
    my_cache = LFUCache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.put("D", "School")
    my_cache.print_cache()
    print(my_cache.get("B"))
    my_cache.put("E", "Battery")
    my_cache.print_cache()
    my_cache.put("C", "Street")
    my_cache.print_cache()
    print(my_cache.get("A"))
    print(my_cache.get("B"))
    print(my_cache.get("C"))
    my_cache.put("F", "Mission")
    my_cache.print_cache()
    my_cache.put("G", "San Francisco")
    my_cache.print_cache()
    my_cache.put("H", "H")
    my_cache.print_cache()
    my_cache.put("I", "I")
    my_cache.print_cache()
    print(my_cache.get("I"))
    print(my_cache.get("H"))
    print(my_cache.get("I"))
    print(my_cache.get("H"))
    print(my_cache.get("I"))
    print(my_cache.get("H"))
    my_cache.put("J", "J")
    my_cache.print_cache()
    my_cache.put("K", "K")
    my_cache.print_cache()
    my_cache.put("L", "L")
    my_cache.print_cache()
    my_cache.put("M", "M")
    my_cache.print_cache()
