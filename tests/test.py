from kwargs_decorator.main import kwargs_decorator_generator


@kwargs_decorator_generator("""
    a,
    b,
    c= a+b,
    d=a+b,
    e =a+b,
    f = c*3,
    g=d*3, 
    h = e * 3
""")
def f(a, b, c, d, e, f, g, h):
    print(f"a = {a}\nb = {b}\nc = {c}\nd = {d}\ne = {e}\nf = {f}\ng = {g}\nh = {h}")


f("x", "z", 0, e=5)
