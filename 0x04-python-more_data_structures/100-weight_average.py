#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    avg = 0
    dnm = 0
    for t in my_list:
        avg += t[0] * t[1]
        dnm += t[1]
    avg /= dnm
    return avg
