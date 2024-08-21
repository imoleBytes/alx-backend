#!/usr/bin/env python3
"""
Create a class MRUCache that inherits from BaseCaching and is a
 caching system:

You must use self.cache_data - dictionary from the parent class BaseCaching
You can overload def __init__(self): but don’t forget to call the parent init:
 super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher that
BaseCaching.MAX_ITEMS:
you must discard the most recently used item (MRU algorithm)
you must print DISCARD: with the key discarded and following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Cache system implementing the MRU algorithm"""
    def __init__(self):
        """ initialize"""
        super().__init__()

    def put(self, key, item):
        """ putting data into the cache"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            del self.cache_data[key]
        self.cache_data.update({key: item})
        if len(self.cache_data) > self.MAX_ITEMS:
            key_to_remove = list(self.cache_data.keys())[-2]
            del self.cache_data[key_to_remove]
            print(f"DISCARD: {key_to_remove}")

    def get(self, key):
        """ getting data from cache"""
        if key is None or key not in self.cache_data:
            return
        ordered_list = list(self.cache_data.keys())
        if key == ordered_list[-1]:
            return self.cache_data[key]
        val = self.cache_data[key]
        del self.cache_data[key]
        self.cache_data.update({key: val})
        return val


if __name__ == "__main__":
    my_cache = MRUCache()
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
