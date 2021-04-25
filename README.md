# GOOpy

You just gooed your last py - python implementation of the java program I wrote "GOO" to find the maximum possible degree of a symmetric group of order n. The order of a symmetric group depends on the cycle lengths in the group. The order is the lcm of all the cycle lengths. Thus, it is in our best interest to find numbers that have no lcm that contribute towards increasing the order.

Currently a brute force algorithm is used and I am in the process of thinking of an optimal way to generate cycles of all relatively prime numbers. I'll implement that algorithm, compare them, and find the big O of each function once I have the optimal algorithm implemented.