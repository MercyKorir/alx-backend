#!/usr/bin/python3
"""Definition of a class BasicCache"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Inherits from BaseCaching"""

    def put(self, key, item):
        """Assigns dictionary a value for key"""

        if key is not None and item is not None:
            self.cache_data[key] = item
    
    def get(self, key):
        """Returns value linked to key"""

        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]