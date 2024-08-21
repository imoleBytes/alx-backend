


from base_caching import BaseCaching


def mru_arrnged(f):
    def wrapper(self, *args):
        f(self, *args)
        if len(self.cache_data) > self.MAX_ITEMS:
            key_to_remove = list(self.cache_data.keys())[-2]
            del self.cache_data[key_to_remove]
            print(f"DISCARD: {key_to_remove}")
    return wrapper


class MRUCache(BaseCaching):
    def __init__(self):
        super().__init__()
    
    @mru_arrnged
    def put(self, key, item):
        if key is None or item is None:
            return
        if key in self.cache_data:
            del self.cache_data[key]
        self.cache_data.update({key: item})
    

    def get(self, key):
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
