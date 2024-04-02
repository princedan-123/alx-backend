#!/usr/bin/env python3
"""A python script that implements the LRU caching algorithm."""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """A subclass of BaseCaching that implements the LRU caching algorithm."""
    def __init__(self):
        """A method that initializes the class."""
        super().__init__()
        self.used_keys = []

    def put(self, key, item):
        """
            A methods that adds an item to the cache.
            args: key - the key of the item to be added.
                  item - the item to be addes.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
        if len(self.cache_data.keys()) > BaseCaching.MAX_ITEMS:
            delete_key = None
            for key in self.cache_data.keys():
                if key not in self.used_keys:
                    delete_key = key
                    break
            if delete_key is None:
                delete_key = self.used_keys.pop(0)
            del self.cache_data[delete_key]
            print(f'DISCARD: {key}')

    def get(self, key):
        """
            A method that retrieves an item from the cache.
            args: key - the key of the item to be retrieved.
        """
        if key is not None and key in self.cache_data.keys():
            self.used_keys.append(key)
        return self.cache_data.get(key, None)
