#!/usr/bin/env python3
"""
Create a class LRUCache that inherits from BaseCaching and is a
caching system:

You must use self.cache_data - dictionary from the parent class
 BaseCaching
You can overload def __init__(self): but don’t forget to call the
parent init: super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher that
BaseCaching.MAX_ITEMS:
you must discard the least recently used item (LRU algorithm)
you must print DISCARD: with the key discarded and following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ Cache class that implement the LRU caching algorithm"""
    def __init__(self):
        """ initialize"""
        super().__init__()

    def put(self, key, item):
        """add to the cache data"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            del self.cache_data[key]
        self.cache_data.update({key: item})

        if len(self.cache_data.keys()) > self.MAX_ITEMS:
            first_key = list(self.cache_data.keys())[0]
            del self.cache_data[first_key]
            print(f"DISCARD: {first_key}")

    def get(self, key):
        """getting data"""
        if key is None or key not in self.cache_data:
            return None
        ordered_keys = list(self.cache_data.keys())
        if key == ordered_keys[-1]:
            return self.cache_data.get(key)
        else:
            val = self.cache_data.get(key)
            del self.cache_data[key]
            self.cache_data[key] = val
            return val


if __name__ == "__main__":
    my_cache = LRUCache()
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
    my_cache.put("J", "J")
    my_cache.print_cache()
    my_cache.put("K", "K")
    my_cache.print_cache()
