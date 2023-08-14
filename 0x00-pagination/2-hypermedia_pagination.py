#!/usr/bin/env python3
"""Definition of a class Server"""
import csv
import math
from typing import List, Dict


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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Takes two args and returns dictionary"""
        inst_page = isinstance(page, int)
        inst_page_size = isinstance(page_size, int)
        assert inst_page and inst_page_size, "Must be integers"
        assert page > 0 and page_size > 0, "Must be positive val"
        data = self.get_page(page, page_size)
        page_length = len(self.get_page(page + 1, page_size))
        if page_length > 0:
            next_page = page + 1
        else:
            next_page = None
        if page_length == 1:
            prev_page = None
        if page_length > 1:
            prev_page = page - 1
        else:
            prev_page = None
        total_pages = math.ceil(len(self.dataset()) / page_size)

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
