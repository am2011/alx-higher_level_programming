#!/usr/bin/python3
""" Program that returns the Pascal triangle """


def pascal_triangle(n):
    """function return pascal triangle"""
    if n < 0:
        return []
    return [[(11 ** i) for i in range(n)]]
