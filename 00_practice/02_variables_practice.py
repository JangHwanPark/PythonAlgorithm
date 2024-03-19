a, b, c = 1, 2, 3
print(a, b, c)

at, bt, ct = "Orange", "Banan", "Cherry"
print(at, bt, ct)

x = y = z = "Orange"
print(x, y, z)


def global_fn_test():
    global xx
    xx = "fantastic"
    print(xx)


def variable_fn_test():
    yy = "fantastic"
    print(yy)


global_fn_test()
variable_fn_test()
print(xx)