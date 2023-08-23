#!/usr/bin/env python3
"""Last in first out cache module"""
from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """Allows storing and retrival of dictionary and
    uses LIFO removal mechanism"""
    def __init__(self):
        """Initializes tha cache"""
        super().__init__()
        self.cache_data = OrderedDict()

    def get(self, key):
        """Retrieves items from cache"""
        return self.cache_data.get(key, None)

    def put(self, key, item):
        """Inserts items by key to cache and removes by LIFO"""
        if key is None or item is None:
            return
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key, _ = self.cache_data.popitem(True)
            print("DISCARD:", last_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)
