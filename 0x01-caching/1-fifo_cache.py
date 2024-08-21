#!/usr/bin/env python3
"""
Create a class FIFOCache that inherits from BaseCaching and is a
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
you must discard the first item put in cache (FIFO algorithm)
you must print DISCARD: with the key discarded and following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """first in first out algo implemented if cache is full"""
    def __init__(self):
        """initialiize"""
        super().__init__()

    def put(self, key, item):
        """put item in cache, followthe first i first out
        algorithm if cache is full
        """
        if not key or not item:
            return
        self.cache_data.update({key: item})

        if len(self.cache_data.keys()) > BaseCaching.MAX_ITEMS:
            first_key = list(self.cache_data.keys())[0]
            del self.cache_data[first_key]
            print(f"DISCARD: {first_key}")

    def get(self, key):
        """get the value of key in cache"""
        return self.cache_data.get(key, None)


if __name__ == "__main__":
    my_cache = FIFOCache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.put("D", "School")
    my_cache.print_cache()
    my_cache.put("E", "Battery")
    my_cache.print_cache()
    my_cache.put("C", "Street")
    my_cache.print_cache()
    my_cache.put("F", "Mission")
    my_cache.print_cache()
