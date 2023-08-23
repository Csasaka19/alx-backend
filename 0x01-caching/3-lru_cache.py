#!/usr/bin/env python3
"""Least recently used cache module"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """Allows storing and retrival of dictionary and
    uses LRU removal mechanism"""
    def __init__(self):
        """Initializes tha cache"""
        super().__init__()
        self.cache_data = OrderedDict()

    def get(self, key):
        """Retrieves items from cache"""
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)

    def put(self, key, item):
        """Inserts items by key to cache and removes by LRU"""
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lru_key, _ = self.cache_data.popitem(False)
                print("DISCARD:", lru_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item
