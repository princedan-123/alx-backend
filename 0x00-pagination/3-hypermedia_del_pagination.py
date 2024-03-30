#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List
from typing import Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
            A method that uses indexing to implement delete resilient
            pagination
            Args:index(int) the index of entries in a page.
                 page_size(int) the amount of entries per page.
        """
        if self.__indexed_dataset is None:
            self.indexed_dataset()
        valid_index = self.__indexed_dataset.get(index, None)
        if valid_index is None:
            self.__indexed_dataset = None
            self.indexed_dataset()
            valid_index = self.__indexed_dataset.get(index, None)
        assert index is not None and valid_index is not None
        if page_size != 0:
            item = index
            data = []
            count = 0
            for i in range(page_size):
                data.append(self.__indexed_dataset.get(item))
                item += 1
                count += 1
        else:
            data = []
        next_index = index + count
        hateoas = {
            'index': index, 'next_index': next_index, 'page_size': page_size,
            'data': data
        }
        return hateoas
