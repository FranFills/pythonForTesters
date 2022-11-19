"""
Writing a well-documented code create a function that calculates simple interest (A = Prt)
where A = Annual interest
p = Principal
r = rate
and t = time
"""


def simple_interest(p, n, t):
    r = n/100
    a = p * r * t
    print('Annual interest = ', a)

