#!/usr/bin/python3
"""Definition of class LFUCache"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Inherits from BaseCaching"""

    def __init__(self):
        """Initialization of class"""

        super().__init__()
        self.lfu = {}
        self.lru = {}

    def put(self, key, item):
        """Assigns dictionary value for key"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            self.lfu[key] += 1
            self.lru[key] = len(self.lru)
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                min_freq = min(self.lfu.values())
                lfu_keys = [k for k, v in self.lfu.items() if v == min_freq]
                if len(lfu_keys) == 1:
                    lfu_key = lfu_keys[0]
                else:
                    min_rec = min(self.lru[k] for k in lfu_keys)
                    check_item = self.lru.items()
                    lfu_key = [k for k, v in check_item if v == min_rec][0]
                print("DISCARD: {}".format(lfu_key))
                del self.cache_data[lfu_key]
                del self.lfu[lfu_key]
                del self.lru[lfu_key]
            self.cache_data[key] = item
            self.lfu[key] = 1
            self.lru[key] = len(self.lru)

    def get(self, key):
        """return value linked to key"""
        if key is None or key not in self.cache_data:
            return None
        self.lfu[key] += 1
        self.lru[key] = len(self.lru)
        return self.cache_data[key]
