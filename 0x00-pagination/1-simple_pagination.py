#!/usr/bin/env python3
"""Definition of a class Server"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """Takes two args and returns a tuple"""

    first_idx = (page - 1) * page_size
    last_idx = first_idx + page_size

    return (first_idx, last_idx)


class Server:
    """
    Server class to paginate a database of popular baby names
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Takes two args and returns a list of lists"""
        inst_page = isinstance(page, int)
        inst_page_size = isinstance(page_size, int)
        assert inst_page and inst_page_size, "Must be integers"
        assert page > 0 and page_size > 0, "Must be positive val"
        first_idx, last_idx = index_range(page, page_size)
        if first_idx >= len(self.dataset()):
            return []
        return self.dataset()[first_idx:last_idx]
