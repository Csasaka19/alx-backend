#!/usr/bin/env python3
"""Basic caching module"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Basic cache class that allows storing and
    retrieving items from a dictionary."""
    def put(self, key, item):
        """A method that adds an item to the cache"""
        if key is None or item is None:
            return
        else:
            self.cache_data[key] = item

    def get(self, key):
        """A method that gets an item by key"""
        return self.cache_data.get(key, None)
