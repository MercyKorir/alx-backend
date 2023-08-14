#!/usr/bin/python3
"""Definition of the class MRUCache"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Inherits from BaseCaching"""

    def __init__(self):
        """Initialization of the class"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Assigns dictionary value for key"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            self.order.remove(key)
            self.order.append(key)
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                res_key = self.order.pop()
                del self.cache_data[res_key]
                print("DISCARD: {}".format(res_key))
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """return value linked to key"""
        if key is None or key not in self.cache_data:
            return None
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
