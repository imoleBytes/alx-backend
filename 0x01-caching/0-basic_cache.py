#!/usr/bin/env python3
"""
Create a class BasicCache that inherits from BaseCaching and is a
caching system:

You must use self.cache_data - dictionary from the parent class BaseCaching
This caching system doesn’t have limit
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn't exist in self.cache_data, return None.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Implements basicCahe, """
    def __init__(self):
        """initialize instance of the class"""
        super().__init__()
        self.MAX_ITEMS = None

    def put(self, key, item):
        """insert the value in cache"""
        if key and item:
            self.cache_data.update([(key, item)])

    def get(self, key):
        """get the value of key in cache"""
        return self.cache_data.get(key, None)


if __name__ == "__main__":
    my_cache = BasicCache()
    my_cache.print_cache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.print_cache()
    print(my_cache.get("A"))
    print(my_cache.get("B"))
    print(my_cache.get("C"))
    print(my_cache.get("D"))
    my_cache.print_cache()
    my_cache.put("D", "School")
    my_cache.put("E", "Battery")
    my_cache.put("A", "Street")
    my_cache.print_cache()
    print(my_cache.get("A"))
