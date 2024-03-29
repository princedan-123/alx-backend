#!/usr/bin/env python3
"""A script that paginates a dataset"""
import csv
import math
from typing import List
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
            A method that implements pagination by using the index_range
            function to determine the indices of data to be returned
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        pagination_indices = index_range(page, page_size)
        start_index = pagination_indices[0]
        end_index = pagination_indices[1]
        size = len(self.dataset())
        first_item = self.__dataset[0]
        index_first = self.__dataset.index(first_item)
        if end_index >= size or start_index < index_first:
            return []
        end_index += 1
        data = self.__dataset[start_index:end_index]
        return data
