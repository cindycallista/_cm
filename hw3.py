import cmath

def root3(a, b, c, d):
    A = b / a
    B = c / a
    C = d / a

    p = B - (A**2 / 3)
    q = (2 * A**3 / 27) - (A * B / 3) + C

    delta = (q**2 / 4) + (p**3 / 27)
    sqrt_delta = cmath.sqrt(delta)

    u_base = -q/2 + sqrt_delta
    v_base = -q/2 - sqrt_delta

    u = cmath.exp(cmath.log(u_base) / 3) if u_base != 0 else 0
    v = cmath.exp(cmath.log(v_base) / 3) if v_base != 0 else 0

    w1 = complex(-0.5, cmath.sqrt(3)/2)
    w2 = complex(-0.5, -cmath.sqrt(3)/2)

    t1 = u + v
    t2 = u * w1 + v * w2
    t3 = u * w2 + v * w1

    offset = A / 3
    return t1 - offset, t2 - offset, t3 - offset

def verify(a, b, c, d, roots):
    f = lambda x: a*x**3 + b*x**2 + c*x + d
    for r in roots:
        res = f(r)
        is_correct = cmath.isclose(res, 0, abs_tol=1e-9)
        print(f"Root: {r}")
        print(f"f(x): {res}")
        print(f"Is Zero: {is_correct}\n")

if __name__ == "__main__":
    # Test: x^3 - 6x^2 + 11x - 6 = 0 (Roots: 1, 2, 3)
    a, b, c, d = 1, -6, 11, -6
    roots = root3(a, b, c, d)
    verify(a, b, c, d, roots)
