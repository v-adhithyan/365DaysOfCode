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

d = {"z": 4, "y": 3, "x": 2}
assert f(**d) == [2, 3, 4]
d = {"z": 4, "y": 3}
assert f(2, **d) == [2, 3, 4]
d = {"y": 3}
assert f(2, z=4, **d) == [2, 3, 4]
assert f(2, **d, z=4) == [2, 3, 4]
t = (3,)
d = {"z": 4}
assert f(2, *t, **d) == [2, 3, 4]
assert f(y=3, *t, **d) == [3, 3, 4]
assert f(*t, y=3, **d) == [3, 3, 4]
assert f(*t, **d, y=3) == [3, 3, 4]
