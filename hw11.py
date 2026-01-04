import numpy as np
from collections import Counter

def solve_ode_general(coefficients):
    roots = np.roots(coefficients)
    
    rounded_roots = []
    for r in roots:
        real_part = round(r.real, 10)
        imag_part = round(r.imag, 10)
        rounded_roots.append(complex(real_part, imag_part))
    
    counts = Counter(rounded_roots)
    
    terms = []
    processed_complex_pairs = set()
    term_count = 1
    
    unique_roots = sorted(counts.keys(), key=lambda x: (x.real, x.imag), reverse=True)
    
    for r in unique_roots:
        multiplicity = counts[r]
        
        if abs(r.imag) < 1e-10:
            for i in range(multiplicity):
                x_power = f"x^{i}" if i > 1 else ("x" if i == 1 else "")
                terms.append(f"C_{term_count}{x_power}e^({r.real}x)")
                term_count += 1
        else:
            alpha = r.real
            beta = abs(r.imag)
            
            if (alpha, beta) in processed_complex_pairs:
                continue
            
            for i in range(multiplicity):
                x_power = f"x^{i}" if i > 1 else ("x" if i == 1 else "")
                exp_part = f"e^({alpha}x)" if alpha != 0 else ""
                
                terms.append(f"C_{term_count}{x_power}{exp_part}cos({beta}x)")
                term_count += 1
                terms.append(f"C_{term_count}{x_power}{exp_part}sin({beta}x)")
                term_count += 1
                
            processed_complex_pairs.add((alpha, beta))

    return "y(x) = " + " + ".join(terms)

print("--- 實數單根範例 ---")
coeffs1 = [1, -3, 2]
print(f"方程係數: {coeffs1}")
print(solve_ode_general(coeffs1))

print("\n--- 實數重根範例 ---")
coeffs2 = [1, -4, 4]
print(f"方程係數: {coeffs2}")
print(solve_ode_general(coeffs2))

print("\n--- 複數共軛根範例 ---")
coeffs3 = [1, 0, 4]
print(f"方程係數: {coeffs3}")
print(solve_ode_general(coeffs3))

print("\n--- 複數重根範例 ---")
coeffs4 = [1, 0, 2, 0, 1]
print(f"方程係數: {coeffs4}")
print(solve_ode_general(coeffs4))

print("\n--- 高階重根範例 ---")
coeffs5 = [1, -6, 12, -8]
print(f"方程係數: {coeffs5}")
print(solve_ode_general(coeffs5))
