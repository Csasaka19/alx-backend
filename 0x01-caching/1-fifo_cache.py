#!/usr/bin/python3
"""First in first out cache module"""
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """Allows storing and retrival of dictionary and
    uses FIFO removal mechanism"""
    def __init__(self):
        """Initializes tha cache"""
        super().__init__()
        self.cache_data = OrderedDict()

    def get(self, key):
        """Retrieves items from cache"""
        return self.cache_data.get(key, None)

    def put(self, key, item):
        """Inserts items by key to cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD: ", first_key)
