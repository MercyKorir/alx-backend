#!/usr/bin/python3
"""Definition of class FIFOCache"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Inherits from BaseCaching"""

    def __init__(self):
        """Initializes FIFOCache class"""

        super().__init__()
    
    def put(self, key, item):
        """assigns dictionary value of key"""

        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                first = next(iter(self.cache_data))
                del self.cache_data[first]
                print("DISCARD: {}".format(first))
            self.cache_data[key] = item
    
    def get(self, key):
        """Return value linked to key"""

        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]