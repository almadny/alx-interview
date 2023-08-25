#!/usr/bin/python3
""" Module that makes change function """


def makeChange(coins, total):
    """Determines the fewest coins needed to make a change"""
    if total <= 0:
        return 0
    if len(coins) == 0:
        return -1
    coins.sort(reverse=True)

    my_tot = 0
    count = 0
    list_ind = 0
    list_len = len(coins)

    while my_tot < total:
        if list_ind >= list_len:
            break
        if my_tot + coins[list_ind] <= total:
            my_tot = my_tot + coins[list_ind]
            count = count + 1
            continue
        list_ind = list_ind + 1

    if my_tot < total:
        return -1
    if my_tot == total:
        return count
