#!/usr/bin/env python3
"""A python script that implements the MRU caching algorithm."""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """A subclass of BaseCaching that implements the MRU caching algorithm."""
    def __init__(self):
        """A method that initializes the class."""
        super().__init__()
        self.most_recent_key = None

    def put(self, key, item):
        """
            A methods that adds an item to the cache.
            args: key - the key of the item to be added.
                  item - the item to be added.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
        if len(self.cache_data.keys()) > BaseCaching.MAX_ITEMS:
            delete_key = self.most_recent_key
            del self.cache_data[delete_key]
            print(f'DISCARD: {delete_key}')
        self.most_recent_key = key

    def get(self, key):
        """
            A method that retrieves an item from the cache.
            args: key - the key of the item to be retrieved.
        """
        if key is not None and self.cache_data.get(key) is not None:
            self.most_recent_key = key
        return self.cache_data.get(key, None)
