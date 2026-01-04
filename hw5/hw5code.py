import cmath

class FiniteFieldElement:
    def __init__(self, value, p):
        self.p = p
        self.value = value % p

    def __add__(self, other):
        return FiniteFieldElement(self.value + other.value, self.p)

    def __sub__(self, other):
        return FiniteFieldElement(self.value - other.value, self.p)

    def __mul__(self, other):
        return FiniteFieldElement(self.value * other.value, self.p)

    def __truediv__(self, other):
        return self * other.inverse()

    def inverse(self):
        return FiniteFieldElement(pow(self.value, -1, self.p), self.p)

    def __neg__(self):
        return FiniteFieldElement(-self.value, self.p)

    def __eq__(self, other):
        if isinstance(other, FiniteFieldElement):
            return self.value == other.value and self.p == other.p
        return False

    def __repr__(self):
        return f"{self.value}"

class FiniteFieldAddGroup:
    def __init__(self, p):
        self.p = p
        self.elements = [FiniteFieldElement(i, p) for i in range(p)]
        self.identity = FiniteFieldElement(0, p)

    def op(self, a, b):
        return a + b

    def inv(self, a):
        return -a

class FiniteFieldMulGroup:
    def __init__(self, p):
        self.p = p
        self.elements = [FiniteFieldElement(i, p) for i in range(1, p)]
        self.identity = FiniteFieldElement(1, p)

    def op(self, a, b):
        return a * b

    def inv(self, a):
        return a.inverse()

def check_group_axioms(group):
    for a in group.elements:
        if group.op(a, group.identity) != a or group.op(group.identity, a) != a:
            return False
        if group.op(a, group.inv(a)) != group.identity:
            return False
    return True

def check_distributivity(p):
    elements = [FiniteFieldElement(i, p) for i in range(p)]
    for a in elements:
        for b in elements:
            for c in elements:
                if a * (b + c) != (a * b) + (a * c):
                    return False
    return True

if __name__ == "__main__":
    p = 7
    add_group = FiniteFieldAddGroup(p)
    mul_group = FiniteFieldMulGroup(p)
    
    print(f"P={p}")
    print(f"Addition Group Verified: {check_group_axioms(add_group)}")
    print(f"Multiplication Group Verified: {check_group_axioms(mul_group)}")
    print(f"Distributivity Verified: {check_distributivity(p)}")
    
    a = FiniteFieldElement(3, p)
    b = FiniteFieldElement(5, p)
    print(f"Example: {a} / {b} = {a / b}")
