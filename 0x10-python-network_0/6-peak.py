#!/usr/bin/python3
"""contains the function find_peak"""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
    lst = list_of_integers
    l = len(lst)
    if l == 0:
        return
    m = l // 2
    if (m == l - 1 or lst[m] >= lst[m + 1]) and (m == 0 or lst[m] >= lst[m - 1]):
        return lst[m]
    if m != l - 1 and lst[m + 1] > lst[m]:
        return find_peak(lst[m + 1:])
    return find_peak(lst[:m])
