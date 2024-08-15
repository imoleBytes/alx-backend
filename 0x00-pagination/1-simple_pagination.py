#!/usr/bin/env python3
'''
Copy index_range from the previous task and the following class into your code

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
            pass


Implement a method named get_page that takes two integer arguments page with
default value 1 and page_size with default value 10.

You have to use this CSV file (same as the one presented at the top of
the project)
Use assert to verify that both arguments are integers greater than 0.
Use index_range to find the correct indexes to paginate the dataset
correctly and return the appropriate page of the dataset (i.e. the
correct list of rows).
If the input arguments are out of range for the dataset, an empty list
should be returned.
'''
import csv
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """return a tupleof start and end index"""
    start = (page - 1) * page_size
    end = page * page_size

    return start, end


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
        """get results within the range specifed"""
        assert type(page) == int and type(page_size) == int
        assert (page * page_size) > 0

        if (page * page_size) > len(self.dataset()):
            return []

        start, end = index_range(page, page_size)
        out = self.dataset()[start:end]
        return out


if __name__ == "__main__":
    server = Server()

    try:
        should_err = server.get_page(-10, 2)
    except AssertionError:
        print("AssertionError raised with negative values")

    try:
        should_err = server.get_page(0, 0)
    except AssertionError:
        print("AssertionError raised with 0")

    try:
        should_err = server.get_page(2, 'Bob')
    except AssertionError:
        print("AssertionError raised when page and/or page_size are not ints")

    print(server.get_page(1, 3))
    print(server.get_page(3, 2))
    print(server.get_page(3000, 100))
