#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == [] or my_list is None:
        return (0)
    reslt = 0
    reslt_2 = 0
    for x, y in my_list:
        reslt += x * y
        reslt_2 += y
    return (reslt / reslt_2)
