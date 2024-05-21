#!/usr/bin/env python3
"""Module for task 1
"""
import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns a tuple of size two containing a start index and an end
    index corresponding to the range of indexes to return in a list for the
    given pagination parameters.

    Args:
        page (int): the number of the page
        page_size (int): the number of items per page

    Returns:
        Tuple[int, int]: start and end indexes of current page.
    """
    # calculate start index by subtracting 1 from the current page number
    # and then multiplying by the page size
    start_index = (page - 1) * page_size
    # calculate end index by adding the start index to the page size
    end_index = start_index + page_size
    # return the start and end indexes as a tuple
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        # a private attribute to store the dataset
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset

        Returns:
            List[List]: The list of rows representing the dataset.
        """
        # check if the dataset has not been loaded yet
        if self.__dataset is None:
            # open the csv file
            with open(self.DATA_FILE) as f:
                # read the csv file
                reader = csv.reader(f)
                dataset = [row for row in reader]
            # store the dataset in the private attribute
            self.__dataset = dataset[1:]
        # return the dataset
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieves a specific page of the dataset of popular baby names.

        Args:
            page (int, optional): the number of the page to retrieve.
            Defaults to 1.
            page_size (int, optional): the number of items per page.
            Defaults to 10.

        Returns:
            List[List]: a list of rows representing the requested page of
            the dataset.
        """
        # Verify that both page and page_size are integers greater than 0
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        # Find the correct start and end indexes for the current page
        start_index, end_index = index_range(page, page_size)
        # Retrieve the dataset
        dataset = self.dataset()
        # Check if the end_index is greater than the length of the dataset
        # If it is, return an empty list
        if end_index > len(dataset):
            return []
        # Return the appropriate page of the dataset
        return dataset[start_index:end_index]
