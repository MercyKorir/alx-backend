#!/usr/bin/python3
"""Definition of class LIFOCache"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Inherits from BaseCaching"""

    def __init__(self):
        """Initializes LIFOCache class"""

        super().__init__()

    def put(self, key, item):
        """assigns dictionary value for key"""

        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                last_key = list(self.cache_data.keys())[-2]
                print("DISCARD: {}".format(last_key))
                del self.cache_data[last_key]

    def get(self, key):
        """Return value linked to key"""

        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
