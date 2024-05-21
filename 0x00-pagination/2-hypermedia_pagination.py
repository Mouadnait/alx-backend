#!/usr/bin/env python3
""" module doc """
import csv
import math
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """ func doc """
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
        """Get page from the dataset"""
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        start, end = self.index_range(page, page_size)
        return self.dataset()[start:end]

    def index_range(self, page: int, page_size: int) -> tuple:
        """returns a tuple of size two
        containing a start index and an end index"""
        return (page - 1) * page_size, page * page_size

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """returns a dictionary"""
        start, end = self.index_range(page, page_size)
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if end < len(self.dataset()) else None,
            "prev_page": page - 1 if start > 0 else None,
            "total_pages": total_pages
        }
