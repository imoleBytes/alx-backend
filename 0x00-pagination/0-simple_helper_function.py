#!/usr/bin/env python3
"""
Write a function named index_range that takes two integer arguments page
and page_size.

The function should return a tuple of size two containing a start index
and an end index corresponding to the range of indexes to return in a list
for those particular pagination parameters.

Page numbers are 1-indexed, i.e. the first page is page 1.
"""


def index_range(page: int, page_size: int) -> tuple:
    """return a tupleof start and end index"""
    # if page < 1:
    #     raise KeyError("Page numbers are 1-indexed, i.e.
    # the first page is page 1.")

    start = (page - 1) * page_size
    end = page * page_size

    return start, end


if __name__ == "__main__":
    res = index_range(1, 7)
    print(type(res))
    print(res)

    res = index_range(page=3, page_size=15)
    print(type(res))
    print(res)
