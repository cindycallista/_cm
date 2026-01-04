def integral(f, a, b, n=10000):
    h = (b - a) / n
    s = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        s += f(a + i * h)
    return s * h

def df(f, x, h=1e-7):
    return (f(x + h) - f(x - h)) / (2 * h)

def theorem1(f, x):
    result = df(lambda t: integral(f, 0, t), x)
    expected = f(x)
    
    print(f"Result: {result}")
    print(f"Expected: {expected}")
    
    assert abs(result - expected) < 1e-5
    print("Verification Successful")

if __name__ == "__main__":
    f = lambda x: x**2 + 3*x + 2
    theorem1(f, 2)
