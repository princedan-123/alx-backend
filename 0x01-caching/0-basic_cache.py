#!/usr/bin/env python3
"""A Python script that inherits from a base class and implements a cache."""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """A subclass that inherits from BaseCaching class."""
    def __init__(self):
        """An initialization method of the subclass."""
        super().__init__()

    def put(self, key, item):
        """
            A method that is used to add data to the cache.
            args: key - the key of the data to be added.
                  item - the item to be added.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
            A method that retrieves data from the cache.
            args: key - the key with which to retrieve the data.
        """
        if key is not None:
            return self.cache_data.get(key, None)
