#!/usr/bin/python3
"""Definition of class LRUCache"""
from base_caching import BaseCaching
import collections


class LRUCache(BaseCaching):
    """Inherits from BaseCaching"""

    def __init__(self):
        """Creating an instance of LRUCache"""

        super().__init__()
        self.order = collections.OrderedDict()

    def put(self, key, item):
        """Assigns dictionary value for key"""

        if key is not None and item is not None:
            self.cache_data[key] = item
            self.order[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                res_key, _ = self.order.popitem(last=False)
                print("DISCARD: {}".format(res_key))
                del self.cache_data[res_key]

    def get(self, key):
        """return value linked to key"""

        if key is None or key not in self.cache_data:
            return None
        val = self.cache_data[key]
        self.order.move_to_end(key)
        return val
