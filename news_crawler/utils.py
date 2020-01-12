from itertools import chain


def flattened_list(lst):
    return list(chain(*lst))
