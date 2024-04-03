#!/usr/bin/env python3
"""A python script that implements the LFU caching algorithm."""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """A subclass of BaseCaching that implements the LFU caching algorithm."""
    def __init__(self):
        """A method that initializes the class."""
        super().__init__()
        self.lru = []
        self.frequency_counter = {}

    def put(self, key, item):
        """
            A methods that adds an item to the cache.
            args: key - the key of the item to be added.
                  item - the item to be addes.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key in self.lru:
                self.lru.remove(key)
            self.lru.append(key)
            if self.frequency_counter.get(key, None) is None:
                self.frequency_counter[key] = 1
            else:
                self.frequency_counter[key] += 1
        if len(self.cache_data.keys()) > BaseCaching.MAX_ITEMS:
            counter = list(self.frequency_counter.values())
            minimum_value = min(counter)
            multiple_frequency = []
            #  check for multiple minimum value
            for key in self.frequency_counter.keys():
                if self.frequency_counter[key] == minimum_value:
                    multiple_frequency.append(key)
            if len(multiple_frequency) > 1:
                #  if multiple LFU pick the one that occured first
                for item in self.lru:
                    found = None
                    for key in multiple_frequency:
                        if item == key:
                            discard_key = key
                            found = True
                            break
                    if found is True:
                        break
            else:
                discard_key = multiple_frequency.pop()
            del self.cache_data[discard_key]
            self.lru.remove(discard_key)
            del self.frequency_counter[discard_key]
            print(f'DISCARD: {discard_key}')

    def get(self, key):
        """
            A method that retrieves an item from the cache.
            args: key - the key of the item to be retrieved.
        """
        if key is not None and key in self.cache_data.keys():
            if key in self.lru:
                self.lru.remove(key)
            self.lru.append(key)
            if self.frequency_counter.get(key, None) is None:
                self.frequency_counter[key] = 1
            else:
                self.frequency_counter[key] += 1
        return self.cache_data.get(key, None)
