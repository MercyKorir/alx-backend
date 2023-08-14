#!/usr/bin/env python3
"""Declaration and definition of a function index_range"""


def index_range(page: int, page_size: int) -> tuple:
    """Takes two args and returns a tuple"""

    first_idx = (page - 1) * page_size
    last_idx = first_idx + page_size

    return (first_idx, last_idx)
