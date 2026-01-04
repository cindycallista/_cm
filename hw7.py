import numpy as np
import decimal
import math

decimal.getcontext().prec = 50
p_val = decimal.Decimal('0.5')
n_val = 10000
prob_direct = p_val ** n_val
print(f"1. Probability (0.5^10000): {prob_direct}\n")

log_prob = n_val * math.log2(0.5)
print(f"2. Log Probability: {log_prob} bits\n")

def entropy(p):
    p = np.array(p)
    return -np.sum(p * np.log2(p + 1e-12))

def cross_entropy(p, q):
    p = np.array(p)
    q = np.array(q)
    return -np.sum(p * np.log2(q + 1e-12))

def kl_divergence(p, q):
    p = np.array(p)
    q = np.array(q)
    return np.sum(p * np.log2((p + 1e-12) / (q + 1e-12)))

def mutual_information(p_xy):
    p_xy = np.array(p_xy)
    p_x = np.sum(p_xy, axis=1)
    p_y = np.sum(p_xy, axis=0)
    mi = 0
    for i in range(len(p_x)):
        for j in range(len(p_y)):
            if p_xy[i, j] > 0:
                mi += p_xy[i, j] * math.log2(p_xy[i, j] / (p_x[i] * p_y[j]))
    return mi

p_dist = [0.5, 0.5]
q_dist = [0.8, 0.2]
joint_xy = [[0.4, 0.1], [0.1, 0.4]]

print(f"3. Metrics:")
print(f"   Entropy: {entropy(p_dist)}")
print(f"   Cross Entropy: {cross_entropy(p_dist, q_dist)}")
print(f"   KL Divergence: {kl_divergence(p_dist, q_dist)}")
print(f"   Mutual Information: {mutual_information(joint_xy)}\n")

h_pp = cross_entropy(p_dist, p_dist)
h_pq = cross_entropy(p_dist, q_dist)
print(f"4. Verification: H(p,p)={h_pp:.4f}, H(p,q)={h_pq:.4f}")
print(f"   Is H(p,q) > H(p,p)? {h_pq > h_pp}\n")

G = np.array([[1,1,0,1], [1,0,1,1], [1,0,0,0], [0,1,1,1], [0,1,0,0], [0,0,1,0], [0,0,0,1]])
H = np.array([[1,0,1,0,1,0,1], [0,1,1,0,0,1,1], [0,0,0,1,1,1,1]])

def hamming_encode(data):
    return np.dot(G, data) % 2

def hamming_decode(received):
    syndrome = tuple(np.dot(H, received) % 2)
    corrected = received.copy()
    if any(syndrome):
        syn_val = syndrome[0] + syndrome[1]*2 + syndrome[2]*4
        corrected[syn_val - 1] = (corrected[syn_val - 1] + 1) % 2
    return corrected[[2, 4, 5, 6]]

data_bits = np.array([1, 0, 1, 1])
codeword = hamming_encode(data_bits)
codeword[0] = (codeword[0] + 1) % 2 # Simulate 1-bit error
decoded_bits = hamming_decode(codeword)

print(f"5. Hamming (7,4):")
print(f"   Original: {data_bits}")
print(f"   Decoded:  {decoded_bits}")
