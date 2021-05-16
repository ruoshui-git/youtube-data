from collections.abc import Iterable
import itertools
from typing import TypeVar

T = TypeVar('T')

def chunks(iterable: Iterable[T], n: int) -> list[Iterable[T]]:
    "Collect data into chunks, not necessarily exact"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    fillvalue = object()
    args = [iter(iterable)] * n
    # return [tuple(x for x in item if x is not fillvalue) for item in itertools.zip_longest(args, fillvalue=fillvalue)]
    [*_list, last] = list(itertools.zip_longest(*args, fillvalue=fillvalue))
    last = tuple(item for item in last if item is not fillvalue)
    return [*_list, last]