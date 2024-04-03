#!/usr/bin/env python3
"""A python script that implements the LIFO caching algorithm."""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """A subclass of BaseCaching that implements the LIFO caching algorithm."""
    def __init__(self):
        """A method that initializes the class."""
        super().__init__()
        self.lifo = []

    def put(self, key, item):
        """
            A methods that adds an item to the cache.
            args: key - the key of the item to be added.
                  item - the item to be addes.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.lifo.append(key)
        if len(self.cache_data.keys()) > BaseCaching.MAX_ITEMS:
            discard_key = self.lifo.pop(-2)
            del self.cache_data[discard_key]
            self.cache_data[key] = item
            print(f'DISCARD: {discard_key}')

    def get(self, key):
        """
            A method that retrieves an item from the cache.
            args: key - the key of the item to be retrieved.
        """
        return self.cache_data.get(key, None)
