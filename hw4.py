import cmath
import random

def evaluate(c, x):
    res = 0
    for coeff in reversed(c):
        res = res * x + coeff
    return res

def derivative(c):
    return [i * c[i] for i in range(1, len(c))]

def find_one_root(c, start_x, iterations=1000):
    x = start_x
    c_prime = derivative(c)
    for _ in range(iterations):
        fx = evaluate(c, x)
        if abs(fx) < 1e-13:
            break
        dfx = evaluate(c_prime, x)
        if abs(dfx) == 0: 
            x += complex(random.random(), random.random())
            continue
        x = x - fx / dfx
    return x

def deflate(c, r):
    n = len(c) - 1
    new_c = [0] * n
    rem = 0
    for i in range(n, 0, -1):
        new_c[i-1] = c[i] + rem
        rem = new_c[i-1] * r
    return new_c

def root(c):
    roots = []
    current_poly = [complex(x) for x in c]
    n = len(c) - 1
    for _ in range(n):
        r = find_one_root(current_poly, complex(random.random(), random.random()))
        roots.append(r)
        current_poly = deflate(current_poly, r)
    return roots

if __name__ == "__main__":
    coeffs = [-1, 0, 0, 0, 0, 1]
    all_roots = root(coeffs)
    for r in all_roots:
        val = evaluate(coeffs, r)
        print(f"Root: {r}, f(root): {val:.2e}, Close: {cmath.isclose(val, 0, abs_tol=1e-7)}")
