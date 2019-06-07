def f(x, y, z):
    return [x, y, z]


t = (3, 4)
assert f(2, t, 5) == [2, (3, 4), 5]
assert f(2, 5, t) == [2, 5, (3, 4)]

assert f(2, *t) == [2, 3, 4]
# Values for X and Y are passed in through the tuple!
assert f(z=2, *t) == [3, 4, 2]
# Values for X and Y are passed in through the tuple!
assert f(*t, z=2) == [3, 4, 2]
