#!/usr/bin/env python3
"""
Replicate code from the previous task.

Implement a get_hyper method that takes the same arguments
(and defaults) as get_page and returns a dictionary containing
the following key-value pairs:

page_size: the length of the returned dataset page
page: the current page number
data: the dataset page (equivalent to return from previous task)
next_page: number of the next page, None if no next page
prev_page: number of the previous page, None if no previous page
total_pages: the total number of pages in the dataset as an integer
Make sure to reuse get_page in your implementation.

You can use the math module if necessary.

"""
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
        """init obj"""
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
        result = self.dataset()[start:end]
        return result

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """returns a dictionary containing the following key-value pairs:
        page_size, page, data, next_page, prev_page, total_pages
        """
        returned_data = self.get_page(page, page_size)

        total_pges = len(self.__dataset) // page_size if len(self.__dataset)\
            % page_size == 0 else len(self.__dataset) // page_size + 1

        result = {
            "page_size": len(returned_data),
            "page": page,
            "data": returned_data,
            "next_page": page + 1 if (page + 1) <= total_pges else None,
            "prev_page": page - 1 if (page - 1) > 0 else None,
            "total_pages": total_pges
        }
        return result


if __name__ == "__main__":

    server = Server()

    print(server.get_hyper(1, 2))
    print("---")
    print(server.get_hyper(2, 2))
    print("---")
    print(server.get_hyper(100, 3))
    print("---")
    print(server.get_hyper(3000, 100))
