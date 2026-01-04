import cmath

def dft(f):
    N = len(f)
    F = []
    for k in range(N):
        sum_val = complex(0, 0)
        for n in range(N):
            angle = -2j * cmath.pi * k * n / N
            sum_val += f[n] * cmath.exp(angle)
        F.append(sum_val)
    return F

def idft(F):
    N = len(F)
    f = []
    for n in range(N):
        sum_val = complex(0, 0)
        for k in range(N):
            angle = 2j * cmath.pi * k * n / N
            sum_val += F[k] * cmath.exp(angle)
        f.append(sum_val / N)
    return f

f_original = [1.0, 0.0, -1.0, 0.0, 1.0]

F_omega = dft(f_original)
f_reconstructed = idft(F_omega)

print("Original Signal f(x):")
print(f_original)
print("\nDFT Result F(omega) (Complex):")
for val in F_omega:
    print(f"{val.real:.3f} + {val.imag:.3f}j")

print("\nReconstructed Signal f(x) after IDFT:")
for val in f_reconstructed:
    print(f"{val.real:.3f}")

is_match = all(cmath.isclose(f_original[i], f_reconstructed[i].real, abs_tol=1e-9) for i in range(len(f_original)))
print(f"\nVerification Success: {is_match}")
