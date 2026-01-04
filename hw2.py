import cmath

def root2(a, b, c):
    d = (b**2) - (4*a*c)
    
    sol1 = (-b + cmath.sqrt(d)) / (2*a)
    sol2 = (-b - cmath.sqrt(d)) / (2*a)
    
    return sol1, sol2

def verify_roots(a, b, c, roots):
    f = lambda x: a*x**2 + b*x + c
    
    for r in roots:
        result = f(r)
        is_zero = cmath.isclose(result, 0, abs_tol=1e-9)
        print(f"Root: {r}")
        print(f"f(root) = {result}")
        print(f"Is close to zero? {is_zero}")
        print("-" * 20)

if __name__ == "__main__":
    # Example 1: Real roots (x^2 - 5x + 6 = 0)
    print("Example 1: Real roots")
    a1, b1, c1 = 1, -5, 6
    roots1 = root2(a1, b1, c1)
    verify_roots(a1, b1, c1, roots1)

    # Example 2: Complex roots (x^2 + x + 1 = 0)
    print("Example 2: Complex roots")
    a2, b2, c2 = 1, 1, 1
    roots2 = root2(a2, b2, c2)
    verify_roots(a2, b2, c2, roots2)
