#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list != []:
        prod_sum = 0
        wght_sum = 0
        for tup in my_list:
            prod_sum += tup[0] * tup[1]
            wght_sum += tup[1]
        return prod_sum/wght_sum
    return 0
